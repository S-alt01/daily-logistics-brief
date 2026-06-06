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
# TOP 5 SUMMARY
# =========================================

story.append(
    Paragraph(
        "TOP 5 SUMMARY",
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
# DYNAMIC KEY MARKET SIGNALS
# =========================================

story.append(
    Paragraph(
        "KEY MARKET SIGNALS",
        styles['Heading1']
    )
)

story.append(Spacer(1, 12))

signals = []

all_titles = " ".join(
    [item["title"].lower() for item in news_items]
)

# =====================================
# EXPRESS
# =====================================

if any(word in all_titles for word in [
    "dhl",
    "fedex",
    "ups",
    "express",
    "parcel",
    "courier",
    "last mile"
]):
    signals.append(
        "• Express competition continues intensifying"
    )

# =====================================
# AIR CARGO
# =====================================

if any(word in all_titles for word in [
    "air cargo",
    "air freight",
    "aviation"
]):
    signals.append(
        "• Air cargo demand remains active"
    )

# =====================================
# OCEAN FREIGHT
# =====================================

if any(word in all_titles for word in [
    "port",
    "shipping",
    "container",
    "vessel",
    "ocean freight"
]):
    signals.append(
        "• Ocean freight market volatility remains elevated"
    )

# =====================================
# AIDC
# =====================================

if any(word in all_titles for word in [
    "automation",
    "robot",
    "warehouse",
    "rfid",
    "barcode",
    "ai"
]):
    signals.append(
        "• Warehouse automation investment continues accelerating"
    )

# =====================================
# TRADE
# =====================================

if any(word in all_titles for word in [
    "tariff",
    "trade",
    "customs"
]):
    signals.append(
        "• Trade policy uncertainty remains a key market risk"
    )

# =====================================
# FALLBACK
# =====================================

if not signals:

    signals.append(
        "• Logistics market conditions remain stable"
    )

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

    # =====================================
    # EXPRESS FIRST PRIORITY
    # =====================================

    if any(word in title for word in [
        "dhl",
        "fedex",
        "ups",
        "express",
        "parcel",
        "courier",
        "last mile"
    ]):
        categories["Express"].append(item)

    # =====================================
    # AIR CARGO
    # =====================================

    elif any(word in title for word in [
        "air cargo",
        "air freight",
        "cargo airline",
        "aviation"
    ]):
        categories["Air Cargo"].append(item)

    # =====================================
    # OCEAN FREIGHT
    # =====================================

    elif any(word in title for word in [
        "shipping",
        "container",
        "port",
        "vessel",
        "ocean freight"
    ]):
        categories["Ocean Freight"].append(item)

    # =====================================
    # AIDC
    # =====================================

    elif any(word in title for word in [
        "automation",
        "robot",
        "warehouse",
        "rfid",
        "barcode",
        "ai"
    ]):
        categories["AIDC"].append(item)

    # =====================================
    # OTHER
    # =====================================

    else:
        categories["Other Logistics"].append(item)

# =========================================
# CATEGORY SECTIONS
# =========================================

for category, items in categories.items():

    story.append(
        Paragraph(
            category.upper(),
            styles['Heading1']
        )
    )

    story.append(Spacer(1, 15))

    # =====================================
    # NIL IF EMPTY
    # =====================================

    if not items:

        story.append(
            Paragraph(
                "NIL",
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 20))

        continue

    # =====================================
    # NEWS ITEMS
    # =====================================

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

doc.build(story)

print("PDF generated")
