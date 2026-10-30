#!/usr/bin/env python3
"""elemix.ardasnturk.com statik sitesini üretir (İngilizce kök, Türkçe /tr/).

Çalıştırma: python3 build.py — sayfalar bu klasöre yazılır, yayınlamak için klasörün tamamı yeterli.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://elemix.ardasnturk.com"
APP_STORE = "https://apps.apple.com/app/id6828653495"
EMAIL = "support@ardasnturk.com"
UPDATED = {"en": "October 31, 2026", "tr": "31 Ekim 2026"}

APPLE = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.2 1.8-3.26 1.88-3.31'
         '-1.03-1.5-2.62-1.7-3.18-1.73-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.18-1.53 2.66-.39 6.6'
         ' 1.1 8.76.73 1.06 1.6 2.24 2.73 2.2 1.1-.05 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.84-1.22'
         ' 1.18-2.41 1.2-2.47-.03-.01-2.3-.88-2.32-3.5zM14.2 6.13c.6-.73 1.01-1.75.9-2.76-.87.04-1.92.58-2.54 1.31-.56.64-1.05'
         ' 1.68-.92 2.67.97.08 1.96-.49 2.56-1.22z"/></svg>')

T = {
    "en": {
        "lang": "en", "base": "/", "other": "/tr/", "other_label": "Türkçe",
        "nav": ("Privacy", "Support"),
        "title": "Elemix: Combine Elements",
        "desc": "A calm, clever element puzzle game for iPhone. Combine elements, drag the clock and set the temperature to create the target material.",
        "h1": "Mix the <em>elements</em>",
        "lead": "Water + fire = steam. Drag the clock and the thermometer to change the world, and create the target material in endless levels.",
        "cta": "Download on the App Store",
        "features": [
            ("💧", "Combine materials", "Drag one material onto another. 63 materials and 60 reactions to discover."),
            ("🌙", "Day and night", "Some reactions change with the time: earth + rain grows a plant by day and a mushroom by night."),
            ("🔥", "Temperature", "From -40 to 180 °C. Cross freezing or boiling and everything on the bench transforms at once."),
            ("🗺️", "Endless levels", "Generated levels, each one checked to be solvable, growing harder as you play."),
            ("⭐", "Stars and par", "Find the shortest solution and earn three stars."),
            ("📖", "Discovery book", "Every material and reaction you find is kept in your book."),
        ],
        "footer": "© 2026 Arda Senturk",
        "privacy": {
            "title": "Privacy Policy",
            "updated": "Last updated",
            "intro": "This policy explains what information the Elemix iPhone app (“Elemix”, “the app”) uses. Elemix is made by Arda Senturk. In short: Elemix has no accounts, no ads and no tracking, and your game progress stays on your device.",
            "sections": [
                ("Information we do not collect",
                 "<p>Elemix does not ask for your name, email address, contacts, location, photos or any other personal information. "
                 "The app contains no advertising and no analytics or tracking tools, and it does not track you across other apps or websites.</p>"),
                ("Game progress",
                 "<p>Your progress (levels, stars, discovered materials and your hint balance) is stored only on your device. "
                 "It is not sent to us. Deleting the app deletes this data.</p>"),
                ("In-app purchases",
                 "<p>Hint packs are sold as in-app purchases. Payment is handled entirely by Apple; we never see your payment details. "
                 "To validate purchases and credit hints, the app uses <strong>RevenueCat</strong>, a purchase-management service. "
                 "RevenueCat receives a random, anonymous app user ID created on your device, your purchase history for Elemix "
                 "(products, prices, dates, transaction IDs), and basic technical information such as the app version, device model, "
                 "operating system and country/storefront. This information is used only to make purchases work and is not used for advertising. "
                 "See <a href=\"https://www.revenuecat.com/privacy\">RevenueCat’s privacy policy</a> and "
                 "<a href=\"https://www.apple.com/legal/privacy/\">Apple’s privacy policy</a>.</p>"),
                ("Children",
                 "<p>Elemix is a general-audience puzzle game and is not directed specifically at children. We do not knowingly collect personal information from anyone, including children.</p>"),
                ("Your choices",
                 "<p>You can delete all game data at any time by deleting the app. For questions about purchase data held by RevenueCat, "
                 f"or any other privacy question, contact us at <a href=\"mailto:{EMAIL}\">{EMAIL}</a>.</p>"),
                ("Changes",
                 "<p>If this policy changes, the new version will be posted on this page with a new date.</p>"),
            ],
        },
        "support": {
            "title": "Support",
            "intro": f"Need help with Elemix? Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> and include your iPhone model and iOS version. We usually reply within a few days.",
            "faq": [
                ("How do I combine materials?", "Drag one card onto another, or tap two cards one after the other."),
                ("When do the clock and the thermometer unlock?", "The day/night clock on the left edge unlocks at level 4, the temperature slider on the right edge at level 8."),
                ("What does a hint do?", "A hint shows the next step of the shortest solution. New players get 3 hints; more can be bought in the hint shop (light bulb button)."),
                ("I bought hints but they did not arrive.", "Close and reopen the app while online: Elemix checks your purchases at launch and credits any hints that are missing. If they still do not appear, email us with the date of the purchase."),
                ("How do I get a refund?", "Refunds for App Store purchases are handled by Apple at reportaproblem.apple.com."),
                ("How do I change the language?", "Tap the globe button on the level map. It opens the iOS Settings page for Elemix, where you can choose the app language."),
            ],
        },
    },
    "tr": {
        "lang": "tr", "base": "/tr/", "other": "/", "other_label": "English",
        "nav": ("Gizlilik", "Destek"),
        "title": "Elemix: Element Birleştirme",
        "desc": "iPhone için sakin ama zekice bir element bulmacası. Elementleri birleştir, saati sürükle, sıcaklığı ayarla ve hedef malzemeyi yarat.",
        "h1": "Elementleri <em>karıştır</em>",
        "lead": "Su + ateş = buhar. Saati ve termometreyi sürükleyerek dünyayı değiştir, sonsuz bölümde hedef malzemeyi yarat.",
        "cta": "App Store'dan indir",
        "features": [
            ("💧", "Malzemeleri birleştir", "Bir malzemeyi diğerinin üzerine sürükle. Keşfedilecek 63 malzeme ve 60 tepkime."),
            ("🌙", "Gece ve gündüz", "Bazı tepkimeler saate göre değişir: toprak + yağmur gündüz bitki, gece mantar verir."),
            ("🔥", "Sıcaklık", "-40 ile 180 °C arası. Donma ya da kaynama noktasını geç, tezgahtaki her şey bir anda dönüşsün."),
            ("🗺️", "Sonsuz bölüm", "Her biri çözülebilir olduğu doğrulanan, oynadıkça zorlaşan bölümler."),
            ("⭐", "Yıldız ve par", "En kısa çözümü bul, üç yıldızı al."),
            ("📖", "Keşif defteri", "Bulduğun her malzeme ve tepkime defterinde kalır."),
        ],
        "footer": "© 2026 Arda Senturk",
        "privacy": {
            "title": "Gizlilik Politikası",
            "updated": "Son güncelleme",
            "intro": "Bu politika, Elemix iPhone uygulamasının (“Elemix”, “uygulama”) hangi bilgileri kullandığını açıklar. Elemix, Arda Senturk tarafından geliştirilmiştir. Kısaca: Elemix'te hesap, reklam ve takip yoktur; oyun ilerlemen cihazında kalır.",
            "sections": [
                ("Toplamadığımız bilgiler",
                 "<p>Elemix adını, e-posta adresini, kişilerini, konumunu, fotoğraflarını ya da başka bir kişisel bilgini istemez. "
                 "Uygulamada reklam, analiz ya da takip aracı yoktur; seni başka uygulama ve web sitelerinde takip etmez.</p>"),
                ("Oyun ilerlemesi",
                 "<p>İlerlemen (bölümler, yıldızlar, keşfedilen malzemeler ve ipucu bakiyen) yalnızca cihazında saklanır, bize gönderilmez. "
                 "Uygulamayı silmek bu verileri de siler.</p>"),
                ("Uygulama içi satın almalar",
                 "<p>İpucu paketleri uygulama içi satın alma ile satılır. Ödemeyi tamamen Apple yapar; ödeme bilgilerini hiçbir zaman görmeyiz. "
                 "Satın almaları doğrulamak ve ipuçlarını eklemek için uygulama bir satın alma yönetim hizmeti olan <strong>RevenueCat</strong>'i kullanır. "
                 "RevenueCat'e cihazında oluşturulan rastgele ve anonim bir uygulama kullanıcı kimliği, Elemix'teki satın alma geçmişin "
                 "(ürünler, fiyatlar, tarihler, işlem kimlikleri) ve uygulama sürümü, cihaz modeli, işletim sistemi ve ülke/mağaza gibi temel teknik bilgiler iletilir. "
                 "Bu bilgiler yalnızca satın almaların çalışması için kullanılır, reklam amacıyla kullanılmaz. "
                 "<a href=\"https://www.revenuecat.com/privacy\">RevenueCat gizlilik politikası</a> ve "
                 "<a href=\"https://www.apple.com/tr/legal/privacy/\">Apple gizlilik politikası</a>.</p>"),
                ("Çocuklar",
                 "<p>Elemix genel kitleye yönelik bir bulmaca oyunudur, özellikle çocuklara yönelik değildir. Çocuklar dahil kimseden bilerek kişisel bilgi toplamayız.</p>"),
                ("Seçeneklerin",
                 "<p>Uygulamayı silerek tüm oyun verilerini istediğin an silebilirsin. RevenueCat'teki satın alma verileri ya da başka bir gizlilik sorusu için "
                 f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a> adresine yaz.</p>"),
                ("Değişiklikler",
                 "<p>Bu politika değişirse yeni sürüm bu sayfada yeni tarihle yayınlanır.</p>"),
            ],
        },
        "support": {
            "title": "Destek",
            "intro": f"Elemix ile ilgili yardıma mı ihtiyacın var? iPhone modelini ve iOS sürümünü de yazarak <a href=\"mailto:{EMAIL}\">{EMAIL}</a> adresine e-posta gönder. Genellikle birkaç gün içinde yanıt veririz.",
            "faq": [
                ("Malzemeleri nasıl birleştiririm?", "Bir kartı diğerinin üzerine sürükle ya da iki karta sırayla dokun."),
                ("Saat ve termometre ne zaman açılır?", "Sol kenardaki gece-gündüz saati 4. bölümde, sağ kenardaki sıcaklık kaydırıcısı 8. bölümde açılır."),
                ("İpucu ne işe yarar?", "İpucu en kısa çözümün sıradaki adımını gösterir. Yeni oyuncular 3 ipucuyla başlar; daha fazlası ipucu mağazasından (ampul düğmesi) alınabilir."),
                ("İpucu satın aldım ama gelmedi.", "İnternete bağlıyken uygulamayı kapatıp yeniden aç: Elemix açılışta satın almalarını kontrol eder ve eksik ipuçlarını ekler. Yine görünmezse satın alma tarihiyle birlikte bize yaz."),
                ("Nasıl iade alırım?", "App Store satın almalarının iadesini Apple, reportaproblem.apple.com adresinden yapar."),
                ("Dili nasıl değiştiririm?", "Bölüm haritasındaki dünya düğmesine dokun. iOS Ayarlar'da Elemix sayfası açılır, oradan uygulama dilini seçebilirsin."),
            ],
        },
    },
}


def page(t, path, title, body, desc=None):
    canon = SITE + path
    alt = {"en": path.replace("/tr/", "/", 1) if path.startswith("/tr/") else path,
           "tr": path if path.startswith("/tr/") else "/tr" + path}
    privacy, support = t["nav"]
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc or t["desc"]}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{SITE}{alt["en"]}">
<link rel="alternate" hreflang="tr" href="{SITE}{alt["tr"]}">
<meta name="apple-itunes-app" content="app-id=6828653495">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc or t["desc"]}">
<meta property="og:image" content="{SITE}/assets/icon.png">
<meta name="theme-color" content="#0b1030">
<link rel="icon" href="/assets/icon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="{t["base"]}"><img src="/assets/icon.png" alt="">Elemix</a>
  <nav><a href="{t["base"]}privacy/">{privacy}</a><a href="{t["base"]}support/">{support}</a><a href="{alt["tr"] if t["lang"] == "en" else alt["en"]}">{t["other_label"]}</a></nav>
</header>
{body}
<footer><span>{t["footer"]}</span><span class="sp"></span><a href="{t["base"]}privacy/">{privacy}</a><a href="{t["base"]}support/">{support}</a><a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</div>
</body>
</html>
'''


def landing(t, shots):
    feats = "".join(f'<div class="feature"><div class="emoji">{e}</div><h3>{h}</h3><p>{p}</p></div>' for e, h, p in t["features"])
    gallery = "".join(f'<img src="/assets/shots/{shots}/{n:02d}.jpg" alt="" loading="lazy">' for n in range(1, 7))
    body = f'''<section class="hero">
  <div>
    <img class="icon" src="/assets/icon.png" alt="Elemix">
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <a class="cta" href="{APP_STORE}">{APPLE}{t["cta"]}</a>
  </div>
  <img class="shot" src="/assets/shots/{shots}/01.jpg" alt="">
</section>
<section class="features">{feats}</section>
<section class="gallery">{gallery}</section>'''
    return page(t, t["base"], t["title"], body)


def privacy(t):
    p = t["privacy"]
    secs = "".join(f"<h2>{h}</h2>{b}" for h, b in p["sections"])
    body = f'''<article class="doc">
<h1>{p["title"]}</h1>
<div class="date">{p["updated"]}: {UPDATED[t["lang"]]}</div>
<p>{p["intro"]}</p>
{secs}
</article>'''
    return page(t, t["base"] + "privacy/", f'{p["title"]} · Elemix', body, p["intro"][:150])


def support(t):
    s = t["support"]
    faq = "".join(f'<div class="box"><h3>{q}</h3><p>{a}</p></div>' for q, a in s["faq"])
    body = f'''<article class="doc">
<h1>{s["title"]}</h1>
<p>{s["intro"]}</p>
{faq}
</article>'''
    return page(t, t["base"] + "support/", f'{s["title"]} · Elemix', body)


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)


def main():
    for lang, shots, prefix in (("en", "en-US", ""), ("tr", "tr", "tr/")):
        t = T[lang]
        write(prefix + "index.html", landing(t, shots))
        write(prefix + "privacy/index.html", privacy(t))
        write(prefix + "support/index.html", support(t))
    write("CNAME", "elemix.ardasnturk.com\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = ["/", "/privacy/", "/support/", "/tr/", "/tr/privacy/", "/tr/support/"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print("ok")


if __name__ == "__main__":
    main()
