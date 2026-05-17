# W.S.S Wiki

> 暖源社（W.S.S）知识库 —— 心理健康与多意识体系统（MPS）中文百科

[![MkDocs](https://img.shields.io/badge/MkDocs-1.5%2B-blue?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material](https://img.shields.io/badge/Material%20Theme-9.5%2B-purple?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**网站地址:** [wiki.51320721.xyz](https://wiki.51320721.xyz)

---

## 关于本项目

W.S.S Wiki 是由「彼岸」QQ 社区（GES / W.S.S 矩阵）维护的心理健康知识库，内容主要来源于 [MPS Wiki](https://wiki.mpsteam.cn/)（中文多意识体系统百科），涵盖心理疾病、解离障碍（DID/OSDD）、创伤与疗愈、多意识体系统（MPS）等主题。

我们致力于提供一个开放、包容、无评判的心理健康知识平台，让每一位到访者都能安心学习与成长。

---

## 功能特性

-   **8 大主题导览** —— 核心概念、临床诊断、系统运作、实践指南、创伤疗愈、角色身份、理论分类、文化表现
-   **交互式心理量表** —— SDS、SAS、SCL-90、DES-II、MID-60、SDQ-20、GAD-7、PHQ-9 等在线筛查工具
-   **全站搜索** —— 支持中英文搜索建议与高亮
-   **博客系统** —— 内置博客功能
-   **数学公式** —— KaTeX 渲染数学公式
-   **Mermaid 图表** —— 支持 Mermaid 流程图
-   **图片放大** —— glightbox 点击放大浏览
-   **明暗主题** —— 浅色 / 深色 / 跟随系统三种模式

---

## 技术栈

| 类别 | 技术 |
|------|------|
| 静态网站生成器 | [MkDocs](https://www.mkdocs.org/) |
| 主题 | [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) |
| Markdown 扩展 | [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/) |
| 数学渲染 | [KaTeX](https://katex.org/) |
| 图表 | [Mermaid](https://mermaid.js.org/) |
| 交互量表 | 原生 CSS + JavaScript |
| 部署 | Cloudflare Pages |

---

## 快速开始

### 环境要求

-   Python 3.11+

### 安装

```bash
# 克隆仓库
git clone https://github.com/CHINAGUOGE/W.S.S-Wiki.git
cd W.S.S-Wiki

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate   # Linux / macOS
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 本地预览

```bash
mkdocs serve
```

浏览器访问 `http://127.0.0.1:8000`，修改文档后自动刷新。

### 构建

```bash
mkdocs build
```

静态站点输出到 `site/` 目录。

---

## 项目结构

```
W.S.S-Wiki/
├── mkdocs.yml              # MkDocs 主配置（站点、主题、插件、扩展）
├── requirements.txt        # Python 依赖
├── overrides/              # Material 主题自定义覆盖
│   └── partials/
│       └── copyright.html  # 自定义页脚
├── docs/                   # 📚 文档源目录
│   ├── index.md            # 首页
│   ├── guides/             # 8 大主题导览页面
│   ├── 心理相关/           # 心理学条目（~344 篇）
│   │   └── 文献与资料/     # 心理资源文档与 PDF
│   ├── 系统/               # 多元系统简介页面
│   ├── 群友/               # 社区成员页面
│   ├── 帮助/               # 帮助页面
│   ├── blog/               # 博客文章
│   ├── assets/             # 图片、CSS、JS（量表等）
│   └── stylesheets/        # 自定义样式
│       └── extra.css       # 黑幕/剧透文本等效果
├── tools/                  # 🛠 内容管理工具
│   ├── build_partitions_cn.py  # 生成主题分区索引页
│   ├── check_tags.py           # 标签规范检查
│   ├── check_links.py          # 内部链接检查
│   ├── generate_seo_urls.py    # SEO URL 生成
│   ├── gen-validation-report.py# 条目结构验证
│   ├── gen_changelog_by_tags.py# 变更日志生成
│   └── pdf_word.py             # PDF/Word 转 Markdown
└── github action/          # 旧 CI/CD 工作流（已弃用）
```

---

## 工具脚本

```bash
# 标签规范检查（Tagging Standard v2.0）
python tools/check_tags.py docs/心理相关/

# 内部链接格式检查
python tools/check_links.py

# 生成主题分区索引页
python tools/build_partitions_cn.py

# 生成 SEO 高优先级 URL 列表
python tools/generate_seo_urls.py

# 生成变更日志
python tools/gen_changelog_by_tags.py

# PDF/Word 文档转 Markdown
python tools/pdf_word.py

# 批量添加版权声明
python add_copyright.py
```

---

## 贡献

欢迎提交 Issue 和 Pull Request。

**约定：**
- 内容条目使用 YAML frontmatter 标注 `topic` 和 `tags`（遵循 Tagging Standard v2.0）
- 内部链接使用相对路径
- 提交信息使用 Conventional Commits 风格

---

## 友情链接

-   [中文多意识体系统百科 (MPS Wiki)](https://wiki.mpsteam.cn/)
-   [Material for MkDocs 文档](https://squidfunk.github.io/mkdocs-material/)

---

## 许可证

本项目采用 [MIT License](LICENSE)。

---

<p align="center">
  <i>「我们一起向前走」—— 与你温暖相伴</i>
</p>
