import json,re,xml.etree.ElementTree as ET
from playwright.sync_api import sync_playwright
B="http://localhost:8765/"
locs=[l[0].text.split("wastetrackingfinder.co.uk/")[1] for l in ET.parse("sitemap.xml").getroot()]
errs=[];bad=[]
with sync_playwright() as p:
  br=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-proxy-server"])
  for w,h in((390,844),(1366,900)):
    pg=br.new_page(viewport={"width":w,"height":h})
    pg.on("pageerror",lambda e:errs.append(str(e)));pg.on("console",lambda m:m.type=="error" and errs.append(m.text))
    for u in locs+["404.html"]:
      r=pg.goto(B+u)
      if r.status!=200:bad.append((u,r.status))
      for s in pg.locator('script[type="application/ld+json"]').all_inner_texts():json.loads(s)
      if pg.evaluate("document.documentElement.scrollWidth")>w+1:bad.append((u,w,"overflow"))
    pg.goto(B);tag=f"{w}"
    pg.screenshot(path=f"shots/home-{tag}.png")
    if w==390:pg.click(".filter-toggle")
    pg.check("input[value=skip-hire]");a=pg.inner_text("#count");pg.check("input[name=price]");b=pg.inner_text("#count");pg.fill("#q","zzzz");c=pg.inner_text("#count")
    print(w,"skip",a,"skip+price",b,"nonsense",c)
    pg.fill("#q","");pg.uncheck("input[name=price]");pg.screenshot(path=f"shots/home-filter-skip-{tag}.png",full_page=False)
    for u,n in(("software/breakerhq/","vendor"),("carriers-brokers-dealers-2027/","guide-2027"),("penalties/","penalties"),("other-not-yet-categorised/","other")):
      pg.goto(B+u);pg.screenshot(path=f"shots/{n}-{tag}.png")
  br.close()
print("pages",len(locs),"bad",bad,"errors",errs[:5])
