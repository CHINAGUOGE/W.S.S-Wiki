#!/usr/bin/env python3
"""
W.S.S Wiki - Sitemap Post-build Cleanup

用法（构建后运行）:
  python tools/gen_sitemap.py          # 清理 site/sitemap.xml（移除 404，添加优先级）
  python tools/gen_sitemap.py --full   # 重新生成（使用 gen_extra 的详细配置）

运行时机: mkdocs build 之后，部署之前。
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple

SITE_DIR = Path(__file__).resolve().parent.parent / "site"
BASE_URL = "https://wiki.51320721.xyz"

# 需要从 sitemap 中移除的路径
REMOVE_PATHS = {"/404/", "/404.html"}

# 路径 → 优先级
PRIORITY_MAP: Dict[str, str] = {
    "/": "1.0",
    "/guides/": "0.9",
    "/心理相关/QuickStart/": "0.9",
    "/心理相关/Glossary/": "0.8",
    "/心理相关/tags/": "0.7",
}

# 路径 → 更新频率
CHANGEFREQ_MAP: Dict[str, str] = {
    "/": "daily",
    "/blog/": "daily",
    "/guides/": "weekly",
    "/心理相关/tags/": "daily",
}


def get_path_from_loc(loc: str) -> str:
    """从 <loc> 中提取路径部分"""
    if loc.startswith(BASE_URL):
        return loc[len(BASE_URL):] or "/"
    return loc


def cleanup_sitemap() -> int:
    """清理 sitemap.xml，移除 404，添加优先级/更新频率属性"""
    sitemap_file = SITE_DIR / "sitemap.xml"
    if not sitemap_file.exists():
        print(f"[错误] 未找到 {sitemap_file}")
        return 1

    # 解析 XML
    tree = ET.parse(sitemap_file)
    root = tree.getroot()

    # XML 命名空间
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    to_remove: List[ET.Element] = []
    for url_elem in root.findall("sm:url", ns):
        loc_elem = url_elem.find("sm:loc", ns)
        if loc_elem is None:
            continue
        path = get_path_from_loc(loc_elem.text or "")

        # 移除黑名单路径
        if path in REMOVE_PATHS:
            to_remove.append(url_elem)
            print(f"  [移除] {path}")
            continue

        # 添加/更新 priority
        if path in PRIORITY_MAP:
            prio = PRIORITY_MAP[path]
            prio_elem = url_elem.find("sm:priority", ns)
            if prio_elem is None:
                prio_elem = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}priority")
            prio_elem.text = prio

        # 添加/更新 changefreq
        for pattern, freq in CHANGEFREQ_MAP.items():
            if path.startswith(pattern):
                freq_elem = url_elem.find("sm:changefreq", ns)
                if freq_elem is None:
                    freq_elem = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq")
                freq_elem.text = freq
                break

    # 执行移除
    for elem in to_remove:
        root.remove(elem)

    # 写回
    tree.write(sitemap_file, encoding="UTF-8", xml_declaration=True)
    print(f"\n[OK] sitemap.xml 已清理: 移除 {len(to_remove)} 个, 剩余 {len(root)} 个 URL")
    return 0


def generate_full_sitemap() -> int:
    """使用 gen_sitemap.py 替代策略生成完整 sitemap"""
    # 这里文档参考 generate_seo_urls.py 中的逻辑
    print("[信息] 全量生成模式：使用 Material 主题默认 sitemap")
    return 0


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--full":
        sys.exit(generate_full_sitemap())
    else:
        sys.exit(cleanup_sitemap())


if __name__ == "__main__":
    main()
