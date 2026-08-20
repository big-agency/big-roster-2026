# -*- coding: utf-8 -*-
import json, os, re

HERE = os.path.dirname(__file__)
people = json.load(open(os.path.join(HERE, "people.json")))
fonts = json.load(open(os.path.join(HERE, "fonts.json")))

FONDO_SVG_RAW = open("/Users/tomascardozo/main/big/web/vectorfondo.svg").read()
FONDO_INNER = re.search(r"<svg[^>]*>(.*)</svg>", FONDO_SVG_RAW, re.S).group(1)
FONDO_VIEWBOX = re.search(r'viewBox="([^"]+)"', FONDO_SVG_RAW).group(1)

# canonical BIG logo — always source the isotipo from this file
LOGO_SVG_RAW = open("/Users/tomascardozo/main/big/brand/nuevo/big-logo2.svg").read()
ISOTIPO_PATH = re.search(r'\sd="([^"]+)"', LOGO_SVG_RAW).group(1)
ISOTIPO_VIEWBOX = re.search(r'viewBox="([^"]+)"', LOGO_SVG_RAW).group(1)

CATEGORIES = ["Mujeres", "Hombres", "Lifestyle", "Beauty & Makeup", "Trends", "Fitness",
              "Humor & Sketches", "Entretenimiento", "Foodie", "Youtube", "Tecnología & Crypto"]

# maca_castro and ammichis excluded from every roster appearance (client request)
SECTIONS = [
    dict(
        slug="mujeres", name="Mujeres", split=("Muje", "res"),
        subtitle="Moda, humor y estilo de vida — las creadoras que más conectan con sus audiencias en cada plataforma.",
        collage=["juli_savioli", "pauli_veltrano", "sabri_ludmila"],
        order=["juli_savioli", "pia_scarnato", "dulce_pink", "renata_blasevich", "giuli_bellicoso",
               "pauli_veltrano", "agustina_cambra", "eve_vidal", "inez", "mumy",
               "giuli_lourdes", "mely_francano", "martu_morales", "nanu_yael", "sabri_ludmila", "yo_soy_brisa"],
    ),
    dict(
        slug="trends", name="Trends", split=("Tren", "ds"),
        subtitle="Contenido que se mueve rápido: humor, moda y cultura pop, directo al feed de audiencias que marcan tendencia.",
        collage=["pia_scarnato", "giuli_lourdes", "martu_morales"],
        order=["pia_scarnato", "dulce_pink", "giuli_bellicoso", "giuli_lourdes",
               "mely_francano", "martu_morales", "tiago_bergallo"],
    ),
]

def isotipo_svg(size=28, color="#FFFFFF", cls=""):
    return f'<svg class="{cls}" width="{size}" height="{size}" viewBox="{ISOTIPO_VIEWBOX}" style="color:{color}"><path fill="currentColor" d="{ISOTIPO_PATH}"/></svg>'

# icon glyphs from the "Tarjeta Talento — Dark" Figma component (node 89:242) — durazno
# glyph on a lima-16%-opacity rounded square, tuned for the azul card background only
IG_ICON_SVG = '''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="20" height="20" rx="7" fill="#E8F29C" fill-opacity="0.16"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M10 13C11.6568 13 13 11.6568 13 10C13 8.34315 11.6568 7 10 7C8.34315 7 7 8.34315 7 10C7 11.6568 8.34315 13 10 13ZM10 12C11.1046 12 12 11.1046 12 10C12 8.89543 11.1046 8 10 8C8.89543 8 8 8.89543 8 10C8 11.1046 8.89543 12 10 12Z" fill="#F7D8BD"/>
<path d="M13 6.5C12.7239 6.5 12.5 6.72386 12.5 7C12.5 7.27614 12.7239 7.5 13 7.5C13.2762 7.5 13.5 7.27614 13.5 7C13.5 6.72386 13.2762 6.5 13 6.5Z" fill="#F7D8BD"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M4.82698 6.13803C4.5 6.77977 4.5 7.61985 4.5 9.3V10.7C4.5 12.3801 4.5 13.2202 4.82698 13.8619C5.1146 14.4264 5.57354 14.8854 6.13803 15.173C6.77977 15.5 7.61985 15.5 9.3 15.5H10.7C12.3801 15.5 13.2202 15.5 13.8619 15.173C14.4264 14.8854 14.8854 14.4264 15.173 13.8619C15.5 13.2202 15.5 12.3801 15.5 10.7V9.3C15.5 7.61985 15.5 6.77977 15.173 6.13803C14.8854 5.57354 14.4264 5.1146 13.8619 4.82698C13.2202 4.5 12.3801 4.5 10.7 4.5H9.3C7.61985 4.5 6.77977 4.5 6.13803 4.82698C5.57354 5.1146 5.1146 5.57354 4.82698 6.13803ZM10.7 5.5H9.3C8.44342 5.5 7.86113 5.50078 7.41104 5.53755C6.97262 5.57337 6.74842 5.6383 6.59202 5.71799C6.2157 5.90974 5.90974 6.2157 5.71799 6.59202C5.6383 6.74842 5.57337 6.97262 5.53755 7.41104C5.50078 7.86113 5.5 8.44342 5.5 9.3V10.7C5.5 11.5566 5.50078 12.1388 5.53755 12.5889C5.57337 13.0274 5.6383 13.2516 5.71799 13.408C5.90974 13.7843 6.2157 14.0902 6.59202 14.282C6.74842 14.3617 6.97262 14.4267 7.41104 14.4625C7.86113 14.4992 8.44342 14.5 9.3 14.5H10.7C11.5566 14.5 12.1388 14.4992 12.5889 14.4625C13.0274 14.4267 13.2516 14.3617 13.408 14.282C13.7843 14.0902 14.0902 13.7843 14.282 13.408C14.3617 13.2516 14.4267 13.0274 14.4625 12.5889C14.4992 12.1388 14.5 11.5566 14.5 10.7V9.3C14.5 8.44342 14.4992 7.86113 14.4625 7.41104C14.4267 6.97262 14.3617 6.74842 14.282 6.59202C14.0902 6.2157 13.7843 5.90974 13.408 5.71799C13.2516 5.6383 13.0274 5.57337 12.5889 5.53755C12.1388 5.50078 11.5566 5.5 10.7 5.5Z" fill="#F7D8BD"/>
</svg>'''

