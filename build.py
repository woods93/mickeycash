#!/usr/bin/env python3
"""Builds index.html for the Mickey Cash site. Run: python3 build.py"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- Settings -------------------------------------------------------------
NAME = "Mickey Cash"
EMAIL_USER, EMAIL_DOMAIN = "Mickeycashband", "live.com"
WEB3FORMS_KEY = ""            # paste the Web3Forms access key here when it exists
APPLE_MUSIC = "https://music.apple.com/us/artist/mickey-cash/595830439"
ALLMUSIC = "https://www.allmusic.com/artist/mickey-cash-mn0003063108"
ALLMUSIC_ALBUM = "https://www.allmusic.com/album/victory-mw0002489502"
YT_CHANNEL = "https://www.youtube.com/@OFFICIALMICKEYCASH"
STAUG = "https://www.visitstaugustine.com/musician/mickey-cash"
# Fourthwall shop address. Leave "" until the shop exists; the Shop section then says "coming soon".
SHOP_URL = ""

# Drop files into assets/images and assets/audio, then list them here.
HERO_IMAGE = "assets/images/hero.jpg"          # used only if the file exists
VICTORY_COVER = "assets/images/victory-cover.jpg"   # used only if the file exists
AUDIO = []   # e.g. [("Ashes By Now", "assets/audio/ashes-by-now.mp3")]

VIDEOS = [
    ("LC9brvHXmgU", "Victory", "Official music video. Video by LollieVox and Camille Alvey."),
    ("0_runBpp8V8", "Mr. Bojangles", "Official music video, filmed in Richmond, Virginia."),
    ("grfxIWPjE_w", "Victory", "Official single."),
]
PRESS_VIDEO = ("sSo7vi6T3js", "Richmond Times-Dispatch", "Mickey sings “Mr. Bojangles” in a newspaper feature.")

TRACKS = [
    ("Ashes By Now", "4:56"), ("Things Are Gonna Get Better", "3:09"),
    ("Long Long Road", "3:54"), ("Ring of Fire", "3:18"),
    ("Victory", "4:40"), ("End of the Line", "4:02"), ("Rocky World", "3:50"),
]

def e(s): return html.escape(s, quote=True)

def exists(rel): return os.path.exists(os.path.join(ROOT, rel))

def lite(vid, title):
    return f'''<button class="yt" type="button" data-id="{vid}" aria-label="Play video: {e(title)}">
  <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
  <span class="play" aria-hidden="true"></span>
</button>'''

def video_card(v):
    vid, title, note = v
    return f'<figure class="video">{lite(vid, title)}<figcaption><strong>{e(title)}</strong><span>{e(note)}</span></figcaption></figure>'

hero_media = (f'<img class="portrait" src="{HERO_IMAGE}" alt="Mickey Cash" width="800" height="1000">'
              if exists(HERO_IMAGE) else '')
hero_cls = "hero has-photo" if hero_media else "hero"

audio_block = ""
if AUDIO:
    items = "".join(f'<li><span>{e(t)}</span><audio controls preload="none" src="{e(p)}"></audio></li>' for t, p in AUDIO)
    audio_block = f'<h3>Listen</h3><ul class="audio">{items}</ul>'

cover = (f'<img class="cover" src="{VICTORY_COVER}" alt="Victory album cover" width="400" height="400">'
         if exists(VICTORY_COVER) else '')

tracks_html = "".join(f'<li><span>{e(t)}</span><span>{d}</span></li>' for t, d in TRACKS)

shop_html = (f'<p>Official Mickey Cash merch.</p><p><a class="btn" href="{SHOP_URL}" target="_blank" rel="noopener">Visit the shop</a></p>'
             if SHOP_URL else '<p>Mickey Cash merch is on its way. Check back soon.</p>')
key_attr = e(WEB3FORMS_KEY)

PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mickey Cash — Americana &amp; Alt-Country Singer-Songwriter</title>
<meta name="description" content="Mickey Cash is an Americana and alt-country singer-songwriter with a powerful, resonant voice. Watch videos, see the Victory album, and get in touch for booking.">
<meta property="og:title" content="Mickey Cash">
<meta property="og:description" content="Americana and alt-country singer-songwriter. Watch, listen, and book.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&family=Playfair+Display:wght@700;900&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="brand" href="#top">Mickey Cash</a>
  <nav aria-label="Main"><ul>
    <li><a href="#bio">Bio</a></li>
    <li><a href="#watch">Watch &amp; Listen</a></li>
    <li><a href="#music">Music</a></li>
    <li><a href="#press">Press</a></li>
    <li><a href="#shop">Shop</a></li>
    <li><a href="#contact">Booking</a></li>
  </ul></nav>
</header>
<main id="main">

<section id="top" class="{hero_cls}">
  <div class="hero-text">
    <p class="kicker">Americana · Alt-Country · Singer-Songwriter</p>
    <h1>Mickey<br>Cash</h1>
    <p class="lede">Old-time country, Americana, and rock, sung with a big, resonant voice.</p>
    <p><a class="btn" href="#watch">Watch &amp; listen</a> <a class="btn ghost" href="#contact">Book Mickey</a></p>
  </div>
  {hero_media}
</section>

<section id="bio">
  <h2>Bio</h2>
  <div class="prose">
    <p>Mickey Cash is an Americana and alt-country singer-songwriter with a big, resonant voice. She blends old-time and modern country with rock, and Janis Joplin is one of her influences.</p>
    <p>She comes from the Cash family. Her debut album, <em>Victory</em>, came out in 2013 and features Nashville studio musicians. She has lived and played in St. Augustine and Nashville, and in 2024 she moved back to her home state of Virginia.</p>
  </div>
</section>

<section id="watch">
  <h2>Watch &amp; Listen</h2>
  <div class="videos">{"".join(video_card(v) for v in VIDEOS)}</div>
  {audio_block}
  <p class="more"><a href="{YT_CHANNEL}" target="_blank" rel="noopener">More on Mickey’s YouTube channel →</a></p>
</section>

<section id="music">
  <h2>Music</h2>
  <div class="album">
    {cover}
    <div>
      <h3><em>Victory</em> <span class="year">2013</span></h3>
      <p class="small">7 tracks · 27:49</p>
      <ol class="tracks">{tracks_html}</ol>
      <p class="stream">
        <a href="{APPLE_MUSIC}" target="_blank" rel="noopener">Apple Music</a>
        <a href="{ALLMUSIC_ALBUM}" target="_blank" rel="noopener">AllMusic</a>
        <a href="{YT_CHANNEL}" target="_blank" rel="noopener">YouTube</a>
      </p>
    </div>
  </div>
  <h3>Also appears on</h3>
  <p><em>Mighty</em> — Ty Smth feat. ZellBo &amp; Mickey Cash (2020)</p>
</section>

<section id="press">
  <h2>Press &amp; Features</h2>
  <div class="press">
    <div>
      <h3>Richmond Times-Dispatch</h3>
      {lite(PRESS_VIDEO[0], PRESS_VIDEO[1])}
      <p class="small">{e(PRESS_VIDEO[2])}</p>
    </div>
    <div>
      <h3>Visit St. Augustine</h3>
      <p>Artist feature on the city’s official visitor site, covering Mickey’s voice, her Cash family roots, and her cover of “Ring of Fire.”</p>
      <p><a href="{STAUG}" target="_blank" rel="noopener">Read the feature →</a></p>
      <h3>AllMusic</h3>
      <p><a href="{ALLMUSIC}" target="_blank" rel="noopener">Artist profile →</a></p>
    </div>
  </div>
</section>

<section id="shop">
  <h2>Shop</h2>
  {shop_html}
</section>

<section id="contact">
  <h2>Booking &amp; Contact</h2>
  <p>For booking, press, and everything else, write to <a class="mail" data-u="{EMAIL_USER}" data-d="{EMAIL_DOMAIN}" href="#contact">email</a>, or use the form.</p>
  <form id="contact-form" class="form" action="https://api.web3forms.com/submit" method="POST" data-key="{key_attr}">
    <input type="hidden" name="access_key" value="{key_attr}">
    <input type="hidden" name="subject" value="New message from the Mickey Cash website">
    <input type="hidden" name="from_name" value="Mickey Cash website">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <label>Name <input name="name" required autocomplete="name"></label>
    <label>Email <input type="email" name="email" required autocomplete="email"></label>
    <label>Message <textarea name="message" rows="5" required></textarea></label>
    <button class="btn" type="submit">Send</button>
    <p class="form-status" role="status"></p>
  </form>
</section>

</main>
<footer class="foot">© <span id="yr">2026</span> Mickey Cash</footer>
<script src="js/site.js"></script>
</body>
</html>
'''

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print("wrote index.html", len(PAGE), "bytes")
