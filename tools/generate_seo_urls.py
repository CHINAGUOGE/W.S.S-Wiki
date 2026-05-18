#!/usr/bin/env python3
"""
生成高权重 URL 列表用于 SEO 提交，以及 sitemap.xml 补充文件。

功能:
  1. 生成 seo_priority_urls.txt — 带优先级的 URL 清单，用于手动提交
  2. 生成 sitemap_extra.xml — 给 MkDocs 内置 sitemap 插件补充的 URL（如 blog 分页等）

基于搜索词频权重和页面重要性生成优先级 URL。
根据站点实际结构动态扫描 docs/ 目录，避免硬编码不存在的页面。
"""

import datetime
from pathlib import Path
from typing import List, Tuple

# 确保标准输出使用 UTF-8（兼容 Windows GBK 终端）
import sys
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# 网站基础 URL
BASE_URL = "https://wiki.51320721.xyz"

# 项目 doc 根目录（本脚本所在 ../docs/）
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

# ── 核心导览页面（优先级 1，changefreq: weekly）──
CORE_GUIDES: List[Tuple[str, str, str]] = [
    ("",                                  "Wiki 首页",                     "always"),
    ("心理相关/QuickStart",                "快速开始",                       "weekly"),
    ("guides/index",                      "核心主题导览总页",                "weekly"),
    ("guides/Core-Concepts-Guide",        "核心概念导览",                   "weekly"),
    ("guides/Mental-Health-Guide",        "心理健康导览",                   "weekly"),
    ("guides/Clinical-Diagnosis-Guide",   "诊断与临床导览",                 "weekly"),
    ("guides/System-Operations-Guide",    "系统运作导览",                   "weekly"),
    ("guides/Practice-Guide",             "实践指南导览",                   "weekly"),
    ("guides/Trauma-Healing-Guide",       "创伤与疗愈导览",                 "weekly"),
    ("guides/Roles-Identity-Guide",       "角色与身份导览",                 "weekly"),
    ("guides/Theory-Classification-Guide", "理论与分类导览",                "weekly"),
    ("guides/Cultural-Media-Guide",       "文化与表现导览",                 "weekly"),
]

# ── 关键词典与工具页面（优先级 1）──
TOOL_PAGES: List[Tuple[str, str, str]] = [
    ("心理相关/tags",     "标签索引",       "daily"),
    ("心理相关/Glossary", "术语词典",        "weekly"),
]

# ── 主题分区索引页面（优先级 2）──
PARTITION_INDEXES: List[Tuple[str, str, str]] = [
    ("guides/Clinical-Diagnosis-index",   "诊断与临床主题分区",     "weekly"),
    ("guides/System-Operations-index",    "系统运作主题分区",       "weekly"),
    ("guides/Practice-index",             "实践指南主题分区",       "weekly"),
    ("guides/Trauma-Healing-index",       "创伤与疗愈主题分区",     "weekly"),
    ("guides/Roles-Identity-index",       "角色与身份主题分区",     "weekly"),
    ("guides/Theory-Classification-index", "理论与分类主题分区",    "weekly"),
    ("guides/Cultural-Media-index",       "文化与表现主题分区",     "weekly"),
]

