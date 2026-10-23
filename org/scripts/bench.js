() => {
  const clean = x => x.innerText.trim().replace(/\s+/g, ' ');
  const t = sel => Array.from(document.querySelectorAll(sel)).map(clean).filter(x => x && x.length < 110);
  const uniq = a => Array.from(new Set(a));
  const body = document.body.innerText.toLowerCase();
  const keys = ['reviews','guarantee','subscribe','free shipping','as seen','dermatologist','clinically','bundle','money-back','tiktok','faq','ingredients','how it works','before','results','rated'];
  const flags = {};
  keys.forEach(k => { flags[k] = body.includes(k); });
  return {
    title: document.title.slice(0, 90),
    h1: uniq(t('h1')).slice(0, 2),
    h2: uniq(t('h2')).slice(0, 14),
    btn: uniq(t('a[class*=button],button[class*=button],a[class*=btn],button[class*=btn]')).slice(0, 10),
    flags: Object.keys(flags).filter(k => flags[k])
  };
}
