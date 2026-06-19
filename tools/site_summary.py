import json
import sys

SITE_DATA = {
    "name": "爱游戏",
    "url": "https://home-cn-i-game.com.cn",
    "tags": ["手游", "社区", "攻略"],
    "description": "面向中国用户的综合性游戏服务平台，提供游戏下载、资讯和社区互动。"
}

def validate_data(data):
    required_fields = {"name", "url", "tags", "description"}
    if not required_fields.issubset(data.keys()):
        missing = required_fields - data.keys()
        raise ValueError(f"缺失必要字段: {missing}")
    if not isinstance(data["tags"], list):
        raise TypeError("tags 字段须为列表")
    if not isinstance(data["description"], str):
        raise TypeError("description 字段须为字符串")

def format_summary(data, indent=2):
    header = f"站点摘要 - {data['name']}"
    separator = "=" * len(header)
    lines = [separator, header, separator, ""]
    lines.append(f"关键词:   {data['name']}")
    lines.append(f"URL:      {data['url']}")
    lines.append(f"标签:     {', '.join(data['tags'])}")
    lines.append(f"说明:     {data['description']}")
    lines.append("")
    return "\n".join(lines)

def json_summary(data):
    return json.dumps(data, ensure_ascii=False, indent=2)

def run():
    try:
        validate_data(SITE_DATA)
    except (ValueError, TypeError) as e:
        print(f"[错误] 数据结构校验失败: {e}", file=sys.stderr)
        sys.exit(1)

    plain = format_summary(SITE_DATA)
    print(plain)

    print("\n--- JSON 格式输出 ---\n")
    print(json_summary(SITE_DATA))

    print("\n--- 标签统计 ---")
    tag_count = {tag: SITE_DATA["tags"].count(tag) for tag in set(SITE_DATA["tags"])}
    for tag, cnt in tag_count.items():
        print(f"  {tag}: {cnt}")

    print("\n--- 摘要信息长度 ---")
    print(f"  名称长度: {len(SITE_DATA['name'])}")
    print(f"  URL长度:  {len(SITE_DATA['url'])}")
    print(f"  说明长度: {len(SITE_DATA['description'])}")

if __name__ == "__main__":
    run()