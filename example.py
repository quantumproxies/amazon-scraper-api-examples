"""Minimal Amazon search API call — one typed row per product.

Docs & schema: https://quanticdata.io/collectors/amazon-scraper-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/amazon_search/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "running shoes",
        "country": "us",
        "max_results": 40
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("page"), row.get("asin"), row.get("title"))
print(f"{len(data['results'])} products, cost ${data['cost']}")
