import json

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# =========================================
# Register Chinese Font
# =========================================

pdfmetrics.registerFont(
    UnicodeCIDFont('STSong-Light')
)

# =========================================
# PDF Setup
# =========================================

doc = SimpleDocTemplate(
    "daily_brief.pdf",
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=28
)

styles = getSampleStyleSheet()

# =========================================
# English Styles
# =========================================

title_style = styles['Title']

heading_style = styles['Heading2']

body_style = styles['BodyText']

body_style.leading = 18

# =========================================
# Chinese Style
# =========================================

chinese_style = ParagraphStyle(
    'Chinese',
    parent=styles['BodyText'],
    fontName='STSong-Light',
    fontSize=10,
    leading=16,
)

# =========================================
# Key Signal Style
# =========================================

signal_style = ParagraphStyle(
    'Signal',
    parent=styles['BodyText'],
    textColor=colors.darkblue,
    fontSize=10,
    leading=16,
)

# =========================================
# Build Story
# =========================================

story = []

# =========================================
# Title
# =========================================

story.append(
    Paragraph(
        "Daily Logistics Intelligence Brief",
        title_style
    )
)

story.append(Spacer(1, 24))

# =========================================
# Load News
# =========================================

with open(
    "summarized_news.json",
    "r",
    encoding="utf-8"
) as f:

    news_items = json.load(f)

# =========================================
# TOP 5 KEY SIGNALS
# =========================================

story.append(
    Paragraph(
        "TOP 5 KEY SIGNALS",
        heading_style
    )
)

story.append(Spacer(1, 12))

for item in news_items[:5]:

    signal = item.get(
        "key_signal",
        "Market conditions remain dynamic."
    )

    story.append(
        Paragraph(
            f"• {signal}",
            signal_style
        )
    )

    story.append(Spacer(1, 10))

story.append(Spacer(1, 24))

# =========================================
# Categories
# =========================================

categories = [
    "Express",
    "Air Cargo",
    "Ocean Freight",
    "AIDC",
    "Other Logistics"
]

# =========================================
# Generate Sections
# =========================================

for category in categories:

    story.append(
        Paragraph(
            category,
            heading_style
        )
    )

    story.append(Spacer(1, 12))

    category_items = []

    for item in news_items:

        item_category = item.get(
            "category",
            "Other Logistics"
        )

        if item_category == category:
            category_items.append(item)

    # =====================================
    # If No News
    # =====================================

    if not category_items:

        story.append(
            Paragraph(
                "Nil",
                body_style
            )
        )

        story.append(Spacer(1, 20))

        continue

    # =====================================
    # News Items
    # =====================================

    for item in category_items:

        title = item.get(
            "title",
            "Untitled News"
        )

        analysis = item.get(
            "analysis",
            "No analysis available."
        )

        chinese_summary = item.get(
            "chinese_summary",
            ""
        )

        link = item.get(
            "link",
            ""
        )

        # =================================
        # Title
        # =================================

        story.append(
            Paragraph(
                title,
                heading_style
            )
        )

        story.append(Spacer(1, 6))

        # =================================
        # Chinese Summary
        # =================================

        if chinese_summary:

            story.append(
                Paragraph(
                    chinese_summary,
                    chinese_style
                )
            )

            story.append(Spacer(1, 8))

        # =================================
        # English Analysis
        # =================================

        story.append(
            Paragraph(
                analysis,
                body_style
            )
        )

        story.append(Spacer(1, 8))

        # =================================
        # Link
        # =================================

        if link:

            story.append(
                Paragraph(
                    f"<font color='blue'>{link}</font>",
                    body_style
                )
            )

            story.append(Spacer(1, 20))

# =========================================
# Build PDF
# =========================================

doc.build(story)

print("Professional PDF generated")