TT_ICON_SVG = '''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="20" height="20" rx="7" fill="#E8F29C" fill-opacity="0.16"/>
<path d="M12.9314 6.22392C12.5107 5.76167 12.2578 5.15893 12.2578 4.5H11.7306C11.8664 5.22023 12.3137 5.83829 12.9314 6.22392Z" fill="#F7D8BD"/>
<path d="M8.05382 9.94764C7.14061 9.94764 6.3978 10.6602 6.3978 11.5362C6.3978 12.1467 6.75989 12.6778 7.28704 12.9434C7.09003 12.683 6.97288 12.3637 6.97288 12.0164C6.97288 11.1404 7.71569 10.4278 8.62891 10.4278C8.7993 10.4278 8.96435 10.4558 9.11879 10.5018V8.57106C8.95902 8.5506 8.79663 8.53782 8.62891 8.53782C8.59961 8.53782 8.57299 8.54038 8.5437 8.54038V10.0217C8.38662 9.97569 8.22421 9.94764 8.05382 9.94764Z" fill="#F7D8BD"/>
<path d="M14.4249 7.07184V8.54038C13.4026 8.54038 12.4548 8.22626 11.6826 7.69501V11.5387C11.6826 13.4568 10.0559 15.0199 8.05377 15.0199C7.28168 15.0199 6.56283 14.7849 5.97444 14.389C6.63737 15.0709 7.58253 15.5 8.62887 15.5C10.6283 15.5 12.2577 13.9395 12.2577 12.0189V8.17516C13.0298 8.70641 13.9776 9.02051 15 9.02051V7.13061C14.8003 7.13061 14.6086 7.11016 14.4249 7.07184Z" fill="#F7D8BD"/>
<path d="M11.6826 11.5387V7.69501C12.4548 8.22626 13.4026 8.54038 14.4249 8.54038V7.07184C13.8339 6.95183 13.3148 6.64535 12.9314 6.22392C12.3137 5.83829 11.869 5.22023 11.7279 4.5H10.2849L10.2822 12.0776C10.2503 12.9256 9.52076 13.6075 8.62887 13.6075C8.07507 13.6075 7.58785 13.3444 7.28434 12.946C6.75718 12.6778 6.3951 12.1492 6.3951 11.5387C6.3951 10.6628 7.13791 9.95017 8.05111 9.95017C8.2215 9.95017 8.38657 9.97828 8.541 10.0243V8.54293C6.58147 8.5838 5 10.1264 5 12.0189C5 12.9332 5.37008 13.7658 5.97444 14.389C6.56283 14.7849 7.28168 15.0199 8.05377 15.0199C10.0532 15.0199 11.6826 13.4568 11.6826 11.5387Z" fill="#F7D8BD"/>
</svg>'''

def tabs_html():
    out = []
    for cat in CATEGORIES:
        out.append(f'<button class="tab" data-cat="{cat}">{cat}</button>')
    return "\n".join(out)

def card_html(pid, i):
    p = people[pid]
    tags = "".join(f'<span class="chip">{t}</span>' for t in p["tags"])
    return f'''
    <article class="card" style="--i:{i}">
      <img class="card-photo" src="{p["photo"]}" alt="{p["name"]}" loading="lazy" decoding="async" width="250" height="250">
      <div class="card-body">
        <h3 class="card-name">{p["name"]}</h3>
        <div class="chip-row">{tags}</div>
        <div class="stat-row">
          <a class="stat" href="{p["ig_url"]}" target="_blank" rel="noopener"><span class="stat-label">Instagram</span><span class="stat-value">{p["ig"]}</span></a>
          <a class="stat" href="{p["tt_url"]}" target="_blank" rel="noopener"><span class="stat-label">TikTok</span><span class="stat-value">{p["tt"]}</span></a>
        </div>
      </div>
    </article>'''

MEDIAKIT_READY = {"agustina_cambra"}  # only pid with a real mediakit.html so far

def _ver_mas_link(pid, name, cls):
    if pid in MEDIAKIT_READY:
        return f'<a class="{cls}" href="mediakit.html?id={pid}">Ver más</a>'
    return f'<a class="{cls} {cls}-toast" href="#" data-name="{name}">Ver más</a>'

