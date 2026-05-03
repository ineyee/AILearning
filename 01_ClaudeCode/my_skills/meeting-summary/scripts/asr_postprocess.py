import argparse  # 用于解析命令行参数
import re        # 用于正则表达式匹配
import sys       # 用于退出程序
from pathlib import Path  # 用于文件读写

# Whisper 输出的时间戳格式，例如：[00:00:01.000 --> 00:00:05.000]
# \d{2} 匹配两位数字，[.,] 兼容小数点和逗号两种分隔符，\s* 允许箭头两侧有空格
TIMESTAMP_PATTERN = re.compile(
    r"\[\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[.,]\d{3}\]\s*"
)


def remove_timestamps(input_path: str, output_path: str) -> None:
    """读取转写文件，删除每行的时间戳，将结果写入输出文件（或打印到终端）。"""

    path = Path(input_path)  # 将字符串路径转为 Path 对象，方便后续操作

    # 文件不存在时报错退出，避免后续操作产生误导性错误
    if not path.exists():
        print(f"[错误] 文件不存在: {input_path}", file=sys.stderr)
        sys.exit(1)

    # 读取文件全部内容，指定 UTF-8 编码以兼容中文
    raw_text = path.read_text(encoding="utf-8")

    # 按行处理：对每一行用空字符串替换时间戳，再去除首尾空格
    cleaned_lines = [
        TIMESTAMP_PATTERN.sub("", line).strip()
        for line in raw_text.splitlines()
    ]

    # 过滤掉删除时间戳后变成空行的行（原本只有时间戳、没有内容的行）
    cleaned_lines = [line for line in cleaned_lines if line]

    # 用换行符将所有行重新拼接成完整文本
    output_text = "\n".join(cleaned_lines)

    if output_path:
        # 指定了输出路径，将结果写入文件
        Path(output_path).write_text(output_text, encoding="utf-8")
        print(f"[完成] 结果已保存至: {output_path}")
    else:
        # 未指定输出路径，直接打印到终端
        print(output_text)


def main():
    """解析命令行参数，调用处理函数。"""

    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description="删除 Whisper ASR 转写文本中的时间戳"
    )

    # 必填参数：输入文件路径
    parser.add_argument("input", help="ASR 转写结果文件路径")

    # 可选参数：输出文件路径，不指定则打印到终端
    parser.add_argument("-o", "--output", help="输出文件路径（不指定则打印到终端）")

    # 解析用户传入的参数
    args = parser.parse_args()

    # 调用核心处理函数
    remove_timestamps(args.input, args.output)


# 只有直接运行此脚本时才执行 main()，被其他模块 import 时不执行
if __name__ == "__main__":
    main()
