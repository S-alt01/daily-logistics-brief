import feedparser
import json
from datetime import datetime

news_items = []

with open("rss_sources.txt") as f:
    urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

for url in urls:
    try:
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            news = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": feed.feed.get("title", url),
                "summary": entry.get("summary", "")
            }

            news_items.append(news)

    except Exception as e:
        print("ERROR:", url, e)

timestamp = datetime.now().strftime("%Y-%m-%d")

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)

print(f"Saved {len(news_items)} news items.")
