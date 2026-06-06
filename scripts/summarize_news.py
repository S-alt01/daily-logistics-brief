import json

# =========================================
# Load RSS News
# =========================================

with open(
    "news.json",
    "r",
    encoding="utf-8"
) as f:

    news = json.load(f)

summarized = []

# =========================================
# Categorization Function
# =========================================

def categorize(title):

    t = title.lower()

    # =====================================
    # Express
    # =====================================

    if any(keyword in t for keyword in [
        "dhl",
        "fedex",
        "ups",
        "express",
        "parcel"
    ]):
        return "Express"

    # =====================================
    # Air Cargo
    # =====================================

    elif any(keyword in t for keyword in [
        "air cargo",
        "cargo airline",
        "freighter",
        "iata",
        "air freight"
    ]):
        return "Air Cargo"

    # =====================================
    # Ocean Freight
    # =====================================

    elif any(keyword in t for keyword in [
        "ocean",
        "shipping",
        "container",
        "maersk",
        "msc",
        "freight rate",
        "vessel"
    ]):
        return "Ocean Freight"

    # =====================================
    # AIDC
    # =====================================

    elif any(keyword in t for keyword in [
        "rfid",
        "barcode",
        "scanner",
        "automation",
        "warehouse robot",
        "aidc"
    ]):
        return "AIDC"

    # =====================================
    # Other Logistics
    # =====================================

    else:
        return "Other Logistics"

# =========================================
# Generate Summary
# =========================================

for item in news[:50]:

    title = item.get(
        "title",
        "Untitled News"
    )

    link = item.get(
        "link",
        ""
    )

    category = categorize(title)

    # =====================================
    # Analysis
    # =====================================

    analysis = (
        f"This development may influence "
        f"{category.lower()} market dynamics, "
        f"capacity planning, and supply chain operations."
    )

    # =====================================
    # Chinese Summary
    # =====================================

    chinese_summary = (
        f"该新闻与{category}行业相关，"
        f"可能影响未来物流市场、运力及供应链变化。"
    )

    # =====================================
    # Key Signal
    # =====================================

    key_signal = (
        f"{category} sector continues to show "
        f"strategic market movement."
    )

    summarized.append({

        "title": title,

        "link": link,

        "category": category,

        "analysis": analysis,

        "chinese_summary": chinese_summary,

        "key_signal": key_signal
    })

# =========================================
# Save Output
# =========================================

with open(
    "summarized_news.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        summarized,
        f,
        ensure_ascii=False,
        indent=2
    )

print("summarized_news.json generated")
