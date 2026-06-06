import json
from datetime import datetime
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()

pdf.set_font("Arial", "B", 18)
pdf.cell(0, 10, "Daily Logistics & AIDC Brief", ln=True)

pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, datetime.now().strftime("%Y-%m-%d"), ln=True)

pdf.ln(10)

pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Executive Summary", ln=True)

pdf.set_font("Arial", "", 11)

executive_summary = """
- Air cargo demand remains strong
- Red Sea shipping risks continue
- AI server supply chain remains active
- Taiwan ODM shipments increasing
"""

pdf.multi_cell(0, 8, executive_summary)

pdf.ln(5)

with open("summarized_news.json", "r", encoding="utf-8") as f:
    news_items = json.load(f)

for item in news_items[:30]:

    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.multi_cell(0, 8, item["title"])

    pdf.ln(3)

    pdf.set_font("Arial", "", 11)

    analysis = item["analysis"]

    clean_text = analysis.encode("latin-1", "replace").decode("latin-1")

    pdf.multi_cell(0, 7, clean_text)

    pdf.ln(5)

    pdf.set_text_color(0, 0, 255)

    pdf.cell(0, 8, item["link"], ln=True, link=item["link"])

    pdf.set_text_color(0, 0, 0)

pdf.output("daily_brief.pdf")

print("PDF generated.")
