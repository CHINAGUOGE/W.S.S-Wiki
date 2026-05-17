import os
import sys
from pathlib import Path

# ==================== 配置区域（自动锁定路径版） ====================
# 1. 动态获取当前脚本所在的绝对路径
SCRIPT_DIR = Path(__file__).resolve().parent

# 2. 根据脚本存放的位置，自动锁死 docs 文件夹的绝对路径：
# 如果脚本在项目根目录（与 docs 平级）：
DOCS_DIR = SCRIPT_DIR / "docs"

# 如果脚本在 tools 目录或者 docs 目录下（即 docs 的子目录/平级工具目录）：
# DOCS_DIR = SCRIPT_DIR.parent / "docs"

# 如果脚本就放在 docs/心理相关 目录下：
# DOCS_DIR = SCRIPT_DIR.parent.parent / "docs"

# 为了防错，你可以直接在这里写死你在 Windows 下的绝对路径：
# DOCS_DIR = r"D:\project\wiki\docs"

# 3. 标准的版权信息格式
COPYRIGHT_TEXT = (
    "\n\n---\n\n"
    '!!! tip "版权说明"\n'
    "    本内容来源于Multiple Personality System Wiki - 多意识体系统百科，MPS Team版权所有。"
)
# ==================================================================

def add_copyright_to_md():
    print(f"当前 Python 解释器位置: {sys.executable}")
    
    # 将其转换为 Path 对象
    docs_path = Path(DOCS_DIR)
    print(f"🔍 脚本正在尝试读取的绝对路径为: {docs_path.absolute()}")
    
    if not docs_path.exists():
        print(f"❌ 找不到配置的 docs 目录: {DOCS_DIR}")
        print("💡 提示：请检查脚本中 DOCS_DIR 的配置是否与你脚本放置的实际目录层级匹配。")
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

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(file_path, "r", encoding="utf-8-sig") as f:
                        content = f.read()

                if '!!! tip "版权说明"' in content and "MPS Team版权所有" in content:
                    skipped_count += 1
                    continue

                clean_content = content.rstrip()
                new_content = clean_content + COPYRIGHT_TEXT

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

                processed_count += 1
                print(f"✅ 已成功添加版权: {file_path.relative_to(docs_path)}")

    print(f"\n==== 📊 统计报告 ====")
    print(f"共扫描 Markdown 文件: {file_count} 个")
    print(f"成功追加版权信息: {processed_count} 个")
    print(f"跳过（已存在版权）: {skipped_count} 个")

if __name__ == "__main__":
    add_copyright_to_md()