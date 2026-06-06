import json
import traceback

try:

    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate("daily_brief.pdf")

    styles = getSampleStyleSheet()

    story = []

    with open("summarized_news.json", "r", encoding="utf-8") as f:
        news_items = json.load(f)

    with open("json_dump.txt", "w", encoding="utf-8") as f:
        f.write(str(news_items[:1]))

    first = news_items[0]

    title = str(first.get("title", "NO TITLE"))
    analysis = str(first.get("analysis", "NO ANALYSIS"))

    story.append(Paragraph(title, styles['Heading2']))
    story.append(Spacer(1, 20))
    story.append(Paragraph(analysis, styles['BodyText']))

    doc.build(story)

    with open("pdf_debug.txt", "w") as f:
        f.write("PDF SUCCESS")

except Exception as e:

    with open("pdf_debug.txt", "w") as f:
        f.write(str(e))
        f.write("\n\n")
        f.write(traceback.format_exc())
