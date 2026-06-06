import json
import feedparser

# =========================================
# Load RSS News
# =========================================

with open(
    "news.json",
    "r",
    encoding="utf-8"
) as f:

    news_items = json.load(f)

# =========================================
# Output List
# =========================================

summarized_news = []

# =========================================
# Category Function
# =========================================

def categorize_news(title):

    title_lower = title.lower()

    # Express

    if any(keyword in title_lower for keyword in [
        "fedex",
        "ups",
        "dhl",
        "parcel",
        "delivery",
        "express"
    ]):

        return "Express"

    # Air Cargo

    elif any(keyword in title_lower for keyword in [
        "air cargo",
        "air freight",
        "cargo airline",
        "aviation",
        "freighter"
    ]):

        return "Air Cargo"

    # Ocean Freight

    elif any(keyword in title_lower for keyword in [
        "ocean",
        "shipping",
        "container",
        "port",
        "vessel",
        "freight"
    ]):

        return "Ocean Freight"

    # AIDC

    elif any(keyword in title_lower for keyword in [
        "ai",
        "automation",
        "robot",
        "warehouse",
        "technology",
        "digital"
    ]):

        return "AIDC"

    # Default

    else:

        return "Other Logistics"

# =========================================
# Generate Key Signal
# =========================================

def generate_key_signal(category):

    signals = {
        "Express": "Express delivery demand and parcel competition continue evolving.",
        "Air Cargo": "Air cargo market conditions continue shifting globally.",
        "Ocean Freight": "Ocean freight and shipping market volatility remains elevated.",
        "AIDC": "Logistics automation and digital supply chain investment continue growing.",
        "Other Logistics": "Broader logistics market conditions remain dynamic."
    }

    return signals.get(
        category,
        "Logistics market conditions remain dynamic."
    )

# =========================================
# Process News
# =========================================

for item in news_items:

    title = item.get(
        "title",
        "No title"
    )

    link = item.get(
        "link",
        ""
    )

    summary = item.get(
        "summary",
        ""
    )

    # =====================================
    # Category
    # =====================================

    category = categorize_news(title)

    # =====================================
    # Key Signal
    # =====================================

    key_signal = generate_key_signal(category)

    # =====================================
    # Chinese Summary
    # =====================================

    chinese_summary_map = {
        "Express": "快递与包裹市场竞争持续加剧。",
        "Air Cargo": "全球航空货运市场持续波动。",
        "Ocean Freight": "海运与港口市场波动持续。",
        "AIDC": "物流自动化与智能仓储投资持续增长。",
        "Other Logistics": "物流行业出现新的市场动态。"
    }

    chinese_summary = chinese_summary_map.get(
        category,
        "物流行业出现新的市场动态。"
    )

    # =====================================
    # Analysis
    # =====================================

    analysis = f"""
This development reflects ongoing changes across the logistics,
transportation, and supply chain sector.

Key implications may include freight capacity shifts,
operational adjustments, supply chain efficiency impact,
and changing regional market conditions.

Summary:
{summary}
"""

    # =====================================
    # Append
    # =====================================

    summarized_news.append({

        "title": title,

        "category": category,

        "key_signal": key_signal,

        "chinese_summary": chinese_summary,

        "link": link,

        "analysis": analysis

    })

# =========================================
# Save JSON
# =========================================

with open(
    "summarized_news.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        summarized_news,
        f,
        ensure_ascii=False,
        indent=2
    )

print("News summarized successfully")
