# jimohne-ads

Ad creatives for Jimohne campaigns.

## WhatsApp Shop Bot — "While You Sleep" (Nov 2026)
- `creatives/shopbot-square.jpg` — 1080×1080 (Feed)
- `creatives/shopbot-story.jpg` — 1080×1920 (Stories / Reels)

Rebuild: `python3 render.py` (renders `ad.html` with Playwright + Chrome into `out/`).

## Website price calculator — ChatGPT Ads (Nov 2026)
Landing page: https://jimohne.com/website (WhatsApp quote). Square 1:1 images, 1200×1200.
- `chatgpt/out/chatgpt-1-price-on-phone` — real price card from the calculator on a phone
- `chatgpt/out/chatgpt-2-from-120k` — "from ₦120,000" with the three main prices
- `chatgpt/out/chatgpt-3-whatsapp-quote` — the quote message arriving on WhatsApp
- `chatgpt/out/chatgpt-4-which-website` — store / booking / school / business, with prices

Ad text: Title "Website price in 60 seconds" · Description "Pick your website, see the naira price, send it on WhatsApp."
Prices in the images come from jimohne-website `website/prices.json`; re-render if prices change.
Rebuild: `cd chatgpt && python3 render.py` (fonts are bundled in `chatgpt/fonts/`).
