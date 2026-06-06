import requests
import os

API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Say hello."
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

with open("gemini_test.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print(response.status_code)
