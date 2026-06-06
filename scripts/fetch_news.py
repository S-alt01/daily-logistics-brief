import json
import feedparser

feed_urls = [

    "https://www.freightwaves.com/news/feed",

    "https://www.supplychaindive.com/feeds/news/",

    "https://www.aircargonews.net/feed/",

    "https://www.logisticsmgmt.com/rss/all",

    "https://www.ttnews.com/rss.xml"
]

news = []

for url in feed_urls:

    feed = feedparser.parse(url)

    for entry in feed.entries[:10]:

        summary = ""

        if "summary" in entry:
            summary = entry.summary

        news.append({
            "title": entry.title,
            "link": entry.link,
            "summary": summary
        })

# Remove duplicates
unique_news = []

seen_titles = set()

for item in news:

    if item["title"] not in seen_titles:

        unique_news.append(item)

        seen_titles.add(item["title"])

# Save
with open("news.json", "w", encoding="utf-8") as f:

    json.dump(unique_news, f, ensure_ascii=False, indent=2)

print(f"{len(unique_news)} news items generated")
