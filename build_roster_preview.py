# -*- coding: utf-8 -*-
# Standalone preview build for external sharing: only Mujeres + Hombres,
# both using the "Tarjeta Talento — Clean Blur" card, "Ver más" always
# linking straight to the person's real Instagram (no mediakit/toast).
# Kept as its own file (not a mode flag on build_html.py) so the main
# site's build is never at risk while this one-off is iterated on.
import json, os, re

HERE = os.path.dirname(__file__)
people = json.load(open(os.path.join(HERE, "people.json")))
fonts = json.load(open(os.path.join(HERE, "fonts.json")))

# collage-only entries (different shots than their card photo), used just for
# the Hombres cat-cover preview, not part of the shared people.json dataset
people["pelao_khe_collage"] = {"name": "Pelao Khe", "photo": "assets/photos/pelao_khe_collage.webp"}
people["pablo_bruschi_collage"] = {"name": "Pablo Bruschi", "photo": "assets/photos/pablo_bruschi_collage.webp"}
people["benja_calero_collage"] = {"name": "Benja Calero", "photo": "assets/photos/benja_calero_collage.webp"}

FONDO_SVG_RAW = open("/Users/tomascardozo/main/big/web/vectorfondo.svg").read()
FONDO_INNER = re.search(r"<svg[^>]*>(.*)</svg>", FONDO_SVG_RAW, re.S).group(1)
FONDO_VIEWBOX = re.search(r'viewBox="([^"]+)"', FONDO_SVG_RAW).group(1)

LOGO_SVG_RAW = open("/Users/tomascardozo/main/big/brand/nuevo/big-logo2.svg").read()
ISOTIPO_PATH = re.search(r'\sd="([^"]+)"', LOGO_SVG_RAW).group(1)
ISOTIPO_VIEWBOX = re.search(r'viewBox="([^"]+)"', LOGO_SVG_RAW).group(1)

CATEGORIES = ["Mujeres", "Hombres"]

# maca_castro, ammichis (mujeres) and fran_silva, gena_pedrazzi, nico_grasso (hombres)
# excluded from every roster appearance per client decision
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
        slug="hombres", name="Hombres", split=("Hom", "bres"),
        subtitle="Carisma, humor y personalidad — los creadores que más conectan con audiencias masivas en cada plataforma.",
        collage=["pelao_khe_collage", "pablo_bruschi_collage", "benja_calero_collage"],
        order=["pelao_khe", "benja_calero", "tiago_bergallo", "cris_pierri", "hablemos_de_cine",
               "ber_scarnato", "mariano_bondar", "inachomer", "santi_gallo", "pablo_bruschi",
               "joselo_marquez", "bruno_rondini", "lubru_invierte", "los_arias_brothers",
               "facu_garcia", "lean_riccio", "tomas_alvarez", "el_capo_willy", "agus_benca",
               "lucas_monopoli", "soy_dalto"],
    ),
]

def isotipo_svg(size=28, color="#FFFFFF", cls=""):
    return f'<svg class="{cls}" width="{size}" height="{size}" viewBox="{ISOTIPO_VIEWBOX}" style="color:{color}"><path fill="currentColor" d="{ISOTIPO_PATH}"/></svg>'

def tabs_html():
    return "\n".join(f'<button class="tab" data-cat="{cat}">{cat}</button>' for cat in CATEGORIES)

def _follower_num(s):
    s = s.strip().upper()
    mult = 1_000_000 if s.endswith("M") else 1_000 if s.endswith("K") else 1
    try:
        return float(s[:-1].strip() if mult > 1 else s) * mult
    except ValueError:
        return 0

def card_html(pid, i):
    """'Tarjeta Talento — Clean Blur' (Figma node 86:359), Ver más -> Instagram real."""
    p = people[pid]
    role = " · ".join(p["tags"])
    top_stat = p["ig"] if _follower_num(p["ig"]) >= _follower_num(p["tt"]) else p["tt"]
    handle = p["ig_url"].rstrip("/").rsplit("/", 1)[-1]
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
        <a class="bcard-btn" href="{p["ig_url"]}" target="_blank" rel="noopener">Ver más</a>
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
    cards = "".join(card_html(pid, i) for i, pid in enumerate(cat["order"]))
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
slug_map = json.dumps({cat["name"]: cat["slug"] for cat in SECTIONS})

