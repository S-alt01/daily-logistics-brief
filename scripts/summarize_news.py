import json

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

summarized = []

for item in news[:3]:

    summarized.append({
        "title": item["title"],
        "link": item["link"],
        "analysis": "This is AI summary test."
    })

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(summarized, f, ensure_ascii=False, indent=2)

print("summarized_news.json generated")
