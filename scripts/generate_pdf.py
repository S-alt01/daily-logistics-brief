import json
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("daily_brief.pdf")

styles = getSampleStyleSheet()

story = []

today = datetime.today().strftime("%Y-%m-%d")

# ======================
# Title
# ======================

story.append(
    Paragraph(
        f"Daily Logistics & AIDC Brief<br/>{today}",
        styles['Title']
    )
)

story.append(Spacer(1, 30))

with open("summarized_news.json", "r", encoding="utf-8") as f:
    news_items = json.load(f)

# ======================
# Executive Summary
# ======================

story.append(
    Paragraph(
        "Executive Summary",
        styles['Heading1']
    )
)

story.append(Spacer(1, 15))

for i, item in enumerate(news_items[:5], start=1):

    text = f"{i}. {item['title']}"

    story.append(
        Paragraph(
            text,
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 8))

story.append(Spacer(1, 25))

# ======================
# Categories
# ======================

categories = {
    "Ocean Freight": [],
    "Air Cargo": [],
    "Warehousing & Automation": [],
    "Trade & Tariffs": [],
    "Other Logistics": []
}

for item in news_items:

    title = item["title"].lower()

    if any(word in title for word in ["port", "shipping", "vessel", "container"]):
        categories["Ocean Freight"].append(item)

    elif any(word in title for word in ["air", "cargo", "airline"]):
        categories["Air Cargo"].append(item)

    elif any(word in title for word in ["warehouse", "robot", "automation", "ai"]):
        categories["Warehousing & Automation"].append(item)

    elif any(word in title for word in ["tariff", "trade", "customs"]):
        categories["Trade & Tariffs"].append(item)

    else:
        categories["Other Logistics"].append(item)

# ======================
# Categorized News
# ======================

for category, items in categories.items():

    if not items:
        continue

    story.append(
        Paragraph(
            category,
            styles['Heading1']
        )
    )

    story.append(Spacer(1, 12))

    for item in items:

        story.append(
            Paragraph(
                item["title"],
                styles['Heading2']
            )
        )

        story.append(
            Paragraph(
                item["analysis"],
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 15))

doc.build(story)

print("PDF generated")
