import json
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

with open("news.json", "r", encoding="utf-8") as f:
    news_items = json.load(f)

summarized_news = []

for item in news_items[:50]:

    prompt = f"""
You are a logistics and AIDC industry analyst.

Summarize this news in Traditional Chinese.

Return format:

1. AI Summary
2. Market Impact

News Title:
{item['title']}

News Summary:
{item['summary']}
"""

    try:

        response = model.generate_content(prompt)

        summarized_news.append({
            "title": item["title"],
            "link": item["link"],
            "source": item["source"],
            "published": item["published"],
            "analysis": response.text
        })

        print("DONE:", item["title"])

    except Exception as e:
        print("ERROR:", e)

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(summarized_news, f, ensure_ascii=False, indent=2)

print("Saved summarized news.")
