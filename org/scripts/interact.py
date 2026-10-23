import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file://%s/mock_shower.html'%sys.argv[1],wait_until='load'); await pg.wait_for_timeout(600)
        print('bar at top:', await pg.evaluate("document.querySelector('[data-lmv-bar]').classList.contains('on')"))
        await pg.screenshot(path='m_top.png')
        await pg.evaluate("window.scrollTo(0,1400)"); await pg.wait_for_timeout(600)
        print('bar after scroll:', await pg.evaluate("document.querySelector('[data-lmv-bar]').classList.contains('on')"))
        await pg.screenshot(path='m_scrolled.png')
        await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(400)
        print('bar back at top:', await pg.evaluate("document.querySelector('[data-lmv-bar]').classList.contains('on')"))
        # variant switch updates price
        await pg.click("text=Refill 3-Pack")
        print('prices:', await pg.eval_on_selector_all('[data-lmv-price]','e=>e.map(x=>x.textContent)'))
        # qty
        await pg.click('[data-lmv-inc]'); await pg.click('[data-lmv-inc]'); await pg.click('[data-lmv-dec]')
        print('qty:', await pg.input_value('input[name=quantity]'))
        # tap targets
        for sel in ['.lmv-btn','.lmv-opt','.lmv-qty button','.lmv-faq summary']:
            bb=await pg.eval_on_selector_all(sel,'e=>e.map(x=>{const r=x.getBoundingClientRect();return [Math.round(r.width),Math.round(r.height)]})')
            print(sel,bb[:3])
        # faq opens
        await pg.evaluate("document.querySelector('.lmv-faq summary').scrollIntoView()"); await pg.click('.lmv-faq summary')
        print('faq open:', await pg.evaluate("document.querySelector('.lmv-faq details').open"))
        await b.close()
asyncio.run(main())
