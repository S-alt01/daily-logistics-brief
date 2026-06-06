import json
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

summarized = []

item = news[0]

prompt = f"""
Summarize this logistics news in simple English.

No markdown.
No bullet points.
Plain text only.

News:
{item['title']}
"""

response = model.generate_content(prompt)

summarized.append({
    "title": item["title"],
    "link": item["link"],
    "analysis": response.text
})

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(summarized, f, ensure_ascii=False, indent=2)

print("summarized_news.json generated")
