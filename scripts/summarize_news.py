import os
import json
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY EXISTS:", bool(api_key))

genai.configure(api_key=api_key)

models = genai.list_models()

output = []

for m in models:
    output.append(str(m.name))

with open("summarized_news.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Gemini test success")
