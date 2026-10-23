import asyncio,re,json
from playwright.async_api import async_playwright
SITES={
 'jolie (shower)':'https://jolie.com',
 'canopy (shower)':'https://canopy.co',
 'supply (razor)':'https://supply.co',
 'billie (razor)':'https://mybillie.com',
 'hero (patches)':'https://herocosmetics.us',
 'starface (patches)':'https://starface.world',
 'patchology (eye patches)':'https://patchology.com',
 'tweezerman/ brow':'https://www.tweezerman.com',
}
JS="""()=>{
 const t=s=>[...document.querySelectorAll(s)].map(e=>e.innerText.trim().replace(/\\s+/g,' ')).filter(x=>x&&x.length<110);
 const body=document.body.innerText.toLowerCase();
 const uniq=a=>[...new Set(a)];
 return {title:document.title.slice(0,90),
  ann:uniq(t('[class*=announcement],[class*=Announcement],[class*=promo-bar],.shopify-section-group-header-group'))[:2],
  h1:uniq(t('h1')).slice(0,2),h2:uniq(t('h2')).slice(0,14),
  btn:uniq(t('a[class*=button],button[class*=button],a[class*=btn],button[class*=btn]')).slice(0,10),
  flags:Object.fromEntries(['reviews','guarantee','subscribe','free shipping','as seen','dermatologist','clinically','bundle','save ','money-back','star','tiktok','instagram','faq','ingredients','how it works','before','results'].map(k=>[k,body.includes(k)]))}
}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        ctx=await b.new_context(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36',viewport={'width':1280,'height':900})
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
