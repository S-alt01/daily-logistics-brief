import json
import traceback

try:

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

    for item in news_items[:1]:

        story.append(
            Paragraph(
                "TEST TITLE",
                styles['Heading2']
            )
        )

        story.append(
            Paragraph(
                "TEST ANALYSIS",
                styles['BodyText']
            )
        )

    doc.build(story)

    with open("pdf_debug.txt", "w") as f:
        f.write("PDF SUCCESS")

except Exception as e:

    with open("pdf_debug.txt", "w") as f:
        f.write(str(e))
        f.write("\n\n")
        f.write(traceback.format_exc())
