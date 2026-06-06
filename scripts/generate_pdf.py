import json
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate(
    "daily_brief.pdf",
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=30
)

styles = getSampleStyleSheet()

story = []

today = datetime.today().strftime("%Y-%m-%d")

# =========================================
# TITLE
# =========================================

story.append(
    Paragraph(
        f"Daily Logistics Intelligence Brief<br/>{today}",
        styles['Title']
    )
)

story.append(Spacer(1, 25))

# =========================================
# LOAD NEWS
# =========================================

with open("summarized_news.json", "r", encoding="utf-8") as f:
    news_items = json.load(f)

# =========================================
# EXECUTIVE SUMMARY
# =========================================

story.append(
    Paragraph(
        "EXECUTIVE INTELLIGENCE SUMMARY",
        styles['Heading1']
    )
)

story.append(Spacer(1, 15))

for i, item in enumerate(news_items[:5], start=1):

    text = f"<b>{i}.</b> {item['title']}"

    story.append(
        Paragraph(
            text,
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 10))

story.append(Spacer(1, 25))

# =========================================
# KEY MARKET SIGNALS
# =========================================

story.append(
    Paragraph(
        "KEY MARKET SIGNALS",
        styles['Heading1']
    )
)

story.append(Spacer(1, 12))

signals = [
    "• Port congestion pressure remains elevated",
    "• Air cargo demand continues stabilizing",
    "• Warehouse automation investment increasing",
    "• Trade policy uncertainty remains a market risk",
    "• Express carriers continue regional expansion"
]

for signal in signals:

    story.append(
        Paragraph(
            signal,
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 6))

story.append(Spacer(1, 25))

# =========================================
# CATEGORIES
# =========================================

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

    # Other Logistics
    else:
        categories["Other Logistics"].append(item)

# =========================================
# CATEGORY SECTIONS
# =========================================

for category, items in categories.items():

    if not items:
        continue

    story.append(
        Paragraph(
            category.upper(),
            styles['Heading1']
        )
    )

    story.append(Spacer(1, 15))

    for item in items[:5]:

        # Title
        story.append(
            Paragraph(
                f"<b>{item['title']}</b>",
                styles['Heading2']
            )
        )

        story.append(Spacer(1, 5))

        # Summary
        story.append(
            Paragraph(
                item["analysis"],
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 5))

        # Implication
        implication = """
        <i>Implication:</i>
        This development may influence logistics capacity,
        supply chain efficiency, and regional freight activity.
        """

        story.append(
            Paragraph(
                implication,
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 5))

        # Source Link
        link_html = f'''
        <font color="blue">
        Source:
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

# =========================================
# WATCHLIST
# =========================================

story.append(
    Paragraph(
        "WATCHLIST",
        styles['Heading1']
    )
)

story.append(Spacer(1, 12))

watch_items = [
    "• Red Sea shipping developments",
    "• US-China tariff policy changes",
    "• Air cargo pricing movement",
    "• Warehouse robotics adoption trends",
    "• Global port congestion indicators"
]

for watch in watch_items:

    story.append(
        Paragraph(
            watch,
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 6))

doc.build(story)

print("PDF generated")