html = f'''<title>BIG Roster 2026</title>
<style>
{font_faces}

:root {{
  --azul: #33419A;
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
.below-hero {{ position: relative; }}
.bg-fondo {{ position: absolute; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }}
.bg-fondo svg {{ position: absolute; top: -5%; left: -5%; width: 110%; height: 110%; display: block; }}

/* ---------- NAV ---------- */
.nav {{
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 18px 32px;
}}
.nav-brand {{
  display: flex; align-items: center; justify-content: center; flex-shrink: 0; cursor: pointer; border: none;
  background: var(--naranja); border-radius: 12px; padding: 9px;
  transition: background .25s ease;
}}
.nav-brand:hover {{ background: var(--azul); }}
.tabs {{ position: relative; display: flex; gap: 4px; }}
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
  border: 1.5px solid var(--naranja);
  font-family: inherit; font-size: 12.5px; font-weight: 600;
  letter-spacing: .02em; text-transform: uppercase;
  color: var(--naranja);
  padding: 9px 16px; white-space: nowrap;
  transition: color .3s ease, background .3s ease, border-color .3s ease;
}}
.tab:hover, .tab.active {{
  background: var(--naranja); color: var(--blanco); border-color: transparent; font-weight: 800;
}}

.tab:focus-visible, .nav-brand:focus-visible, .rail-arrow:focus-visible, .rail:focus-visible, .scroll-cue:focus-visible {{
  outline: 2px solid var(--lima); outline-offset: 3px;
}}

.section-inner {{ position: relative; z-index: 1; width: 100%; max-width: 1400px; margin: 0 auto; padding: 0 32px; }}

/* ---------- PORTADA ---------- */
.portada {{
  position: relative; min-height: 82vh; overflow: hidden;
  display: flex; align-items: center; padding: 140px 0 100px;
  border-radius: 0 0 64px 64px;
  background: var(--naranja);
  border-bottom: 2px solid var(--fondo);
}}
.portada .section-inner {{ max-width: 900px; }}
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

.cat-viewport {{ position: relative; }}
.category {{ display: none; }}
.category.active-cat {{ display: block; }}
.category.cat-out {{ animation: catOut .25s cubic-bezier(.4,0,1,1) forwards; }}
.category.cat-in {{ animation: catIn .4s cubic-bezier(.16,1,.3,1); }}
@keyframes catOut {{ to {{ opacity: 0; transform: translateX(-32px); }} }}
@keyframes catIn {{ from {{ opacity: 0; transform: translateX(32px); }} to {{ opacity: 1; transform: translateX(0); }} }}

.cat-cover {{ position: relative; min-height: 92vh; overflow: hidden; display: flex; align-items: center; padding: 120px 0 80px; }}
.cat-cover .section-inner {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 40px; align-items: center; }}
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
.cat-collage {{ position: relative; height: 560px; opacity: 0; animation: riseIn .9s cubic-bezier(.16,1,.3,1) .5s forwards; }}
.collage-tile {{ position: absolute; display: block; border-radius: 32px; width: auto; height: auto; object-fit: cover; object-position: center; }}
.ct-1 {{ width: 46%; height: 46%; left: 0; top: 4%; }}
.ct-2 {{ width: 46%; height: 34%; left: 0; bottom: 2%; }}
.ct-3 {{ width: 44%; height: 88%; right: 0; top: 8%; }}

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
  padding: 10px 32px 28px; cursor: grab; user-select: none; scrollbar-width: none;
}}
.rail::-webkit-scrollbar {{ display: none; }}
.rail.dragging {{ cursor: grabbing; scroll-snap-type: none; }}

/* ---------- TARJETA TALENTO — CLEAN BLUR (Figma node 86:359) ---------- */
.bcard {{
  flex: 0 0 307px; scroll-snap-align: start; position: relative;
  height: 527px; border-radius: 32px; overflow: hidden; background: #d9d9d9;
  transition: transform .4s cubic-bezier(.16,1,.3,1), box-shadow .4s cubic-bezier(.16,1,.3,1);
}}
.bcard:hover {{ transform: translateY(-6px); box-shadow: 0 22px 44px rgba(13,13,23,.28); }}
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
.bcard-top {{ position: absolute; top: 26px; left: 24px; right: 24px; pointer-events: none; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }}
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

@media (max-width: 860px) {{
  .cat-cover .section-inner {{ grid-template-columns: 1fr; }}
  .cat-collage {{ height: 320px; order: -1; }}
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
      <h1>Roster<span class="lima">de Talentos</span></h1>
      <p>Creadores y creadoras que conectan marcas con audiencias reales, en cada categoría y en cada red.</p>
    </div>
    <button class="scroll-cue" onclick="document.getElementById('catViewport').scrollIntoView({{behavior:'smooth'}})">
      Explorar más <span class="chev">↓</span>
    </button>
  </section>

  <div class="below-hero">
    <div class="bg-fondo" aria-hidden="true">{fondo_svg()}</div>
    <div class="cat-viewport" id="catViewport">
{sections_html}
    </div>
  </div>
</div>

<script>
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

tabEls.forEach(t => {{
  t.addEventListener('mouseenter', () => movePill(t));
  t.addEventListener('click', () => {{
    const slug = SLUG_MAP[t.dataset.cat];
    catViewport.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    showCategory(slug);
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

const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) e.target.classList.add('inview'); }});
}}, {{ threshold: .2 }});
document.querySelectorAll('.rail-head').forEach(el => io.observe(el));

document.querySelectorAll('.cat-rail').forEach(catRail => {{
  const rail = catRail.querySelector('.rail');
  const progressFill = catRail.querySelector('.progress-fill');
  const prevBtn = catRail.querySelector('.rail-arrow.prev');
  const nextBtn = catRail.querySelector('.rail-arrow.next');

  let isDown = false, startX = 0, startScroll = 0, moved = false, pendingDx = 0, rafScheduled = false;
  rail.addEventListener('pointerdown', (e) => {{
    if (e.target.closest('a')) return;
    isDown = true; moved = false;
    rail.classList.add('dragging');
    startX = e.clientX; startScroll = rail.scrollLeft;
    rail.setPointerCapture(e.pointerId);
  }});
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

  function updateProgress() {{
    const max = rail.scrollWidth - rail.clientWidth;
    const pct = max > 0 ? (rail.scrollLeft / max) * 100 : 0;
    progressFill.style.width = pct + '%';
  }}
  rail.addEventListener('scroll', updateProgress);

  prevBtn.addEventListener('click', () => rail.scrollBy({{ left: -333, behavior: 'smooth' }}));
  nextBtn.addEventListener('click', () => rail.scrollBy({{ left: 333, behavior: 'smooth' }}));

  updateProgress();
}});
</script>
'''

out_path = os.path.join(HERE, "roster.html")
with open(out_path, "w") as f:
    f.write(html)
print("wrote", out_path, len(html) / 1024, "KB")