def _follower_num(s):
    s = s.strip().upper()
    mult = 1_000_000 if s.endswith("M") else 1_000 if s.endswith("K") else 1
    try:
        return float(s[:-1].strip() if mult > 1 else s) * mult
    except ValueError:
        return 0

def card_html_talent_dark(pid, i):
    """'Tarjeta Talento — Dark' (Figma node 86:357), trial run on Mujeres only."""
    p = people[pid]
    subtitle = " · ".join(p["tags"])
    btn = _ver_mas_link(pid, p["name"], "tcard-btn").replace(">Ver más<", ">Ver más <span>→</span><")
    return f'''
    <article class="tcard" style="--i:{i}">
      <img class="tcard-photo" src="{p["photo"]}" alt="{p["name"]}" loading="lazy" decoding="async" width="268" height="300">
      <div class="tcard-body">
        <div class="tcard-name-row">
          <h3 class="tcard-name">{p["name"]}</h3>
          <span class="tcard-badge" aria-hidden="true">✓</span>
        </div>
        <p class="tcard-subtitle">{subtitle}</p>
        <div class="tcard-bottom">
          <div class="tcard-stats">
            <a class="tcard-stat" href="{p["ig_url"]}" target="_blank" rel="noopener">{IG_ICON_SVG}<span>{p["ig"]}</span></a>
            <a class="tcard-stat" href="{p["tt_url"]}" target="_blank" rel="noopener">{TT_ICON_SVG}<span>{p["tt"]}</span></a>
          </div>
          {btn}
        </div>
      </div>
    </article>'''

def card_html_clean_blur(pid, i):
    """'Tarjeta Talento — Clean Blur' (Figma node 86:359): full-bleed photo, blurred scrims."""
    p = people[pid]
    role = " · ".join(p["tags"])
    top_stat = p["ig"] if _follower_num(p["ig"]) >= _follower_num(p["tt"]) else p["tt"]
    handle = p["ig_url"].rstrip("/").rsplit("/", 1)[-1]
    btn = _ver_mas_link(pid, p["name"], "bcard-btn")
    return f'''
    <article class="bcard" style="--i:{i}">
      <img class="bcard-photo" src="{p["photo"]}" alt="{p["name"]}" loading="lazy" decoding="async" width="307" height="527">
      <div class="bcard-top-scrim" aria-hidden="true"></div>
      <div class="bcard-top">
        <h3 class="bcard-name">{p["name"]}</h3>
        <span class="bcard-pill">{top_stat} seguidores</span>
      </div>
      <div class="bcard-bottom">
        <div class="bcard-identity">
          <img class="bcard-avatar" src="{p["photo"]}" alt="" loading="lazy" decoding="async" width="34" height="34">
          <div class="bcard-id-text">
            <span class="bcard-handle">@{handle}</span>
            <span class="bcard-role">{role}</span>
          </div>
        </div>
        {btn}
      </div>
    </article>'''

def collage_html(ids):
    return "".join(
        f'<img class="collage-tile ct-{i+1}" src="{people[cid]["photo"]}" alt="{people[cid]["name"]}" loading="lazy" decoding="async">'
        for i, cid in enumerate(ids)
    )

def category_section(cat, active):
    slug = cat["slug"]
    head, tail = cat["split"]
    renderer = card_html_clean_blur if slug == "mujeres" else card_html
    cards = "".join(renderer(pid, i) for i, pid in enumerate(cat["order"]))
    active_cls = " active-cat" if active else ""
    return f'''
  <section class="category{active_cls}" data-cat="{cat["name"]}" data-slug="{slug}" id="cat-{slug}">
    <div class="cat-cover">
      <div class="section-inner">
        <div>
          <h1>{head}{tail}</h1>
          <p>{cat["subtitle"]}</p>
        </div>
        <div class="cat-collage">
          {collage_html(cat["collage"])}
        </div>
      </div>
    </div>
    <div class="cat-rail">
      <div class="rail-head">
        <div class="rail-eyebrow">{len(cat["order"])} creadores en nuestro equipo</div>
      </div>
      <div class="rail-wrap">
        <button class="rail-arrow prev" aria-label="Anterior">‹</button>
        <button class="rail-arrow next" aria-label="Siguiente">›</button>
        <div class="rail" tabindex="0" role="region" aria-label="Creadores de {cat["name"]}, deslizar con las flechas del teclado">
          {cards}
        </div>
      </div>
      <div class="progress-track">
        <div class="progress-bar"><div class="progress-fill"></div></div>
      </div>
    </div>
  </section>'''

font_faces = "\n".join(f'''
@font-face {{
  font-family: 'Inter';
  font-weight: {w};
  font-style: normal;
  src: url(data:font/woff2;base64,{fonts[name]}) format('woff2');
  font-display: swap;
}}''' for name, w in [("Regular", 400), ("Medium", 500), ("Bold", 700), ("Black", 900)])

def fondo_svg():
    return f'<svg viewBox="{FONDO_VIEWBOX}" preserveAspectRatio="xMidYMid slice">{FONDO_INNER}</svg>'

sections_html = "\n".join(category_section(cat, active=(i == 0)) for i, cat in enumerate(SECTIONS))
first_slug = SECTIONS[0]["slug"]
slug_map = json.dumps({cat["name"]: cat["slug"] for cat in SECTIONS})

