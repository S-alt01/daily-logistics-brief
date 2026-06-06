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
# Build Story
# =========================================

story = []

# =========================================
# Title
# =========================================

story.append(
    Paragraph(
        "Daily Logistics Intelligence Brief",
        styles['Title']
    )
)

story.append(Spacer(1, 20))

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
        styles['Heading2']
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
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 8))

story.append(Spacer(1, 20))

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
            styles['Heading2']
        )
    )

    story.append(Spacer(1, 12))

    category_items = [
        item for item in news_items
        if item.get("category") == category
    ]

    # =====================================
    # No News
    # =====================================

    if not category_items:

        story.append(
            Paragraph(
                "Nil",
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 20))

        continue

    # =====================================
    # News Items
    # =====================================

    for item in category_items:

        # Title

        story.append(
            Paragraph(
                item.get(
                    "title",
                    "Untitled News"
                ),
                styles['Heading3']
            )
        )

        story.append(Spacer(1, 6))

        # Chinese Summary

        chinese_summary = item.get(
            "chinese_summary",
            ""
        )

        if chinese_summary:

            story.append(
                Paragraph(
                    chinese_summary,
                    chinese_style
                )
            )

            story.append(Spacer(1, 8))

        # Analysis

        story.append(
            Paragraph(
                item.get(
                    "analysis",
                    "No analysis available."
                ),
                styles['BodyText']
            )
        )

        story.append(Spacer(1, 8))

        # Link

        link = item.get(
            "link",
            ""
        )

        if link:

            story.append(
                Paragraph(
                    f"<font color='blue'>{link}</font>",
                    styles['BodyText']
                )
            )

        story.append(Spacer(1, 20))

# =========================================
# Build PDF
# =========================================

doc.build(story)

print("Professional PDF generated")
