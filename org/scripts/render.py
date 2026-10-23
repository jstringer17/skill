import re,json,sys
from liquid import Environment, Template
from liquid.filter import with_environment
env=Environment()

def money(v): return "$%.2f"%(float(v))
env.add_filter('money',money)
env.add_filter('asset_url',lambda s:'theme/assets/'+s)
env.add_filter('stylesheet_tag',lambda u:'<link rel="stylesheet" href="%s">'%u)
env.add_filter('image_url',lambda i,**k:i)
env.add_filter('image_tag',lambda i,**k:'<img src="%s">'%i)
env.add_filter('payment_button',lambda f:'<div class="shopify-payment-button"><button style="width:100%;height:48px;background:#5a31f4;color:#fff;border:0;border-radius:999px">Buy with Shop Pay</button></div>')

src=open('theme/sections/lumova-landing.liquid',encoding='utf8').read()
schema=re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}',src,re.S)
src=src[:schema.start()]
# form tag -> html form
src=re.sub(r"\{%-?\s*form\s+'product'[^%]*-?%\}",'<form id="{{ form_id }}" class="lmv-form">',src)
src=re.sub(r"\{%-?\s*endform\s*-?%\}",'</form>',src)
src=src.replace("{{ 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap' | stylesheet_tag }}","")
src=src.replace('{{ b.shopify_attributes }}','')
src=re.sub(r"image_tag:[^}]*?\}\}","image_tag }}",src)
src=src.replace("| image_url: width: 1200 | image_tag }}","| image_url | image_tag }}")
src=src.replace("{{ 'lumova.css' | asset_url | stylesheet_tag }}",'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap"><style>'+open('theme/assets/lumova.css').read()+'</style>')
src=src.replace("<script src=\"{{ 'lumova.js' | asset_url }}\" defer></script>","<script>"+open('theme/assets/lumova.js').read()+"</script>")

def build(tpl,title,variants):
    t=json.loads(re.sub(r'/\*.*?\*/','',open('theme/templates/'+tpl).read(),flags=re.S))['sections']['main']
    blocks=[dict(type=t['blocks'][i]['type'],settings=t['blocks'][i]['settings']) for i in t['block_order']]
    vs=[dict(id=1000+i,title=v[0],price=v[1],compare_at_price=0,available=True) for i,v in enumerate(variants)]
    cur=vs[0]
    prod=dict(title=title,variants=vs,selected_or_first_available_variant=cur,featured_media=None,media=[])
    sec=dict(id='main',settings=t['settings'],blocks=blocks)
    # settings missing keys default
    for k in ['hero_image','guarantee']: sec['settings'].setdefault(k,'')
    return env.from_string(src).render(product=prod,section=sec,form='x')

pages={
 'shower':build('product.lumova-shower.json','Lumova Hair-First Shower Filter',[('Starter Kit (filter head + 5 cartridges)',44.99),('Refill 3-Pack',19.99)]),
 'razor':build('product.lumova-razor.json','Lumova Single-Blade Safety Razor',[('Rose Gold + 10 blades',44.99)]),
}
for k,h in pages.items():
    open('mock_%s.html'%k,'w',encoding='utf8').write('<!doctype html><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"><body style="margin:0">'+h)
    print(k,len(h))
