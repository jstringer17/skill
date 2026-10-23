import asyncio,re
from playwright.async_api import async_playwright
U="https://www.cjdropshipping.com/product/replacement-shower-filter-for-held-showerhead---high-output-shower-water-filter-to-remove-chlorine-fluoride-and-hard-water-p-2604190751231614300.html"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--disable-blink-features=AutomationControlled'])
        c=await b.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',viewport={'width':1280,'height':900})
        pg=await c.new_page()
        await pg.goto(U,wait_until='domcontentloaded',timeout=60000)
        for i in range(6):
            await pg.wait_for_timeout(3000)
            t=await pg.title(); print(i,t[:80])
            if 'verification' not in t.lower(): break
        imgs=await pg.evaluate("Array.from(document.images).map(i=>i.currentSrc||i.src).filter(s=>s.includes('cjdropshipping')||s.includes('cc-west')||s.includes('oss'))")
        print(len(imgs)); print('\n'.join(list(dict.fromkeys(imgs))[:15]))
        await b.close()
asyncio.run(main())
