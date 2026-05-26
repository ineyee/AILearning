#!/usr/bin/env python3
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


DART_PATH_RE = re.compile(r"""(?P<path>(?:file://)?(?:~|/|\./|\.\./)?[^\s'"`<>|&;]+?\.dart)""")
WRITE_COMMAND_RE = re.compile(
    r"""(^|\s)(touch|tee|mv|cp|install|python3?|node|ruby|perl|sed\s+-i)\b|>{1,2}""",
    re.IGNORECASE,
)


def load_event() -> dict:
    try:
        data = json.load(sys.stdin)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)


def token_to_path(token: str) -> str:
    token = token.strip().strip("'\"`")
    token = token.rstrip(",:)")
    if token.startswith("file://"):
        parsed = urlparse(token)
        return unquote(parsed.path)
    return token


def within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_dart_file(token: str, root: Path) -> Path | None:
    raw = token_to_path(token)
    if not raw.endswith(".dart"):
        return None

    candidates = [raw]
    if raw.startswith(("a/", "b/")):
        candidates.append(raw[2:])

    for candidate in candidates:
        path = Path(candidate).expanduser()
        if not path.is_absolute():
            path = root / path
        path = path.resolve(strict=False)
        if path.suffix == ".dart" and within(path, root) and path.is_file():
            return path
    return None


def collect_paths_from_event(data: dict, root: Path) -> list[Path]:
    paths: list[Path] = []
    seen: set[Path] = set()

    for text in walk_strings(data.get("tool_input", data)):
        for match in DART_PATH_RE.finditer(text):
            path = resolve_dart_file(match.group("path"), root)
            if path and path not in seen:
                seen.add(path)
                paths.append(path)

    return paths


def command_text(data: dict) -> str:
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return ""
    cmd = tool_input.get("cmd") or tool_input.get("command")
    return cmd if isinstance(cmd, str) else ""


def tool_can_modify_files(data: dict) -> bool:
    tool_name = str(data.get("tool_name") or "").lower()
    if any(marker in tool_name for marker in ("apply_patch", "write", "edit", "create")):
        return True

    if "exec" in tool_name or "shell" in tool_name or "command" in tool_name:
        return bool(WRITE_COMMAND_RE.search(command_text(data)))

    return False


def can_use_git_fallback(data: dict) -> bool:
    tool_name = str(data.get("tool_name") or "").lower()
    if any(marker in tool_name for marker in ("apply_patch", "write", "edit", "create")):
        return True

    cmd = command_text(data)
    return ".dart" in cmd and bool(WRITE_COMMAND_RE.search(cmd))


def git_paths(args: list[str], root: Path) -> list[Path]:
    try:
        result = subprocess.run(
            args,
            cwd=root,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return []

    if result.returncode != 0:
        return []

    paths: list[Path] = []
    for line in result.stdout.splitlines():
        path = resolve_dart_file(line, root)
        if path:
            paths.append(path)
    return paths


def collect_git_fallback(root: Path) -> list[Path]:
    paths = git_paths(["git", "diff", "--name-only", "--diff-filter=ACMRT", "--", "*.dart"], root)
    paths.extend(git_paths(["git", "ls-files", "--others", "--exclude-standard", "--", "*.dart"], root))

    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if path not in seen:
            seen.add(path)
            unique.append(path)
    return unique


def find_dart_command() -> list[str] | None:
    dart = shutil.which("dart")
    if dart:
        return [dart, "format"]

    fvm = shutil.which("fvm")
    if fvm:
        return [fvm, "dart", "format"]

    flutter = shutil.which("flutter")
    if flutter:
        dart_from_flutter = Path(flutter).resolve().parent / "cache" / "dart-sdk" / "bin" / "dart"
        if dart_from_flutter.exists():
            return [str(dart_from_flutter), "format"]

    return None


def format_paths(paths: list[Path], root: Path) -> int:
    command = find_dart_command()
    if not command:
        print("[dart-format-hook] skipped: dart formatter not found on PATH", file=sys.stderr)
        return 0

    relative_paths = [str(path.relative_to(root)) for path in paths]
    result = subprocess.run(
        [*command, *relative_paths],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )

    output = (result.stdout + result.stderr).strip()
    if output:
        print(output, file=sys.stderr)

    if result.returncode != 0:
        print(
            f"[dart-format-hook] formatter exited with code {result.returncode}; continuing without blocking Codex",
            file=sys.stderr,
        )
    return 0


def main() -> int:
    data = load_event()
    if data.get("hook_event_name") != "PostToolUse":
        return 0
    if not tool_can_modify_files(data):
        return 0

    cwd = data.get("cwd") or os.getcwd()
    root = Path(cwd).expanduser().resolve(strict=False)

    paths = collect_paths_from_event(data, root)
    if not paths and can_use_git_fallback(data):
        paths = collect_git_fallback(root)

    if not paths:
        return 0

    return format_paths(paths, root)


if __name__ == "__main__":
    raise SystemExit(main())
