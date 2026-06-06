import json
import re

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

summarized = []

for item in news:

    clean_summary = re.sub(
        '<.*?>',
        '',
        item.get("summary", "")
    )

    clean_summary = clean_summary.strip()

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
        "title": item["title"],
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
