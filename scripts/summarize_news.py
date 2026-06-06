import json
import re

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

summarized = []

for item in news:

    title = item["title"]

    clean_summary = re.sub(
        '<.*?>',
        '',
        item.get("summary", "")
    )

    clean_summary = clean_summary.strip()

    title_lower = title.lower()

    # =====================================
    # SIMPLE CHINESE SUMMARY
    # =====================================

    chinese_summary = "物流行业出现新的市场动态。"

    if any(word in title_lower for word in [
        "dhl",
        "fedex",
        "ups",
        "express",
        "parcel"
    ]):
        chinese_summary = "国际快递与包裹业务持续扩张。"

    elif any(word in title_lower for word in [
        "air cargo",
        "air freight",
        "aviation"
    ]):
        chinese_summary = "航空货运市场需求保持活跃。"

    elif any(word in title_lower for word in [
        "shipping",
        "container",
        "port",
        "vessel"
    ]):
        chinese_summary = "海运与港口市场波动持续。"

    elif any(word in title_lower for word in [
        "automation",
        "warehouse",
        "robot",
        "ai",
        "rfid"
    ]):
        chinese_summary = "物流自动化与智能仓储投资持续增长。"

    # =====================================
    # EXECUTIVE ANALYSIS
    # =====================================

    analysis = f"""
This development reflects ongoing changes across the logistics,
transportation, and supply chain sector.

Key implications may include freight capacity shifts,
operational adjustments, supply chain efficiency impact,
and changing regional market conditions.

Summary:
{clean_summary}
"""

    summarized.append({

        "title": title,

        "chinese_summary": chinese_summary,

        "link": item["link"],

        "analysis": analysis
    })

with open(
    "summarized_news.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        summarized,
        f,
        ensure_ascii=False,
        indent=2
    )

print("summarized_news.json generated")
