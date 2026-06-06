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

    title = str(item.get("title", ""))

    analysis = str(item.get("analysis", ""))

    title = title.encode(
        "latin-1",
        "ignore"
    ).decode("latin-1")

    analysis = analysis.encode(
        "latin-1",
        "ignore"
    ).decode("latin-1")

    story.append(
        Paragraph(
            title,
            styles['Heading2']
        )
    )

    story.append(
        Paragraph(
            analysis,
            styles['BodyText']
        )
    )

    story.append(Spacer(1, 20))

doc.build(story)

print("PDF generated")
