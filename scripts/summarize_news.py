import json
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

summarized = []

for item in news[:3]:

    prompt = f"""
请用简体中文简短总结下面新闻。

不要使用 markdown 或特殊符号。

新闻标题：
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
