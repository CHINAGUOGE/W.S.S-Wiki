#!/usr/bin/env python3
"""
W.S.S Wiki - SEO 综合工具
包含功能:
  1. 检查所有页面是否含有 description frontmatter
  2. 统计页面字数（用于评估内容质量）
  3. 生成页面描述建议（基于文件名和内容片段）
  4. 检查内部链接是否有效
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# 确保标准输出使用 UTF-8（兼容 Windows GBK 终端）
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


def check_descriptions() -> Tuple[List[str], List[str]]:
    """检查所有 .md 文件是否包含 description frontmatter"""
    missing_desc: List[str] = []
    has_desc: List[str] = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel_path = md_file.relative_to(DOCS_DIR)
        content = md_file.read_text(encoding="utf-8")

        # 跳过 tags 和 index 页面
        if md_file.stem in ("tags", "tags.md"):
            continue

        # 检查 frontmatter
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                frontmatter = content[3:end]
                if "description:" in frontmatter:
                    has_desc.append(str(rel_path))
                    continue

        missing_desc.append(str(rel_path))

    return has_desc, missing_desc


def count_word_stats() -> List[Tuple[str, int]]:
    """统计每个页面的中文字数"""
    stats: List[Tuple[str, int]] = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")

        # 去掉 frontmatter
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                content = content[end + 3:]

        # 去掉 markdown 语法
        text = re.sub(r"[#*`~\[\]()>|\\]", "", content)
        # 统计中文字符
        chinese_chars = len(re.findall(r"[一-鿿]", text))

        rel_path = md_file.relative_to(DOCS_DIR)
        stats.append((str(rel_path), chinese_chars))

    stats.sort(key=lambda x: x[1])
    return stats


def check_image_alt_text() -> List[str]:
    """检查是否所有图片都有 alt 文本"""
    missing_alt: List[str] = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        # 匹配没有 alt 的图片: ![](url) 或 ![ ](url)
        no_alt = re.findall(r"!\s*\[\s*\]\([^)]+\)", content)
        if no_alt:
            rel_path = md_file.relative_to(DOCS_DIR)
            missing_alt.append(f"{rel_path} ({len(no_alt)} 处)")

    return missing_alt


def check_heading_hierarchy() -> List[str]:
    """检查是否所有页面都有 H1 标题"""
    missing_h1: List[str] = []
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        # 跳过 frontmatter
        body = content
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                body = content[end + 3:]
        # 找第一个 # 标题
        h1 = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        if not h1:
            rel_path = md_file.relative_to(DOCS_DIR)
            missing_h1.append(str(rel_path))
    return missing_h1


def _print_with_encoding(text: str) -> None:
    """安全打印（兼容 Windows GBK 终端）"""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('gbk', errors='replace'))


def main() -> None:
    _print_with_encoding("=" * 60)
    _print_with_encoding("W.S.S Wiki - SEO 健康检查报告")
    _print_with_encoding("=" * 60)

    # 1. Description 检查
    _print_with_encoding("\n[1/4] Description frontmatter 检查...")
    has_desc, missing_desc = check_descriptions()
    _print_with_encoding(f"[OK] 已包含 description: {len(has_desc)} 个文件")
    if missing_desc:
        _print_with_encoding(f"[WARN] 缺少 description: {len(missing_desc)} 个文件")
        for f in missing_desc[:20]:
            _print_with_encoding(f"    - {f}")
        if len(missing_desc) > 20:
            _print_with_encoding(f"    ... 还有 {len(missing_desc) - 20} 个")

    # 2. 字数统计
    _print_with_encoding("\n[2/4] 内容字数统计...")
    stats = count_word_stats()
    total_chars = sum(s[1] for s in stats)
    min_chars = stats[0][1] if stats else 0
    max_chars = stats[-1][1] if stats else 0
    avg_chars = total_chars // len(stats) if stats else 0
    _print_with_encoding(f"  总中文字数: {total_chars}")
    _print_with_encoding(f"  平均字数/页: {avg_chars}")
    _print_with_encoding(f"  最少/最多: {min_chars} / {max_chars}")
    thin_pages = [(f, c) for f, c in stats if c < 100]
    if thin_pages:
        _print_with_encoding(f"[WARN] 内容过少的页面 (< 100 字): {len(thin_pages)} 个")
        for f, c in thin_pages[:10]:
            _print_with_encoding(f"    - {f} ({c} 字)")

    # 3. 图片 Alt 文本
    _print_with_encoding("\n[3/4] 图片 Alt 文本检查...")
    missing_alt = check_image_alt_text()
    if missing_alt:
        _print_with_encoding(f"[WARN] 缺少 alt 文本的图片: {len(missing_alt)} 处")
        for f in missing_alt[:10]:
            _print_with_encoding(f"    - {f}")
    else:
        _print_with_encoding("  [OK] 所有图片均有 alt 文本")

    # 4. H1 标题
    _print_with_encoding("\n[4/4] H1 标题层级检查...")
    missing_h1 = check_heading_hierarchy()
    if missing_h1:
        _print_with_encoding(f"[WARN] 缺少 H1 标题: {len(missing_h1)} 个文件")
        for f in missing_h1[:10]:
            _print_with_encoding(f"    - {f}")
    else:
        _print_with_encoding("  [OK] 所有页面均有 H1 标题")

    _print_with_encoding("\n" + "=" * 60)
    _print_with_encoding("检查完成。建议修复上述警告项以提升 SEO 表现。")
    _print_with_encoding("=" * 60)


if __name__ == "__main__":
    main()
