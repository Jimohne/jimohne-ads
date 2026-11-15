# Renders ads.html into four 1200x1200 PNGs (plus JPG copies) in out/. Run: python3 render.py
import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image
HERE = pathlib.Path(__file__).parent.resolve()
NAMES = {1: 'price-on-phone', 2: 'from-120k', 3: 'whatsapp-quote', 4: 'which-website'}
async def main():
    (HERE / 'out').mkdir(exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 1200})
        for n, name in NAMES.items():
            await pg.goto((HERE / 'ads.html').as_uri() + f'?n={n}')
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(300)
            png = HERE / 'out' / f'chatgpt-{n}-{name}.png'
            await pg.screenshot(path=str(png))
            Image.open(png).convert('RGB').save(png.with_suffix('.jpg'), quality=90)
        await b.close()
asyncio.run(main())
