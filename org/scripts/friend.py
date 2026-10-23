import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        for label,vp in [('d',{'width':1280,'height':900}),('m',{'width':390,'height':844})]:
            pg=await b.new_page(viewport=vp)
            r=await pg.goto('https://5ykszq-ie.myshopify.com/',wait_until='networkidle',timeout=60000)
            print(label,r.status,pg.url)
            await pg.wait_for_timeout(1500)
            h=await pg.evaluate("document.documentElement.scrollHeight")
            # scroll to trigger lazy/reveal
            for y in range(0,h,600):
                await pg.evaluate("window.scrollTo(0,%d)"%y); await pg.wait_for_timeout(120)
            await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(500)
            await pg.screenshot(path='friend_%s.png'%label,full_page=True)
            if label=='d':
                info=await pg.evaluate("""()=>{const cs=getComputedStyle(document.body);const out={bodyFont:cs.fontFamily,bodyBg:cs.backgroundColor,color:cs.color};
                const h=document.querySelector('h1,h2');if(h){const c=getComputedStyle(h);out.h=[c.fontFamily,c.fontSize,c.fontWeight,c.color]}
                const btn=document.querySelector('a.button,button.button,.button');if(btn){const c=getComputedStyle(btn);out.btn=[c.backgroundColor,c.color,c.borderRadius]}
                return out}""")
                print(info)
            await pg.close()
        await b.close()
asyncio.run(main())
