import json
import os

from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

item = news[0]

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"Summarize this logistics news in simple English: {item['title']}"
)

summarized = [{
    "title": item["title"],
    "link": item["link"],
    "analysis": response.text
}]

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(summarized, f, ensure_ascii=False, indent=2)

print("summarized_news.json generated")