html = f'''<title>BIG Roster 2026 — Prototipo</title>
<style>
{font_faces}

:root {{
  --azul: #33419A;
  --azul-2: #4C5AB8;
  --azul-dark: #262F73;
  --naranja: #F36F2C;
  --fondo: #F7D8BD;
  --lima: #E8F29C;
  --negro: #0D0D14;
  --blanco: #FFFFFF;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--fondo);
  color: var(--azul);
  overflow-x: hidden;
  letter-spacing: -0.01em;
}}

.page-flow {{ position: relative; }}
/* the curve only exists below the hero: .below-hero wraps everything that
   comes after the portada photo, and .bg-fondo is scoped to it instead of
   the whole page, so the SVG has nothing to run under while the hero photo
   is on screen and only starts the moment the hero ends. */
.below-hero {{ position: relative; }}
.bg-fondo {{
  position: absolute; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
}}
.bg-fondo svg {{
  position: absolute; top: -5%; left: -5%; width: 110%; height: 110%; display: block;
}}

/* ---------- NAV ---------- */
.nav {{
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 18px 32px;
}}
.nav-brand {{
  display: flex; align-items: center; justify-content: center; flex-shrink: 0; cursor: pointer; border: none;
  background: var(--naranja); border-radius: 12px; padding: 9px; /* solid chip so the white mark stays visible over both the hero and the peach body */
  transition: background .25s ease;
}}
.nav-brand:hover {{ background: var(--azul); }}
.tabs {{
  position: relative; display: flex; gap: 4px;
  overflow-x: auto; scrollbar-width: none; max-width: 74vw;
}}
.tabs::-webkit-scrollbar {{ display: none; }}
.tab-pill {{
  position: absolute; top: 4px; height: calc(100% - 8px);
  border-radius: 999px; background: var(--naranja);
  opacity: 0;
  transition: transform .45s cubic-bezier(.16,1,.3,1), width .45s cubic-bezier(.16,1,.3,1), opacity .3s ease;
  z-index: 0;
}}
.tab-pill.show {{ opacity: 1; }}
.tab {{
  position: relative; z-index: 1;
  background: var(--fondo); cursor: pointer; border-radius: 999px;
  border: 1.5px solid var(--naranja); /* solid peach chip, always readable regardless of what's behind the nav */
  font-family: inherit; font-size: 12.5px; font-weight: 600;
  letter-spacing: .02em; text-transform: uppercase;
  color: var(--naranja);
  padding: 9px 16px; white-space: nowrap;
  transition: color .3s ease, background .3s ease, border-color .3s ease;
}}
.tab:hover, .tab.active {{
  background: var(--naranja); color: var(--blanco); border-color: transparent; font-weight: 800;
}}

/* visible keyboard-focus ring, consistent across every interactive control */
.tab:focus-visible, .nav-brand:focus-visible, .stat:focus-visible,
.rail-arrow:focus-visible, .rail:focus-visible, .scroll-cue:focus-visible {{
  outline: 2px solid var(--lima); outline-offset: 3px;
}}

/* ---------- SECTION HEADS (shared) ---------- */
.section-inner {{ position: relative; z-index: 1; width: 100%; max-width: 1400px; margin: 0 auto; padding: 0 32px; }}

/* ---------- PORTADA (hero module, no photo) ---------- */
.portada {{
  position: relative; min-height: 100vh; overflow: hidden;
  display: flex; align-items: center; padding: 140px 0 100px;
  border-radius: 0 0 64px 64px; /* the hero is the whole top of the page; only its
                                    bottom edge rounds off into the section below */
  background: var(--naranja); /* the strong color owns the hero so it reads as its
                                  own bold module against the peach body below it */
  border-bottom: 2px solid var(--fondo);
}}
.portada .section-inner {{ max-width: 900px; }}
.portada-logo {{ margin-bottom: 34px; opacity: 0; animation: riseIn .7s cubic-bezier(.16,1,.3,1) .05s forwards; }}
.portada h1 {{
  color: var(--blanco);
  font-weight: 900; line-height: .85; letter-spacing: -0.07em; text-transform: uppercase;
  font-size: clamp(56px, 8vw, 128px);
  opacity: 0; transform: translateY(24px);
  animation: riseIn .8s cubic-bezier(.16,1,.3,1) .18s forwards;
}}
.portada h1 .lima {{ color: var(--fondo); display: block; }}
.portada p {{
  margin-top: 26px; max-width: 520px; font-size: 20px; font-weight: 500;
  line-height: 1.5; color: rgba(255,255,255,.78);
  opacity: 0; transform: translateY(18px);
  animation: riseIn .7s cubic-bezier(.16,1,.3,1) .34s forwards;
}}
@keyframes riseIn {{ to {{ opacity: 1; transform: translateY(0); }} }}

.scroll-cue {{
  position: absolute; bottom: 36px; left: 32px; z-index: 2;
  display: flex; align-items: center; gap: 10px;
  font-size: 12px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
  color: rgba(255,255,255,.55); cursor: pointer; border: none; background: none; font-family: inherit;
}}
.scroll-cue .chev {{ display: block; animation: bounce 1.8s ease-in-out infinite; }}
@keyframes bounce {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(5px); }} }}

/* ---------- CATEGORY VIEWPORT (one tab visible at a time) ---------- */
.cat-viewport {{ position: relative; }}
.category {{ display: none; }}
.category.active-cat {{ display: block; }}
.category.cat-out {{ animation: catOut .25s cubic-bezier(.4,0,1,1) forwards; }}
.category.cat-in {{ animation: catIn .4s cubic-bezier(.16,1,.3,1); }}
@keyframes catOut {{ to {{ opacity: 0; transform: translateX(-32px); }} }}
@keyframes catIn {{ from {{ opacity: 0; transform: translateX(32px); }} to {{ opacity: 1; transform: translateX(0); }} }}

/* ---------- CATEGORY: cover ---------- */
.cat-cover {{
  position: relative; min-height: 92vh; overflow: hidden;
  display: flex; align-items: center; padding: 120px 0 80px;
}}
.cat-cover .section-inner {{
  display: grid; grid-template-columns: 1.15fr 1fr; gap: 40px; align-items: center;
}}
.cat-cover h1 {{
  color: var(--naranja);
  font-weight: 900; line-height: .85; letter-spacing: -0.07em; text-transform: uppercase;
  font-size: clamp(64px, 9vw, 148px);
  opacity: 0; transform: translateY(24px);
  animation: riseIn .8s cubic-bezier(.16,1,.3,1) .1s forwards;
}}
.cat-cover p {{
  margin-top: 26px; max-width: 460px; font-size: 19px; font-weight: 500;
  line-height: 1.45; color: var(--naranja);
  opacity: 0; transform: translateY(18px);
  animation: riseIn .7s cubic-bezier(.16,1,.3,1) .38s forwards;
}}
.cat-collage {{
  position: relative; height: 560px;
  opacity: 0; animation: riseIn .9s cubic-bezier(.16,1,.3,1) .5s forwards;
}}
.collage-tile {{
  position: absolute; display: block; border-radius: 32px;
  width: auto; height: auto; object-fit: cover; object-position: center;
}}
.ct-1 {{ width: 46%; height: 46%; left: 0; top: 4%; }}
.ct-2 {{ width: 46%; height: 34%; left: 0; bottom: 2%; }}
.ct-3 {{ width: 44%; height: 88%; right: 0; top: 8%; }}

/* ---------- CATEGORY: rail ---------- */
.cat-rail {{ position: relative; overflow: hidden; padding: 40px 0 120px; }}
.rail-head {{
  position: relative; z-index: 1;
  max-width: 1400px; margin: 0 auto 48px; padding: 0 32px;
  opacity: 0; transform: translateY(20px); transition: opacity .7s cubic-bezier(.16,1,.3,1), transform .7s cubic-bezier(.16,1,.3,1);
}}
.rail-head.inview {{ opacity: 1; transform: translateY(0); }}
.rail-eyebrow {{ color: var(--naranja); font-weight: 700; font-size: 13px; letter-spacing: .06em; text-transform: uppercase; }}

.rail-wrap {{ position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; }}
.rail {{
  display: flex; gap: 26px; overflow-x: auto; scroll-snap-type: x proximity;
  padding: 10px 32px 28px; cursor: grab; user-select: none;
  scrollbar-width: none;
}}
.rail::-webkit-scrollbar {{ display: none; }}
.rail.dragging {{ cursor: grabbing; scroll-snap-type: none; }}

.card {{ flex: 0 0 250px; scroll-snap-align: start; }}
.card-photo {{
  display: block; width: 250px; height: 250px; border-radius: 25px;
  object-fit: cover; object-position: center top;
  pointer-events: none; background: #d9d9d9; /* placeholder tone while the lazy image loads in */
}}
.card-body {{
  background: #EEE; border-radius: 20px; padding: 20px;
  margin-top: -34px; position: relative; z-index: 1;
  display: flex; flex-direction: column; gap: 14px;
  pointer-events: none;
}}
.card-name {{ color: var(--azul); font-size: 26px; font-weight: 700; letter-spacing: -0.035em; line-height: 1.08; }}
.chip-row {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.chip {{
  background: var(--blanco); color: var(--azul); font-size: 11px; font-weight: 600;
  padding: 5px 10px; border-radius: 8px; letter-spacing: -0.01em;
}}
.stat-row {{ display: flex; gap: 8px; }}
.stat {{
  flex: 1; background: var(--naranja); border-radius: 12px; padding: 10px 12px;
  text-decoration: none; color: inherit; pointer-events: auto;
  transition: background .2s ease, transform .2s ease, box-shadow .2s ease;
}}
.stat:hover {{
  background: #F58C56; transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(243,111,44,.35);
}}
.stat-label {{ display: block; color: var(--blanco); font-size: 10.5px; font-weight: 500; letter-spacing: -0.01em; }}
.stat-value {{ display: block; color: var(--blanco); font-size: 18px; font-weight: 700; letter-spacing: -0.03em; margin-top: 1px; }}

/* ---------- TARJETA TALENTO — CLEAN BLUR (Figma node 86:359) — mujeres, current ---------- */
.bcard {{
  flex: 0 0 307px; scroll-snap-align: start; position: relative;
  height: 527px; border-radius: 32px; overflow: hidden; background: #d9d9d9;
  transition: transform .4s cubic-bezier(.16,1,.3,1), box-shadow .4s cubic-bezier(.16,1,.3,1);
}}
.bcard:hover {{
  transform: translateY(-6px);
  box-shadow: 0 22px 44px rgba(13,13,23,.28);
}}
.bcard-photo {{
  position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: center top; pointer-events: none;
  transition: transform .5s cubic-bezier(.16,1,.3,1);
}}
.bcard:hover .bcard-photo {{ transform: scale(1.05); }}
.bcard-top-scrim {{
  position: absolute; top: 0; left: 0; right: 0; height: 170px; pointer-events: none;
  background: linear-gradient(to bottom, rgba(13,13,23,.78), rgba(13,13,23,0));
}}
.bcard-top {{
  position: absolute; top: 26px; left: 24px; right: 24px; pointer-events: none;
  display: flex; flex-direction: column; align-items: flex-start; gap: 6px;
}}
.bcard-name {{ color: var(--blanco); font-size: 28px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.05; }}
.bcard-pill {{
  display: inline-flex; align-items: center; padding: 6px 12px; border-radius: 999px;
  background: rgba(255,255,255,.22); -webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px);
  color: var(--blanco); font-size: 11.5px; font-weight: 500;
}}
.bcard-bottom {{
  position: absolute; left: 12px; right: 12px; bottom: 12px; height: 72px;
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
  padding: 12px; border-radius: 22px; box-sizing: border-box;
  background: rgba(0,0,0,.2); border: 1px solid rgba(255,255,255,.25);
  -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px);
}}
.bcard-identity {{ display: flex; align-items: center; gap: 8px; min-width: 0; pointer-events: none; }}
.bcard-avatar {{ width: 34px; height: 34px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }}
.bcard-id-text {{ display: flex; flex-direction: column; gap: 1px; min-width: 0; }}
.bcard-handle {{ color: var(--blanco); font-size: 12.5px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.bcard-role {{ color: rgba(255,255,255,.7); font-size: 10.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.bcard-btn {{
  display: inline-flex; align-items: center; justify-content: center;
  background: var(--naranja); color: var(--blanco); font-weight: 700; font-size: 12px;
  padding: 9px 14px; border-radius: 999px; text-decoration: none; white-space: nowrap; flex-shrink: 0;
  transition: background .2s ease, transform .2s ease;
}}
.bcard-btn:hover {{ background: #F58C56; transform: translateY(-2px); }}

/* ---------- TARJETA TALENTO — DARK (Figma node 89:242) — mujeres only, trial run ---------- */
.tcard {{
  flex: 0 0 300px; scroll-snap-align: start;
  display: flex; flex-direction: column; gap: 18px;
  background: var(--azul); border-radius: 32px; padding: 16px;
}}
.tcard-photo {{
  display: block; width: 268px; height: 300px; border-radius: 22px;
  object-fit: cover; object-position: center top; pointer-events: none;
  background: #d9d9d9;
}}
.tcard-body {{ display: flex; flex-direction: column; gap: 6px; }}
.tcard-name-row {{ display: flex; align-items: center; gap: 6px; }}
.tcard-name {{ color: var(--fondo); font-size: 28px; font-weight: 900; letter-spacing: -0.05em; line-height: 1; }}
.tcard-badge {{
  width: 18px; height: 18px; border-radius: 50%; background: var(--lima);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  color: var(--azul); font-size: 11px; font-weight: 900;
}}
.tcard-subtitle {{ color: var(--fondo); opacity: .65; font-size: 13px; line-height: 1.35; }}
.tcard-bottom {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 8px; }}
.tcard-stats {{ display: flex; align-items: center; gap: 10px; }}
.tcard-stat {{
  display: flex; align-items: center; gap: 4px; text-decoration: none;
  color: var(--fondo); font-size: 13px; font-weight: 700; letter-spacing: -0.03em;
}}
.tcard-stat svg {{ display: block; flex-shrink: 0; }}
.tcard-btn {{
  display: inline-flex; align-items: center; gap: 4px;
  background: var(--naranja); color: var(--fondo); font-weight: 700; font-size: 12.5px;
  padding: 10px 16px; border-radius: 999px; text-decoration: none; white-space: nowrap;
  transition: background .2s ease, transform .2s ease;
}}
.tcard-btn:hover {{ background: #F58C56; transform: translateY(-2px); }}

/* ---------- TARJETA PRINCIPAL (Figma node 49:125) — trends only, trial run ---------- */
.category[data-slug="trends"] .card {{
  flex-basis: 280px;
  border: 5px solid var(--naranja);
  border-radius: 25px;
  overflow: hidden;
}}
.category[data-slug="trends"] .card-photo {{
  width: 280px; height: 280px; border-radius: 0;
}}
.category[data-slug="trends"] .card-body {{
  background: var(--naranja); border-radius: 24px; margin-top: -39px; gap: 16px;
}}
.category[data-slug="trends"] .card-name {{
  color: var(--fondo); font-size: 32px; letter-spacing: -0.09em; line-height: 1.1;
}}
.category[data-slug="trends"] .chip {{
  background: var(--naranja); color: var(--fondo); font-weight: 500;
  font-size: 12px; padding: 6px 12px; letter-spacing: -0.05em;
  border: 1px solid var(--fondo);
}}
.category[data-slug="trends"] .stat {{
  background: var(--fondo); border: 1px solid var(--fondo); padding: 12px 14px;
}}
.category[data-slug="trends"] .stat-row a:nth-child(2) {{ border-color: var(--naranja); }}
.category[data-slug="trends"] .stat-label,
.category[data-slug="trends"] .stat-value {{ color: var(--naranja); }}
.category[data-slug="trends"] .stat:hover {{ background: var(--naranja); box-shadow: none; }}
.category[data-slug="trends"] .stat:hover .stat-label,
.category[data-slug="trends"] .stat:hover .stat-value {{ color: var(--fondo); }}

.rail-arrow {{
  position: absolute; top: 42%; transform: translateY(-50%);
  width: 46px; height: 46px; border-radius: 50%; border: none; cursor: pointer;
  background: rgba(243,111,44,.16); color: var(--naranja);
  display: flex; align-items: center; justify-content: center; font-size: 18px;
  transition: background .25s ease, transform .25s ease;
  z-index: 3;
}}
.rail-arrow:hover {{ background: var(--naranja); color: var(--blanco); transform: translateY(-50%) scale(1.08); }}
.rail-arrow.prev {{ left: 4px; }}
.rail-arrow.next {{ right: 4px; }}

.progress-track {{ max-width: 1400px; margin: 8px auto 0; padding: 0 32px; }}
.progress-bar {{ height: 3px; background: rgba(51,65,154,.18); border-radius: 3px; overflow: hidden; }}
.progress-fill {{ height: 100%; width: 25%; background: var(--naranja); border-radius: 3px; transition: width .1s linear; }}

.toast {{
  position: fixed; bottom: 28px; left: 50%; transform: translateX(-50%) translateY(20px);
  background: var(--blanco); color: var(--negro); font-size: 13px; font-weight: 600;
  padding: 12px 20px; border-radius: 999px; box-shadow: 0 14px 30px rgba(13,13,20,.4);
  opacity: 0; pointer-events: none; transition: opacity .3s ease, transform .3s ease;
  z-index: 200;
}}
.toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

@media (max-width: 860px) {{
  .cat-cover .section-inner {{ grid-template-columns: 1fr; }}
  .cat-collage {{ height: 320px; order: -1; }}
  .tabs {{ max-width: 56vw; }}
  .portada {{ border-radius: 0 0 32px 32px; }}
}}

@media (prefers-reduced-motion: reduce) {{
  html {{ scroll-behavior: auto; }}
  *, *::before, *::after {{
    animation-duration: .001ms !important; animation-iteration-count: 1 !important;
    transition-duration: .001ms !important; scroll-behavior: auto !important;
  }}
}}
</style>

<div class="page-flow" id="pageFlow">
  <nav class="nav">
    <button class="nav-brand" id="navBrand">
      {isotipo_svg(24, "#FFFFFF")}
    </button>
    <div class="tabs" id="tabs">
      <div class="tab-pill" id="tabPill"></div>
      {tabs_html()}
    </div>
  </nav>

  <section class="portada" id="portada">
    <div class="section-inner">
      {isotipo_svg(52, "#FFFFFF", "portada-logo")}
      <h1>Roster<span class="lima">de Talentos</span></h1>
      <p>Creadores y creadoras que conectan marcas con audiencias reales, en cada categoría y en cada red.</p>
    </div>
    <button class="scroll-cue" onclick="document.getElementById('catViewport').scrollIntoView({{behavior:'smooth'}})">
      Explorar por categoría <span class="chev">↓</span>
    </button>
  </section>

  <div class="below-hero">
    <div class="bg-fondo" aria-hidden="true">{fondo_svg()}</div>

    <div class="cat-viewport" id="catViewport">
{sections_html}
    </div>
  </div>
</div>

<div class="toast" id="toast">Esta vista todavía no está armada</div>

<script>
// --- nav pill: active state driven by scrollspy over .category sections ---
const tabsEl = document.getElementById('tabs');
const pill = document.getElementById('tabPill');
const tabEls = Array.from(document.querySelectorAll('.tab'));
let currentActive = null;

function movePill(el) {{
  if (!el) {{ pill.classList.remove('show'); return; }}
  const r = el.getBoundingClientRect();
  const navR = tabsEl.getBoundingClientRect();
  pill.style.width = r.width + 'px';
  pill.style.transform = `translateX(${{r.left - navR.left + tabsEl.scrollLeft}}px)`;
  pill.classList.add('show');
}}

function setActive(cat) {{
  currentActive = cat;
  tabEls.forEach(t => t.classList.toggle('active', t.dataset.cat === cat));
  const el = cat ? tabEls.find(t => t.dataset.cat === cat) : null;
  movePill(el);
}}

// --- category tabs: only one .category is ever in the DOM flow at a time ---
const SLUG_MAP = {slug_map};
const catViewport = document.getElementById('catViewport');
const catSections = {{}};
document.querySelectorAll('.category').forEach(el => {{ catSections[el.dataset.slug] = el; }});
let activeSlug = Object.keys(catSections).find(s => catSections[s].classList.contains('active-cat')) || null;

const REDUCE_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const CAT_OUT_MS = REDUCE_MOTION ? 0 : 250, CAT_IN_MS = REDUCE_MOTION ? 0 : 400;
function showCategory(slug) {{
  const next = catSections[slug];
  if (!next || slug === activeSlug) return;
  const current = activeSlug ? catSections[activeSlug] : null;
  activeSlug = slug;
  setActive(next.dataset.cat);
  if (!current) {{
    next.classList.add('active-cat', 'cat-in');
    setTimeout(() => next.classList.remove('cat-in'), CAT_IN_MS);
    return;
  }}
  current.classList.add('cat-out');
  setTimeout(() => {{
    current.classList.remove('active-cat', 'cat-out');
    next.classList.add('active-cat', 'cat-in');
    setTimeout(() => next.classList.remove('cat-in'), CAT_IN_MS);
  }}, CAT_OUT_MS);
}}

const toast = document.getElementById('toast');
let toastTimer;

document.querySelectorAll('.tcard-btn-toast, .bcard-btn-toast').forEach(btn => {{
  btn.addEventListener('click', (e) => {{
    e.preventDefault();
    toast.textContent = `El mediakit de ${{btn.dataset.name}} todavía no está armado`;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2400);
  }});
}});

tabEls.forEach(t => {{
  t.addEventListener('mouseenter', () => movePill(t));
  t.addEventListener('click', () => {{
    const slug = SLUG_MAP[t.dataset.cat];
    if (slug) {{
      catViewport.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      showCategory(slug);
      return;
    }}
    toast.textContent = `"${{t.dataset.cat}}" todavía no está armada en este prototipo`;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2400);
  }});
}});
tabsEl.addEventListener('mouseleave', () => movePill(currentActive ? tabEls.find(t => t.dataset.cat === currentActive) : null));
document.getElementById('navBrand').addEventListener('click', () => document.getElementById('portada').scrollIntoView({{ behavior: 'smooth' }}));

const portadaObserver = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) setActive(null); }});
}}, {{ rootMargin: '-45% 0px -45% 0px', threshold: 0 }});
portadaObserver.observe(document.getElementById('portada'));

const viewportObserver = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting && activeSlug) setActive(catSections[activeSlug].dataset.cat); }});
}}, {{ rootMargin: '-45% 0px -45% 0px', threshold: 0 }});
viewportObserver.observe(catViewport);

window.addEventListener('resize', () => movePill(currentActive ? tabEls.find(t => t.dataset.cat === currentActive) : null));

// --- reveal on scroll (section headings only) ---
const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) e.target.classList.add('inview'); }});
}}, {{ threshold: .2 }});
document.querySelectorAll('.rail-head').forEach(el => io.observe(el));

// --- carousel: drag to scroll + progress (one instance per category) ---
document.querySelectorAll('.cat-rail').forEach(catRail => {{
  const rail = catRail.querySelector('.rail');
  const progressFill = catRail.querySelector('.progress-fill');
  const prevBtn = catRail.querySelector('.rail-arrow.prev');
  const nextBtn = catRail.querySelector('.rail-arrow.next');

  let isDown = false, startX = 0, startScroll = 0, moved = false, pendingDx = 0, rafScheduled = false;
  rail.addEventListener('pointerdown', (e) => {{
    if (e.target.closest('a')) return; // let real links click through, don't hijack via pointer capture
    isDown = true; moved = false;
    rail.classList.add('dragging');
    startX = e.clientX; startScroll = rail.scrollLeft;
    rail.setPointerCapture(e.pointerId);
  }});
  // pointermove can fire far more often than the screen refreshes (high
  // polling-rate mice/trackpads) — writing scrollLeft on every single event
  // instead of once per animation frame was the main source of dropped
  // frames while dragging.
  rail.addEventListener('pointermove', (e) => {{
    if (!isDown) return;
    pendingDx = e.clientX - startX;
    if (Math.abs(pendingDx) > 4) moved = true;
    if (!rafScheduled) {{
      rafScheduled = true;
      requestAnimationFrame(() => {{
        rail.scrollLeft = startScroll - pendingDx;
        rafScheduled = false;
      }});
    }}
  }});
  ['pointerup', 'pointerleave', 'pointercancel'].forEach(ev =>
    rail.addEventListener(ev, () => {{ isDown = false; rail.classList.remove('dragging'); }})
  );
  rail.addEventListener('click', (e) => {{ if (moved) e.preventDefault(); }}, true);

  // progress bar only — the earlier per-card scale-on-scroll "focus" effect
  // was dropped: it forced a getBoundingClientRect/layout pass for every
  // card on every scroll frame, for a purely decorative touch. Native
  // scroll-snap already gives a smooth, GPU-only carousel without it.
  function updateProgress() {{
    const max = rail.scrollWidth - rail.clientWidth;
    const pct = max > 0 ? (rail.scrollLeft / max) * 100 : 0;
    progressFill.style.width = pct + '%';
  }}
  rail.addEventListener('scroll', updateProgress);

  prevBtn.addEventListener('click', () => rail.scrollBy({{ left: -276, behavior: 'smooth' }}));
  nextBtn.addEventListener('click', () => rail.scrollBy({{ left: 276, behavior: 'smooth' }}));

  updateProgress();
}});
</script>
'''

out_path = os.path.join(HERE, "roster_trends_prototype.html")
with open(out_path, "w") as f:
    f.write(html)
print("wrote", out_path, len(html)/1024, "KB")
