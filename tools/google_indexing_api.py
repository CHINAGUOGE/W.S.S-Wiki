#!/usr/bin/env python3
"""
W.S.S Wiki - Google Indexing API 批量提交脚本

使用 Google Indexing API 通知搜索引擎收录/更新页面。
适用于部署后通知 Google 尽快抓取更新的页面。

前置条件:
  1. 在 Google Search Console 验证站点所有权
  2. 在 Google Cloud Console 启用 Indexing API 并创建服务账号
  3. 下载服务账号 JSON 密钥并保存到项目根目录或安全位置

用法:
  python tools/google_indexing_api.py                          # 提交 seo_priority_urls.txt 中所有优先级 1 & 2 的 URL
  python tools/google_indexing_api.py --url https://...        # 提交单个 URL
  python tools/google_indexing_api.py --file urls.txt          # 从文件中读取 URL 列表
  python tools/google_indexing_api.py --priority 1 2           # 提交指定优先级的 URL

环境变量:
  GOOGLE_APPLICATION_CREDENTIALS: 服务账号 JSON 密钥路径
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Tuple

# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_priority_urls(priorities: List[int] | None = None) -> List[str]:
    """从 seo_priority_urls.txt 中提取 URL 列表"""
    url_file = PROJECT_ROOT / "seo_priority_urls.txt"
    if not url_file.exists():
        print(f"[错误] 未找到 {url_file}，请先运行 generate_seo_urls.py")
        return []

    urls: List[str] = []
    current_priority = 0
    priority_map = {"最高": 1, "高": 2, "中等": 3, "普通": 4}

    with open(url_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 检测优先级标题
            for key, val in priority_map.items():
                if f"【优先级 {val}】" in line and key in line:
                    current_priority = val
                    break
            # 提取 URL
            if line.startswith("https://") and not line.startswith("https://unpkg"):
                url = line.split()[0].rstrip("#")
                if priorities is None or current_priority in priorities:
                    urls.append(url)

    return urls


def submit_via_api(urls: List[str], credentials_path: str | None = None) -> None:
    """使用 Google Indexing API 提交 URL"""
    try:
        from google.auth import default
        from google.auth.transport.requests import Request
        from google.oauth2 import service_account
        import googleapiclient.discovery
    except ImportError:
        print("[错误] 缺少依赖：请安装 google-auth 和 google-api-python-client")
        print("  pip install google-auth google-api-python-client")
        sys.exit(1)

    if not urls:
        print("[跳过] 没有需要提交的 URL")
        return

    # 认证
    if credentials_path:
        creds = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/indexing"],
        )
    else:
        creds, _ = default(
            scopes=["https://www.googleapis.com/auth/indexing"]
        )

    # 创建服务
    service = googleapiclient.discovery.build("indexing", "v3", credentials=creds)

    # 批量提交
    success = 0
    failed = 0
    for url in urls:
        body = {"url": url, "type": "URL_UPDATED"}
        try:
            service.urlNotifications().publish(body=body).execute()
            print(f"  ✓ {url}")
            success += 1
        except Exception as e:
            print(f"  ✗ {url} → {e}")
            failed += 1

    print(f"\n提交完成: {success} 成功, {failed} 失败 / 共 {len(urls)} 个")


def main() -> None:
    parser = argparse.ArgumentParser(description="Google Indexing API 批量提交")
    parser.add_argument("--url", help="提交单个 URL")
    parser.add_argument("--file", help="从文件读取 URL 列表")
    parser.add_argument("--priority", nargs="*", type=int,
                        help="提交指定优先级的 URL（如 1 2 表示优先级 1 和 2）")
    parser.add_argument("--credentials",
                        default=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
                        help="服务账号 JSON 密钥路径")
    args = parser.parse_args()

    urls: List[str] = []
    if args.url:
        urls = [args.url]
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip().startswith("https://")]
    else:
        priorities = args.priority if args.priority else [1, 2]
        urls = load_priority_urls(priorities)

    if not urls:
        print("没有找到要提交的 URL。")
        sys.exit(0)

    print(f"准备提交 {len(urls)} 个 URL 到 Google Indexing API...\n")
    submit_via_api(urls, args.credentials)


if __name__ == "__main__":
    main()
