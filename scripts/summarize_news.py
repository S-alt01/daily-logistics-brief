import json
import requests
import os

API_KEY = os.getenv("GEMINI_API_KEY")

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

item = news[0]

prompt = f"""
Summarize this logistics news in simple English.

Plain text only.
No markdown.

News:
{item['title']}
"""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

result = response.json()

analysis = result["candidates"][0]["content"]["parts"][0]["text"]

summarized = [{
    "title": item["title"],
    "link": item["link"],
    "analysis": analysis
}]

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(summarized, f, ensure_ascii=False, indent=2)

print("summarized_news.json generated")
