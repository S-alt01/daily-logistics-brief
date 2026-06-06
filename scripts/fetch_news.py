import feedparser
import json

news = []

with open("rss_sources.txt", "r") as f:
    feeds = f.readlines()

for url in feeds[:5]:
    feed = feedparser.parse(url.strip())

    for entry in feed.entries[:3]:
        news.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", "")
        })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("news.json generated")
