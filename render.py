import asyncio
from playwright.async_api import async_playwright
base=open('ad.html').read()
phone='''<div class="phone">
<div class="top"><div class="av">MC</div><div><b>Mama Chidi Wholesale</b><small>online · replies instantly</small></div></div>
<div class="chat">
<div class="m in">Hi, I want 5 cartons of Indomie & 2 bags of rice 🙏<span class="t">11:42 PM</span></div>
<div class="m out">Done ✅ Here’s your order:
<div class="list"><div><span>5 × Indomie (ctn)</span><span>₦42,500</span></div><div><span>2 × Rice 50kg</span><span>₦156,000</span></div><div><b>Total</b><b>₦198,500</b></div></div>
<span class="btn">Pay now</span><span class="t">11:42 PM</span></div>
<div class="m in">Paid! 💸<span class="t">11:43 PM</span></div>
<div class="m out">Payment received. Delivery tomorrow 🚚<span class="t">11:43 PM</span></div>
</div></div>'''
pills='<div class="pills"><span>📦 Orders</span><span>💳 Payments</span><span>📋 Price list</span><span>⏰ 24/7</span></div>'
foot='<div class="foot"><div class="cta">Get your shop bot →</div><div class="url">jimohne.com</div></div>'
sq=f'''<style>:root{{--w:1080px;--h:1080px;--pad:64px;--h1:66px;--gap1:34px;--sub:27px;--subw:440px;--chat:21px;--cta:28px;--pill:21px}}</style>
<div style="display:flex;gap:44px;flex:1;margin-top:10px">
 <div style="flex:1.05;display:flex;flex-direction:column">
  <h1>Let WhatsApp take your orders <em>while you sleep</em></h1>
  <p class="sub">For wholesalers in Lagos &amp; Abuja. Customers browse, order and pay — right inside WhatsApp.</p>
  <div style="margin-top:auto">{pills}</div>
 </div>
 <div style="flex:1;display:flex;align-items:center">{phone}</div>
</div>
<div style="margin-top:36px">{foot}</div>'''
st=f'''<style>:root{{--w:1080px;--h:1920px;--pad:80px;--h1:96px;--gap1:110px;--sub:36px;--subw:880px;--chat:30px;--cta:38px;--pill:28px}}.brand span{{font-size:32px}}.url{{font-size:28px}}</style>
<h1>Let WhatsApp take your orders <em>while you sleep</em></h1>
<p class="sub">For wholesalers in Lagos &amp; Abuja. Customers browse, order and pay — right inside WhatsApp.</p>
<div style="margin:70px 40px 0">{phone}</div>
<div style="margin-top:50px">{pills}</div>
<div style="margin-top:50px">{foot}</div>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for name,html,w,h in [('square',sq,1080,1080),('story',st,1080,1920)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.set_content(base.replace('<!--CONTENT-->',html)); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'out/shopbot-{name}.png'); 
        await b.close()
asyncio.run(main())
