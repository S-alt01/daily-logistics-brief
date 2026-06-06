import json
import feedparser

feed_url = "https://www.freightwaves.com/news/feed"

feed = feedparser.parse(feed_url)

news = []

for entry in feed.entries[:3]:

    news.append({
        "title": entry.title,
        "link": entry.link
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("news.json generated")