# ── 高优先级词条 slug（优先级 2）──
PRIORITY_ENTRIES = [
    # ===== 核心诊断 =====
    "DID", "OSDD", "PTSD", "CPTSD",
    "Dissociative-Disorders", "Anxiety-Disorders", "Depressive-Disorders",
    "Borderline-Personality-Disorder-BPD", "Narcissistic-Personality-Disorder-NPD",
    "Generalized-Anxiety-Disorder-GAD", "Social-Anxiety-Disorder", "Panic-Disorder",
    "OCD", "Schizophrenia-SZ", "Bipolar-Disorders", "Eating-Disorders-ED",
    "Autism-Spectrum-Disorder", "Attention-Deficit-Hyperactivity-Disorder-ADHD",
    "Substance-Use-Disorders-SUD", "Depersonalization-Derealization-Disorder-DPDR",

    # ===== 解离与创伤核心概念 =====
    "Dissociation", "Trauma", "Multiple_Personality_System",
    "Structural-Dissociation-Theory", "Functional-Dissociation",
    "Dissociative-Amnesia-DA", "Emmengard-Classification",
    "C-PTSD-Coping-Styles", "Window-of-Tolerance", "Flashback", "Grounding", "Trigger",

    # ===== 系统运作核心 =====
    "System", "Alter", "Host", "Switch", "Front-Fronting", "Co-Fronting",
    "Co-Consciousness", "Internal-Communication", "Headspace-Inner-World",
    "Blending", "Front-Blur", "Frontstuck", "Fusion", "Integration",
    "Memory-Shielding", "Passive-Influence", "Subsystem", "Exomemory", "System-Roles",

    # ===== 核心角色 =====
    "Protector", "Gatekeeper", "Caregiver", "Persecutor", "Fragment",
    "Child-Alter", "Adult-Alter", "Trauma-Holder", "Memory-Holder",
    "Introject", "Internal-Self-Helper-ISH", "Soulbond",

    # ===== 常用疗法 =====
    "Cognitive-Behavioral-Therapy-CBT", "Dialectical-Behavior-Therapy-DBT",
    "Eye-Movement-Desensitization-Reprocessing-EMDR", "Internal-Family-Systems-IFS",
    "Cognitive-Processing-Therapy-CPT", "Acceptance-Commitment-Therapy-ACT",
    "Somatic-Experiencing-SE", "Three-Phase-Trauma-Treatment",
    "Phase-Oriented-Treatment-Principles", "Cranial-Electrotherapy-Stimulation-CES",

    # ===== 交互式量表工具 =====
    "Self-Rating-Depression-Scale-SDS", "Self-Rating-Anxiety-Scale-SAS",
    "Symptom-Checklist-90-SCL-90", "Dissociative-Experiences-Scale-DES-II",
    "Multidimensional-Inventory-of-Dissociation-MID-60",
    "Somatoform-Dissociation-Questionnaire-SDQ-20",
    "Generalized-Anxiety-Disorder-7-GAD-7", "Patient-Health-Questionnaire-9-PHQ-9",
    "DSM-5TR-Scales",

    # ===== 社区高频概念 =====
    "Tulpa", "Tulpa-Guide-0", "Tulpa-Guide-1", "Tulpa-Guide-2", "Tulpa-Guide-3",
    "Forcing", "Vocality", "Wonderland", "Parroting-Puppeting", "Tulpish", "Alterhuman",
]

# ── 固定目录页面（优先级 3）──
SECONDARY_SECTIONS: List[Tuple[str, str, str, str]] = [
    # (相对路径, 输出描述, docs 子目录, changefreq)
    ("blog/",                    "博客首页",          "blog",      "daily"),
    ("帮助/关于W.S.S",           "关于暖源社",         "帮助",      "monthly"),
    ("帮助/markdown语法教程",     "Markdown 语法教程",  "帮助",      "monthly"),
    ("心理相关/文献与资料/index", "文献与资料总页",     "心理相关/文献与资料", "weekly"),
]

# ── 忽略的目录 / 文件模式──
IGNORE_DIRS = {
    "__pycache__", ".git", "node_modules", "site", "venv",
    "assets", "stylesheets",
}


def _collect_files_under(rel_dir: str, exclude_patterns: set | None = None) -> List[str]:
    """扫描 docs/{rel_dir} 下所有 .md 文件，返回 slug 列表（不含扩展名）。"""
    if exclude_patterns is None:
        exclude_patterns = {"index", "tags", "Glossary", "QuickStart"}
    target = DOCS_DIR / rel_dir
    if not target.is_dir():
        return []
    slugs: List[str] = []
    for f in sorted(target.iterdir()):
        if f.suffix != ".md":
            continue
        stem = f.stem
        if stem in exclude_patterns:
            continue
        slugs.append(stem)
    return slugs


