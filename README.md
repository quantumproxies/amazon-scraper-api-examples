# Amazon search API — examples

Amazon search results for a keyword — ASIN, price, rating, reviews, image.

**Live page, full schema & pricing → [quanticdata.io/collectors/amazon-scraper-api/](https://quanticdata.io/collectors/amazon-scraper-api/)**

Searches an Amazon marketplace for a keyword and delivers the result cards: ASIN, title, brand, current and list price, star rating, review count, sponsored flag, image and the clean /dp/ URL. Reads the server-rendered page on the TLS tier — no browser — and retries on a fresh exit when Amazon fronts the request with its bot-check interstitial.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/amazon_search/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "running shoes", "country": "us", "max_results": 40}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — What to search on Amazon, e.g. "running shoes".
- `country` (string) — ISO 3166-1 alpha-2 code — picks the local site AND the proxy exit (default us).
- `max_results` (integer) — How many products to deliver at most (1–200). You pay only for delivered products.

## Output — one row per product

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position across pages. |
| `page` | integer | Search page the row came from. |
| `asin` | string | Amazon product id. |
| `title` | string | Product title. |
| `brand` | string | Brand line when the layout shows one. |
| `price` | string | Current price as shown. |
| `price_value` | number | Numeric current price. |
| `list_price` | string | Struck-through list price when discounted. |
| `rating` | number | Star rating (1–5). |
| `reviews` | integer | Review count (1.4K → 1400). |
| `sponsored` | boolean | True for paid placements. |
| `image` | string | Thumbnail URL. |
…and 2 more fields — full schema on the [live page](https://quanticdata.io/collectors/amazon-scraper-api/).

## Pricing

**$0.001 per delivered product** ($1 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 2,000 products — no card required.

## Links

- This collector: https://quanticdata.io/collectors/amazon-scraper-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
