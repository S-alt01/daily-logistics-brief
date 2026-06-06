import json
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
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
# TOP 5 SUMMARY
# ======================

story.append(
    Paragraph(
        "TOP 5 SUMMARY",
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
    "Express": [],
    "Air Cargo": [],
    "Ocean Freight": [],
    "AIDC": [],
    "Other Logistics": []
}

for item in news_items:

    title = item["title"].lower()

    # Express
    if any(word in title for word in [
        "dhl",
        "fedex",
        "ups",
        "express"
    ]):
        categories["Express"].append(item)

    # Air Cargo
    elif any(word in title for word in [
        "air",
        "cargo",
        "airline",
        "aviation"
    ]):
        categories["Air Cargo"].append(item)

    # Ocean Freight
    elif any(word in title for word in [
        "ocean",
        "shipping",
        "vessel",
        "container",
        "port"
    ]):
        categories["Ocean Freight"].append(item)

    # AIDC
    elif any(word in title for word in [
        "ai",
        "automation",
        "robot",
        "warehouse",
        "rfid",
        "barcode"
    ]):
        categories["AIDC"].append(item)

    # Other
    else:
        categories["Other Logistics"].append(item)

# ======================
# CATEGORY SECTIONS
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

        # Title
        story.append(
            Paragraph(
                item["title"],
                styles['Heading2']
            )
        )

        # Summary
        story.append(
            Paragraph(
                item["analysis"],
                styles['BodyText']
            )
        )

        # Link
        link_html = f'''
        <font color="blue">
        Source Link:
        <a href="{item["link"]}">
        {item["link"]}
        </a>
        </font>
        '''

        story.append(
            Paragraph(
                link_html,
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 18))

doc.build(story)

print("PDF generated")
