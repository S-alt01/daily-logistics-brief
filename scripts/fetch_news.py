import json

news = [
    {
        "title": "Test logistics news",
        "link": "https://example.com"
    }
]

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("news.json generated")
