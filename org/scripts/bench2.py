import asyncio,re,json
from playwright.async_api import async_playwright
SITES={
 'jolie (shower)':'https://www.jolie.com',
 'canopy (shower)':'https://canopy.co',
 'supply (razor)':'https://supply.co',
 'billie (razor)':'https://mybillie.com',
 'hero (patches)':'https://herocosmetics.us',
 'starface (patches)':'https://starface.world',
 'patchology (eye patches)':'https://patchology.com',
 'tweezerman/ brow':'https://www.tweezerman.com',
}
JS=open("bench.js").read()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        ctx=await b.new_context(ignore_https_errors=True,user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36',viewport={'width':1280,'height':900})
        for k,u in SITES.items():
            pg=await ctx.new_page()
            try:
                r=await pg.goto(u,wait_until='domcontentloaded',timeout=40000)
                await pg.wait_for_timeout(3500)
                d=await pg.evaluate(JS)
                print('==',k,r.status if r else '', pg.url)
                print(json.dumps(d,ensure_ascii=False)[:1500])
            except Exception as e:
                print('==',k,'ERR',str(e)[:120])
            await pg.close()
        await b.close()
asyncio.run(main())
