import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("daily_brief.pdf")

styles = getSampleStyleSheet()

story = []

story.append(
    Paragraph(
        "Daily Logistics & AIDC Brief",
        styles['Title']
    )
)

story.append(Spacer(1, 20))

with open("summarized_news.json", "r", encoding="utf-8") as f:
    news_items = json.load(f)

for item in news_items[:3]:

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

    story.append(Spacer(1, 20))

doc.build(story)

print("PDF generated")
