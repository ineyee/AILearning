# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库简介

这是一个学习仓库，用于记录 Claude Code 的概念和使用方法，由两篇 Markdown 文章和各功能的实战 Demo 子目录组成。

- `第一篇：概念速通.md` — 概念总览（是什么）
- `第二篇：使用指南和实践技巧.md` — 使用指南与实践技巧（怎么用）

## Demo 子目录

每个子目录是某个 Claude Code 功能的独立 Demo：

| 目录 | 演示的功能 |
|---|---|
| `hook_demo/` | Hooks — `PostToolUse` hook，在 Write/Edit 后自动格式化 `.dart` 文件 |
| `mcp_server_demo/` | 在项目中使用 MCP Server |
| `my_mcp_servers/weather-mcp-server/` | 自建 MCP Server（Python + FastMCP，调用 Open-Meteo API） |
| `my_skills/meeting-summary/` | 自建 Skill，含路由逻辑和参考文件 |
| `my_subagents/` | 自建 Subagent（weekly-report-writer） |
| `subagent_demo/` | 使用 Subagent — 含 `startup-analyst` agent |
| `skill_demo/` | 使用 Skill — 含 `huashu-nuwa` 和 `li-meijin-perspective` skill |
| `plugin_demo/` | 使用 Plugin |
| `my-first-plugin/` | 自建 Plugin（打包了 MCP Server + Skill + Agent + Hooks） |
| `my-marketplace/` | 自建 Plugin Marketplace（引用了 `my-first-plugin`） |

## MCP Server 开发

天气 MCP Server（`my_mcp_servers/weather-mcp-server/`）使用 Python + `uv`：

```bash
# 直接运行 MCP Server（用于测试）
cd my_mcp_servers/weather-mcp-server
uv run weather-mcp-server.py
```

Server 使用 `mcp` 包中的 `FastMCP`，工具通过 `@mcpServer.tool()` 注册。函数名、带类型注解的参数以及 docstring 会作为工具的元数据暴露给模型。

## Skill 结构

Skill 放在一个目录下，包含带 frontmatter 的 `SKILL.md`：

```markdown
---
name: skill-name
description: 触发描述，模型根据此决定是否路由到该 Skill。
---
```

在 `SKILL.md` 中用 `@references/filename.md` 语法加载参考文件。

## Subagent / Agent 结构

Agent 文件是带 frontmatter 的 Markdown：

```markdown
---
name: agent-name
description: 何时主动调用该 Agent。
model: sonnet   # 或 inherit
tools: Read, Glob
color: green
---
```

## Plugin 结构

Plugin 目录需要包含 `.claude-plugin/plugin.json`：

```json
{
  "name": "plugin-name",
  "mcpServers": "./.mcp.json",
  "skills": ["./skills/skill-name"],
  "agents": ["./agents/agent-name.md"],
  "hooks": "./hooks/hooks.json"
}
```

Plugin 根目录下的 `.mcp.json` 使用 `${CLAUDE_PLUGIN_ROOT}` 引用相对于 Plugin 目录的路径。

## Hook 模式

Hook 定义在 `.claude/settings.json`（项目级）或 `hooks/hooks.json`（Plugin 级）：

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{ "type": "command", "command": "..." }]
    }]
  }
}
```

`hook_demo` 演示了在任意 Write 或 Edit 工具调用后自动格式化 Dart 文件。
