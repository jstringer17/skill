import re,sys,subprocess
q=sys.argv[1]
slug=q.replace(' ','-')
u=f"https://www.aliexpress.com/w/wholesale-{slug}.html"
s=subprocess.run(['curl','-sSL','-m','30','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
parts=re.split(r'"productId":"(\d+)"',s)
rows=[]
for i in range(1,len(parts),2):
    pid=parts[i]; ch=parts[i+1][:4000]
    t=re.search(r'"displayTitle":"([^"]+)"',ch)
    p=re.search(r'"formattedPrice":"([^"]+)"',ch)
    sold=re.search(r'"tradeDesc":"([^"]+)"',ch)
    rt=re.search(r'"starRating":"?([\d.]+)',ch)
    rows.append((pid,(t.group(1) if t else '')[:60],p.group(1) if p else '',sold.group(1) if sold else '',rt.group(1) if rt else ''))
def n(x):
    m=re.match(r'([\d,]+)\+?',x); return int(m.group(1).replace(',','')) if m else 0
rows.sort(key=lambda r:-n(r[3]))
print('==',q,len(s),len(rows))
for r in rows[:4]: print(r)
