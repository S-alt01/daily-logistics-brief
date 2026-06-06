import json
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# =========================================
# REGISTER CHINESE FONT
# =========================================

pdfmetrics.registerFont(
    UnicodeCIDFont('STSong-Light')
)

# =========================================
# PDF SETTINGS
# =========================================

doc = SimpleDocTemplate(
    "daily_brief.pdf",
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# =========================================
# CUSTOM STYLES
# =========================================

title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Title'],
    fontName='STSong-Light',
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0B1F3A"),
    spaceAfter=30
)

section_style = ParagraphStyle(
    'SectionStyle',
    parent=styles['Heading1'],
    fontName='STSong-Light',
    fontSize=16,
    leading=22,
    textColor=colors.HexColor("#12355B"),
    spaceAfter=12
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['BodyText'],
    fontName='STSong-Light',
    fontSize=10,
    leading=16
)

# =========================================
# PAGE FOOTER
# =========================================

def add_page_number(canvas, doc):

    page_num = canvas.getPageNumber()

    footer_text = (
        f"Daily Logistics Intelligence Brief | "
        f"Page {page_num}"
    )

    canvas.setFont("Helvetica", 8)

    canvas.drawRightString(
        550,
        20,
        footer_text
    )

# =========================================
# STORY
# =========================================

story = []

today = datetime.today().strftime("%Y-%m-%d")

# =========================================
# TITLE
# =========================================

story.append(
    Paragraph(
        "Daily Logistics Intelligence Brief",
        title_style
    )
)

story.append(
    Paragraph(
        today,
        styles['Heading2']
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
        section_style
    )
)

for i, item in enumerate(news_items[:5], start=1):

    text = f"<b>{i}.</b> {item['title']}"

    story.append(
        Paragraph(
            text,
            body_style
        )
    )

    story.append(Spacer(1, 8))

story.append(Spacer(1, 25))

# =========================================
# DYNAMIC KEY SIGNALS
# =========================================

story.append(
    Paragraph(
        "KEY MARKET SIGNALS",
        section_style
    )
)

signals = []

all_titles = " ".join(
    [item["title"].lower() for item in news_items]
)

if any(word in all_titles for word in [
    "dhl",
    "fedex",
    "ups",
    "express",
    "parcel"
]):
    signals.append(
        "• Express competition continues intensifying"
    )

if any(word in all_titles for word in [
    "air cargo",
    "air freight",
    "aviation"
]):
    signals.append(
        "• Air cargo demand remains active"
    )

if any(word in all_titles for word in [
    "shipping",
    "container",
    "port",
    "vessel"
]):
    signals.append(
        "• Ocean freight market volatility remains elevated"
    )

if any(word in all_titles for word in [
    "automation",
    "warehouse",
    "robot",
    "rfid",
    "ai"
]):
    signals.append(
        "• Warehouse automation investment accelerating"
    )

if not signals:

    signals.append(
        "• Logistics market conditions remain stable"
    )

for signal in signals:

    story.append(
        Paragraph(
            signal,
            body_style
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

    # EXPRESS PRIORITY
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

    # AIR CARGO
    elif any(word in title for word in [
        "air cargo",
        "air freight",
        "aviation"
    ]):
        categories["Air Cargo"].append(item)

    # OCEAN
    elif any(word in title for word in [
        "shipping",
        "container",
        "port",
        "vessel"
    ]):
        categories["Ocean Freight"].append(item)

    # AIDC
    elif any(word in title for word in [
        "automation",
        "robot",
        "warehouse",
        "rfid",
        "barcode",
        "ai"
    ]):
        categories["AIDC"].append(item)

    else:
        categories["Other Logistics"].append(item)

# =========================================
# SECTION ORDER
# =========================================

section_order = [
    "Express",
    "Air Cargo",
    "Ocean Freight",
    "AIDC",
    "Other Logistics"
]

# =========================================
# SECTION CONTENT
# =========================================

for section in section_order:

    story.append(
        Paragraph(
            section.upper(),
            section_style
        )
    )

    story.append(Spacer(1, 10))

    items = categories[section]

    # NIL
    if not items:

        story.append(
            Paragraph(
                "NIL",
                body_style
            )
        )

        story.append(Spacer(1, 20))

        continue

    for item in items[:5]:

        # TITLE
        story.append(
            Paragraph(
                f"<b>{item['title']}</b>",
                styles['Heading2']
            )
        )

        story.append(Spacer(1, 5))

        # CHINESE SUMMARY
        story.append(
            Paragraph(
                f"<font color='#444444'><b>中文摘要：</b>{item.get('chinese_summary', '')}</font>",
                body_style
            )
        )

        story.append(Spacer(1, 6))

        # ANALYSIS
        story.append(
            Paragraph(
                item["analysis"],
                body_style
            )
        )

        story.append(Spacer(1, 6))

        # SOURCE
        link_html = f'''
        <font color="#1D4E89">
        Source:
        <a href="{item["link"]}">
        {item["link"]}
        </a>
        </font>
        '''

        story.append(
            Paragraph(
                link_html,
                body_style
            )
        )

        story.append(Spacer(1, 20))

# =========================================
# BUILD PDF
# =========================================

doc.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
)

print("Professional intelligence PDF generated")
