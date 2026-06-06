from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("daily_brief.pdf")

styles = getSampleStyleSheet()

story = []

story.append(
    Paragraph(
        "Daily Logistics Brief Test",
        styles['Title']
    )
)

doc.build(story)

print("PDF generated")