def generate_url_list() -> List[Tuple[int, str, str, str]]:
    """
    生成带优先级的 URL 列表
    返回: [(优先级, URL, 描述, changefreq)]
    优先级: 1=最高, 5=最低
    """
    urls: List[Tuple[int, str, str, str]] = []

    # 首页 + 核心导览（优先级 1）
    for path, desc, freq in CORE_GUIDES:
        url = f"{BASE_URL}/{path}" if path else BASE_URL
        urls.append((1, url, desc, freq))

    # 关键词典与工具页（优先级 1）
    for path, desc, freq in TOOL_PAGES:
        urls.append((1, f"{BASE_URL}/{path}", desc, freq))

    # 主题分区索引（优先级 2）
    for path, desc, freq in PARTITION_INDEXES:
        urls.append((2, f"{BASE_URL}/{path}", desc, freq))

    # 高优先级词条（优先级 2）
    for entry in PRIORITY_ENTRIES:
        urls.append((2, f"{BASE_URL}/心理相关/{entry}", f"词条: {entry}", "monthly"))

    # 二级目录页面（优先级 3）
    for path, desc, _subdir, freq in SECONDARY_SECTIONS:
        urls.append((3, f"{BASE_URL}/{path}", desc, freq))

    # 动态扫描 docs/系统/ 和 docs/群友/
    for sub in ("系统", "群友"):
        slugs = _collect_files_under(sub)
        for slug in slugs:
            urls.append((3, f"{BASE_URL}/{sub}/{slug}", f"{sub}/{slug}", "monthly"))

    # 动态扫描 docs/心理相关/ 补充词条（优先级 4）
    manual_slugs: set = set()
    for entry in PRIORITY_ENTRIES:
        manual_slugs.add(entry)
    manual_slugs.update({"index", "tags", "Glossary", "QuickStart"})

    for slug in _collect_files_under("心理相关"):
        if slug in manual_slugs:
            continue
        urls.append((4, f"{BASE_URL}/心理相关/{slug}", f"词条: {slug}", "monthly"))

    return urls


def generate_sitemap_xml(urls: List[Tuple[int, str, str, str]]) -> str:
    """
    生成 sitemap XML 片段（用于补充 MkDocs 内置 sitemap）。
    如果 mkdocs-sitemap 插件已自动生成完整 sitemap，此文件可忽略。
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    priority_map = {1: "1.0", 2: "0.8", 3: "0.6", 4: "0.4", 5: "0.3"}

    lines: List[str] = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for priority, url, desc, changefreq in sorted(urls, key=lambda x: (x[0], x[1])):
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority_map.get(priority, '0.5')}</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    return "\n".join(lines)


def format_url_list(urls: List[Tuple[int, str, str, str]]) -> str:
    """格式化 URL 列表为可读文本"""
    output: List[str] = []
    output.append("=" * 80)
    output.append("W.S.S Wiki - SEO 高权重 URL 清单")
    output.append(f"网站地址: {BASE_URL}")
    output.append(f"生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("=" * 80)
    output.append("")

    current_priority: int | None = None
    for priority, url, desc, _freq in urls:
        if priority != current_priority:
            current_priority = priority
            priority_label = {
                1: "最高优先级 - 核心页面与工具",
                2: "高优先级 - 主题分区与核心词条",
                3: "中等优先级 - 二级页面与补充词条",
                4: "普通优先级 - 全部心理相关词条",
                5: "低优先级 - 补充内容",
            }
            output.append("")
            output.append(f"{'─' * 80}")
            output.append(f"【优先级 {priority}】{priority_label.get(priority, '其他')}")
            output.append(f"{'─' * 80}")
            output.append("")
        output.append(f"{url}  # {desc}")

    output.append("")
    output.append("=" * 80)
    output.append(f"总计: {len(urls)} 个 URL")
    output.append("")
    output.append("使用建议:")
    output.append("1. 优先提交「优先级 1」的 URL 到搜索引擎")
    output.append("2. 定期更新「优先级 2」的词条内容")
    output.append("3. 使用 Google Search Console / Bing Webmaster Tools 批量提交")
    output.append("4. 部署后 sitemap.xml 由 MkDocs sitemap 插件自动生成")
    output.append("5. 使用 tools/google_indexing_api.py 提交重要页面更新")
    output.append("6. 运行 tools/seo_health_check.py 检查 SEO 健康度")
    output.append("=" * 80)

    return "\n".join(output)


def main() -> None:
    urls = generate_url_list()

    # 输出 URL 清单到项目根目录
    output_file = Path(__file__).resolve().parent.parent / "seo_priority_urls.txt"
    output_file.write_text(format_url_list(urls), encoding="utf-8")
    print(f"[OK] 已生成: {output_file.name} ({len(urls)} 个 URL)")

    # 输出 sitemap 补充文件
    sitemap_xml = generate_sitemap_xml(urls)
    sitemap_file = Path(__file__).resolve().parent.parent / "sitemap_extra.xml"
    sitemap_file.write_text(sitemap_xml, encoding="utf-8")
    print(f"[OK] 已生成: {sitemap_file.name}")

    print("\n" + format_url_list(urls))


if __name__ == "__main__":
    main()
