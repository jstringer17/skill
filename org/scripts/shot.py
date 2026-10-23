import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
        for name in ['shower','razor']:
            for label,vp in [('desktop',{'width':1280,'height':900}),('mobile',{'width':390,'height':844})]:
                pg=await b.new_page(viewport=vp)
                msgs=[]
                pg.on('console',lambda m:msgs.append(m.text))
                pg.on('pageerror',lambda e:msgs.append('ERR '+str(e)))
                await pg.goto('file://%s/mock_%s.html'%(sys.argv[1],name),wait_until='load')
                await pg.wait_for_timeout(800)
                await pg.screenshot(path='%s_%s.png'%(name,label),full_page=True)
                ov=await pg.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth")
                print(name,label,'h-overflow:',ov,msgs[:3])
                await pg.close()
        await b.close()
asyncio.run(main())
