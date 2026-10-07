# Kullanım: python3 make_product_pages.py https://ADRES   -> site/urun/NN.html sayfalarını üretir
import sys, os, re, html
base=sys.argv[1].rstrip('/')
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(root,'index.html'),encoding='utf-8').read()
items=re.findall(r'data-no="(\d\d)" data-name="([^"]+)" href', src)
num=re.search(r'WHATSAPP_NUMBER = "(\d+)"',src).group(1)
os.makedirs(os.path.join(root,'urun'),exist_ok=True)
for no,name in dict(items).items():
    t=f"{name} · AHİ.3D"; img=f"{base}/urunler/og/urun-{no}.jpg"
    msg=f"Merhaba AHİ.3D, sitenizdeki {no} numaralı ürün ({name}) hakkında fiyat almak istiyorum.\n{base}/urun/{no}.html"
    from urllib.parse import quote
    open(os.path.join(root,'urun',f'{no}.html'),'w',encoding='utf-8').write(f'''<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta property="og:title" content="{html.escape(t)}">
<meta property="og:description" content="No. {no} · AHİ.3D 3D Baskı ve Tasarım Atölyesi">
<meta property="og:image" content="{img}"><meta property="">
<meta property="og:url" content="{base}/urun/{no}.html"><meta property="og:type" content="product">
<style>body{{margin:0;background:#0b241f;color:#eef4ec;font-family:system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;padding:16px;box-sizing:border-box}}main{{max-width:34rem;width:100%;text-align:center}}img{{width:100%;border-radius:16px}}a{{display:inline-block;margin:12px 6px 0;padding:12px 20px;border-radius:999px;text-decoration:none;font-weight:600}}.wa{{background:#1fa855;color:#fff}}.back{{border:1.5px solid #4d6b5e;color:#eef4ec}}small{{color:#a9c98a;font-family:monospace}}</style></head>
<body><main><img src="../urunler/orijinal/urun-{no}.webp" alt="{html.escape(name)}"><p><small>No. {no}</small><br><strong>{html.escape(name)}</strong></p>
<a class="wa" href="https://wa.me/{num}?text={quote(msg)}">WhatsApp'tan fiyat sor</a><a class="back" href="../index.html#urunler">Tüm ürünler</a></main></body></html>''')
print('ok', len(dict(items)))
