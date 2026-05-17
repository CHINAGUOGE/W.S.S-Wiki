import os
import sys
from pathlib import Path

# ==================== 配置区域 ====================
# 1. 你的 docs 文件夹路径
DOCS_DIR = "./docs/心理相关"

# 2. 标准的版权信息格式（严格保留 Markdown 缩进与换行）
# 在 Windows 下统一使用标准 \n，Python 在写入时会自动根据系统或标准转换
COPYRIGHT_TEXT = (
    "\n\n---\n\n"
    '!!! tip "版权说明"\n'
    "    本内容来源于Multiple Personality System Wiki - 多意识体系统百科，MPS Team版权所有。"
)
# ==================================================


def add_copyright_to_md():
    # 确保当前使用的是虚拟环境的 Python，打印出来以便核对
    print(f"当前 Python 解释器位置: {sys.executable}")

    docs_path = Path(DOCS_DIR)
    if not docs_path.exists():
        print(f"❌ 找不到配置的 docs 目录: {DOCS_DIR}")
        return

    processed_count = 0
    skipped_count = 0
    file_count = 0

    print("🚀 开始在 Windows 环境下批量检查并添加版权信息...\n")

    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                file_count += 1
                file_path = Path(root) / file

                # 显式指定 encoding='utf-8' 防止 Windows 默认使用 GBK 导致读取报错或乱码
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    print(
                        f"⚠️  文件 {file_path.name} 编码不是标准 UTF-8，正在尝试 utf-8-sig..."
                    )
                    with open(file_path, "r", encoding="utf-8-sig") as f:
                        content = f.read()

                # 安全检测：如果文件中已经包含这段版权说明，则跳过，避免重复追加
                if (
                    '!!! tip "版权说明"' in content
                    and "MPS Team版权所有" in content
                ):
                    skipped_count += 1
                    continue

                # rstrip() 清除文件末尾所有的空白、原换行符
                # 这样可以确保后面拼接的 \n\n---\n\n 是绝对精准的“换行两次+分割线+换行两次”
                clean_content = content.rstrip()

                # 追加版权信息
                new_content = clean_content + COPYRIGHT_TEXT

                # 写回文件，同样强制指定 utf-8
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                processed_count += 1
                print(
                    f"✅ 已成功添加版权: {file_path.relative_to(docs_path)}"
                )

    print(f"\n==== 📊 统计报告 ====")
    print(f"共扫描 Markdown 文件: {file_count} 个")
    print(f"成功追加版权信息: {processed_count} 个")
    print(f"跳过（已存在版权）: {skipped_count} 个")


if __name__ == "__main__":
    add_copyright_to_md()