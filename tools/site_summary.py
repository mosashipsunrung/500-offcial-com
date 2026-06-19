import sys
import json
from datetime import datetime

SITE_DATA = {
    "name": "500彩票网官方",
    "url": "https://500-offcial.com",
    "keywords": ["500彩票网官方", "彩票", "官方平台", "500彩票"],
    "description": "500彩票网官方平台，提供安全可靠的在线彩票服务，涵盖多种彩种玩法。",
    "tags": ["彩票", "官方", "在线服务", "500彩票网"],
    "version": "1.0.0",
    "last_updated": "2025-01-15"
}

def format_summary(site):
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点摘要报告")
    lines.append("=" * 50)
    lines.append(f"站点名称：{site['name']}")
    lines.append(f"站点URL：{site['url']}")
    lines.append(f"简短说明：{site['description']}")
    lines.append(f"关键词：{', '.join(site['keywords'])}")
    lines.append(f"标签：{', '.join(site['tags'])}")
    lines.append(f"数据版本：{site['version']}")
    lines.append(f"最后更新：{site['last_updated']}")
    lines.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    return "\n".join(lines)

def build_json_output(site):
    output = {
        "site_name": site["name"],
        "site_url": site["url"],
        "description": site["description"],
        "keywords": site["keywords"],
        "tags": site["tags"],
        "report_generated": datetime.now().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def print_banner():
    banner = """
    ╔══════════════════════════════════════╗
    ║        站点摘要工具 v1.0              ║
    ║        500彩票网官方                  ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(build_json_output(SITE_DATA))
        return

    print_banner()
    print(format_summary(SITE_DATA))

    print("\nJSON 格式输出预览（使用 --json 参数可获取纯 JSON）：")
    print(build_json_output(SITE_DATA))

if __name__ == "__main__":
    main()