# -*- coding: utf-8 -*-
import json, os, re

HERE = os.path.dirname(__file__)
people = json.load(open(os.path.join(HERE, "people.json")))
fonts = json.load(open(os.path.join(HERE, "fonts.json")))

LOGO_SVG_RAW = open("/Users/tomascardozo/main/big/brand/nuevo/big-logo2.svg").read()
ISOTIPO_PATH = re.search(r'\sd="([^"]+)"', LOGO_SVG_RAW).group(1)
ISOTIPO_VIEWBOX = re.search(r'viewBox="([^"]+)"', LOGO_SVG_RAW).group(1)

FONDO_SVG_RAW = open("/Users/tomascardozo/main/big/web/vectorfondo.svg").read()
FONDO_INNER = re.search(r"<svg[^>]*>(.*)</svg>", FONDO_SVG_RAW, re.S).group(1)
FONDO_VIEWBOX = re.search(r'viewBox="([^"]+)"', FONDO_SVG_RAW).group(1)

# Fantasy/placeholder data — first profile only (Agustina Cambra), structured so
# adding the next person later is just another dict entry. Numbers are made up
# but internally consistent (ages sum to 100, IG/TikTok reach differ by platform)
# to avoid the copy-paste-looking duplication flagged in the reference mediakit.
MEDIAKIT = {
    "agustina_cambra": dict(
        pilares=["Lifestyle", "Música", "Actuación", "Moda"],
        bio="Agustina combina música, actuación y lifestyle para crear contenido auténtico. "
            "Su comunidad destaca por su cercanía e interacción, convirtiéndola en una creadora "
            "versátil para campañas de moda, belleza, entretenimiento y experiencias.",
        contact_email="contacto@bigagency.com.ar",
        contact_handle="@agusfc_",
        platforms=dict(
            instagram=dict(
                label="Instagram", mono="IG", followers="35.4 K",
                er="4.8%", reach="128 K", reach_window="Alcance · últimos 30 días",
                gender=dict(mujeres=60, hombres=40),
                age=[("18-24", 38), ("25-34", 34), ("35+", 28)],
            ),
            tiktok=dict(
                label="TikTok", mono="TT", followers="2 M",
                er="7.2%", reach="540 K", reach_window="Alcance · últimos 30 días",
                gender=dict(mujeres=70, hombres=30),
                age=[("18-24", 45), ("25-34", 33), ("35+", 22)],
            ),
        ),
        countries=[("🇦🇷", "Argentina", 42), ("🇨🇱", "Chile", 15), ("🇺🇾", "Uruguay", 11),
                   ("🇲🇽", "México", 9), ("🇪🇸", "España", 8)],
        collab_photos=["agustina_cambra", "pia_scarnato", "dulce_pink", "juli_savioli"],
    ),
}

def isotipo_svg(size=24, color="#FFFFFF", cls=""):
    return f'<svg class="{cls}" width="{size}" height="{size}" viewBox="{ISOTIPO_VIEWBOX}" style="color:{color}"><path fill="currentColor" d="{ISOTIPO_PATH}"/></svg>'

def fondo_svg():
    return f'<svg viewBox="{FONDO_VIEWBOX}" preserveAspectRatio="xMidYMid slice">{FONDO_INNER}</svg>'

def bar_gender(g):
    total = g["mujeres"] + g["hombres"]
    m_pct = round(g["mujeres"] / total * 100)
    h_pct = 100 - m_pct
    return f'''
    <div class="mk-gender">
      <div class="mk-gender-labels"><span>Mujeres</span><span>Hombres</span></div>
      <div class="mk-gender-bar">
        <div class="mk-gender-seg mk-seg-m" style="width:{m_pct}%"></div>
        <div class="mk-gender-seg mk-seg-h" style="width:{h_pct}%"></div>
      </div>
      <div class="mk-gender-values"><span>{m_pct}%</span><span>{h_pct}%</span></div>
    </div>'''

def bars_age(age_list):
    rows = "".join(f'''
      <div class="mk-age-row">
        <span class="mk-age-label">{label}</span>
        <div class="mk-age-track"><div class="mk-age-fill" style="width:{pct}%"></div></div>
        <span class="mk-age-value">{pct}%</span>
      </div>''' for label, pct in age_list)
    return f'<div class="mk-age">{rows}</div>'

def platform_panel(key, p, active):
    return f'''
    <div class="mk-audience-panel" data-platform-panel="{key}" {"" if active else 'style="display:none"'}>
      <div class="mk-audience-cols">
        <div>
          <div class="mk-audience-subhead">Género</div>
          {bar_gender(p["gender"])}
        </div>
        <div>
          <div class="mk-audience-subhead">Edad</div>
          {bars_age(p["age"])}
        </div>
      </div>
    </div>'''

def platform_card(key, p):
    return f'''
    <article class="mk-card mk-platform">
      <div class="mk-platform-head">
        <div class="mk-mono">{p["mono"]}</div>
        <div class="mk-platform-name">{p["label"]}</div>
      </div>
      <div class="mk-followers">{p["followers"]}<span>seguidores</span></div>
      <div class="mk-platform-stats">
        <div class="mk-mini-stat"><span class="mk-mini-label">Engagement</span><span class="mk-mini-value">{p["er"]}</span></div>
        <div class="mk-mini-stat"><span class="mk-mini-label">{p["reach_window"]}</span><span class="mk-mini-value">{p["reach"]}</span></div>
      </div>
    </article>'''

def build_profile(pid):
    person = people[pid]
    mk = MEDIAKIT[pid]
    pilares = "".join(f'<span class="chip">{t}</span>' for t in mk["pilares"])
    platforms = mk["platforms"]
    platform_cards = "".join(platform_card(k, p) for k, p in platforms.items())
    toggle_btns = "".join(
        f'<button class="mk-toggle-btn{" active" if i == 0 else ""}" data-platform="{k}">{p["label"]}</button>'
        for i, (k, p) in enumerate(platforms.items())
    )
    audience_panels = "".join(platform_panel(k, p, i == 0) for i, (k, p) in enumerate(platforms.items()))
    countries = "".join(f'''
      <div class="mk-country-row">
        <span class="mk-country-flag">{flag}</span>
        <span class="mk-country-name">{name}</span>
        <div class="mk-country-track"><div class="mk-country-fill" style="width:{pct}%"></div></div>
        <span class="mk-country-value">{pct}%</span>
      </div>''' for flag, name, pct in mk["countries"])
    collab_imgs = "".join(
        f'<img class="mk-collab-thumb" src="{people[cid]["photo"]}" alt="" loading="lazy" decoding="async">'
        for cid in mk["collab_photos"]
    )

    return f'''<title>{person["name"]} — Media Kit — BIG Roster 2026</title>
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
body {{
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--fondo);
  color: var(--azul);
  letter-spacing: -0.01em;
  min-height: 100vh;
}}

.mk-bg {{ position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }}
.mk-bg svg {{ position: absolute; top: -5%; left: -5%; width: 110%; height: 110%; display: block; }}

.mk-shell {{ position: relative; z-index: 1; max-width: 1360px; margin: 0 auto; padding: 28px 32px 80px; }}

.mk-nav {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 28px; }}
.mk-badge {{
  display: flex; align-items: center; justify-content: center;
  background: var(--naranja); border-radius: 12px; padding: 9px;
  text-decoration: none;
}}
.mk-back {{
  display: flex; align-items: center; gap: 8px;
  color: var(--azul); text-decoration: none; font-weight: 700; font-size: 13px;
  letter-spacing: .02em; text-transform: uppercase;
  border: 1.5px solid var(--azul); border-radius: 999px; padding: 9px 18px 9px 14px;
  transition: background .25s ease, color .25s ease;
}}
.mk-back:hover {{ background: var(--azul); color: var(--blanco); }}

.mk-grid {{
  display: grid; grid-template-columns: 340px 1fr 1fr; gap: 24px;
  grid-template-areas:
    "profile ig tt"
    "profile audience audience"
    "profile paises collab";
  align-items: start;
}}

.mk-card {{
  background: var(--blanco); border-radius: 28px; padding: 28px;
}}

/* ---------- profile sidebar ---------- */
.mk-profile {{
  grid-area: profile; background: var(--azul); color: var(--blanco);
  border-radius: 32px; padding: 28px;
  display: flex; flex-direction: column; gap: 20px;
}}
.mk-photo {{
  width: 100%; aspect-ratio: 4/5; object-fit: cover; object-position: center top;
  border-radius: 22px; display: block;
}}
.mk-name {{
  color: var(--lima); font-weight: 900; text-transform: uppercase;
  font-size: 30px; line-height: .95; letter-spacing: -0.05em;
  margin-bottom: 12px;
}}
.mk-pilares {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.mk-profile .chip {{
  background: var(--blanco); color: var(--azul); font-size: 11px; font-weight: 600;
  padding: 5px 10px; border-radius: 8px; letter-spacing: -0.01em;
}}
.mk-vibe-label {{
  color: var(--naranja); font-weight: 800; font-size: 12.5px;
  letter-spacing: .06em; text-transform: uppercase;
}}
.mk-bio {{ color: rgba(255,255,255,.8); font-size: 14.5px; line-height: 1.5; margin-top: 6px; }}
.mk-contact {{
  margin-top: auto; padding-top: 18px; border-top: 1px solid rgba(255,255,255,.18);
  display: flex; flex-direction: column; gap: 10px;
}}
.mk-contact-row {{ display: flex; flex-direction: column; gap: 2px; font-size: 13px; color: rgba(255,255,255,.75); }}
.mk-contact-row b {{ color: var(--blanco); font-weight: 700; }}
.mk-cta {{
  display: inline-flex; align-items: center; justify-content: center;
  background: var(--naranja); color: var(--blanco); font-weight: 800; font-size: 13px;
  text-transform: uppercase; letter-spacing: .03em; border-radius: 999px;
  padding: 12px; text-decoration: none; transition: background .25s ease;
}}
.mk-cta:hover {{ background: var(--blanco); color: var(--naranja); }}

/* ---------- platform cards ---------- */
.mk-platform-head {{ display: flex; align-items: center; gap: 10px; }}
.mk-mono {{
  width: 34px; height: 34px; border-radius: 10px; background: var(--azul); color: var(--blanco);
  display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 12px;
}}
.mk-platform-name {{ font-weight: 700; font-size: 14px; color: var(--azul); }}
.mk-followers {{
  margin-top: 16px; font-weight: 900; font-size: 40px; letter-spacing: -0.04em;
  color: var(--naranja); line-height: 1;
}}
.mk-followers span {{
  display: block; font-weight: 600; font-size: 12px; letter-spacing: 0; text-transform: none;
  color: var(--azul); opacity: .6; margin-top: 6px;
}}
.mk-platform-stats {{ display: flex; gap: 10px; margin-top: 20px; }}
.mk-mini-stat {{
  flex: 1; background: var(--fondo); border-radius: 14px; padding: 10px 12px;
}}
.mk-mini-label {{ display: block; font-size: 10.5px; font-weight: 600; color: var(--azul); opacity: .65; }}
.mk-mini-value {{ display: block; font-size: 17px; font-weight: 800; color: var(--azul); margin-top: 2px; }}

/* ---------- audience card ---------- */
.mk-audience {{ grid-area: audience; }}
.mk-audience-headrow {{ display: flex; align-items: center; justify-content: space-between; }}
.mk-audience-title {{ font-weight: 800; font-size: 18px; color: var(--azul); }}
.mk-toggle {{ display: flex; gap: 4px; background: var(--fondo); border-radius: 999px; padding: 4px; }}
.mk-toggle-btn {{
  border: none; background: none; cursor: pointer; border-radius: 999px;
  font-family: inherit; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .02em;
  color: var(--naranja); padding: 7px 14px; transition: background .25s ease, color .25s ease;
}}
.mk-toggle-btn.active {{ background: var(--naranja); color: var(--blanco); }}
.mk-audience-cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin-top: 22px; }}
.mk-audience-subhead {{ font-weight: 700; font-size: 13px; color: var(--azul); opacity: .7; margin-bottom: 12px; }}

.mk-gender-labels, .mk-gender-values {{
  display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 700; color: var(--azul);
}}
.mk-gender-bar {{ display: flex; height: 10px; border-radius: 999px; overflow: hidden; margin: 6px 0; }}
.mk-seg-m {{ background: var(--lima); }}
.mk-seg-h {{ background: var(--azul); }}

.mk-age-row {{ display: grid; grid-template-columns: 48px 1fr 40px; align-items: center; gap: 10px; margin-top: 10px; }}
.mk-age-label {{ font-size: 12px; font-weight: 700; color: var(--azul); opacity: .7; }}
.mk-age-track {{ height: 8px; border-radius: 999px; background: var(--fondo); overflow: hidden; }}
.mk-age-fill {{ height: 100%; background: var(--naranja); border-radius: 999px; }}
.mk-age-value {{ font-size: 12.5px; font-weight: 800; color: var(--azul); text-align: right; }}

/* ---------- countries ---------- */
.mk-countries {{ grid-area: paises; }}
.mk-country-row {{ display: grid; grid-template-columns: 22px 84px 1fr 36px; align-items: center; gap: 10px; margin-top: 12px; }}
.mk-country-row:first-of-type {{ margin-top: 18px; }}
.mk-country-flag {{ font-size: 16px; }}
.mk-country-name {{ font-size: 12.5px; font-weight: 700; color: var(--azul); }}
.mk-country-track {{ height: 8px; border-radius: 999px; background: var(--fondo); overflow: hidden; }}
.mk-country-fill {{ height: 100%; background: var(--azul); border-radius: 999px; }}
.mk-country-value {{ font-size: 12.5px; font-weight: 800; color: var(--azul); text-align: right; }}

/* ---------- collaborations preview ---------- */
.mk-collab {{ grid-area: collab; }}
.mk-collab-head {{ display: flex; align-items: center; justify-content: space-between; }}
.mk-collab-link {{ font-size: 12px; font-weight: 700; color: var(--naranja); text-decoration: none; }}
.mk-collab-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 18px; }}
.mk-collab-thumb {{ width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px; display: block; }}

.mk-card-title {{ font-weight: 800; font-size: 18px; color: var(--azul); }}

@media (max-width: 1000px) {{
  .mk-grid {{
    grid-template-columns: 1fr; grid-template-areas: "profile" "ig" "tt" "audience" "paises" "collab";
  }}
  .mk-audience-cols {{ grid-template-columns: 1fr; gap: 20px; }}
}}
</style>

<div class="mk-bg" aria-hidden="true">{fondo_svg()}</div>

<div class="mk-shell">
  <nav class="mk-nav">
    <a class="mk-back" href="index.html">← Volver al roster</a>
    <a class="mk-badge" href="index.html" aria-label="BIG Agency">{isotipo_svg(22, "#FFFFFF")}</a>
  </nav>

  <div class="mk-grid">
    <aside class="mk-profile">
      <img class="mk-photo" src="{person["photo"]}" alt="{person["name"]}">
      <div>
        <div class="mk-name">{person["name"]}</div>
        <div class="mk-pilares">{pilares}</div>
      </div>
      <div>
        <div class="mk-vibe-label">Her Vibe</div>
        <p class="mk-bio">{mk["bio"]}</p>
      </div>
      <div class="mk-contact">
        <div class="mk-contact-row">Contacto agencia<b>{mk["contact_email"]}</b></div>
        <div class="mk-contact-row">Handle<b>{mk["contact_handle"]}</b></div>
        <a class="mk-cta" href="mailto:{mk["contact_email"]}">Contactar</a>
      </div>
    </aside>

    {platform_cards}

    <section class="mk-card mk-audience">
      <div class="mk-audience-headrow">
        <div class="mk-audience-title">Audiencia</div>
        <div class="mk-toggle">{toggle_btns}</div>
      </div>
      {audience_panels}
    </section>

    <section class="mk-card mk-countries">
      <div class="mk-card-title">Top países</div>
      {countries}
    </section>

    <section class="mk-card mk-collab">
      <div class="mk-collab-head">
        <div class="mk-card-title">Colaboraciones</div>
        <a class="mk-collab-link" href="#">Ver todas →</a>
      </div>
      <div class="mk-collab-grid">{collab_imgs}</div>
    </section>
  </div>
</div>

<script>
document.querySelectorAll('.mk-toggle-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.mk-toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const plat = btn.dataset.platform;
    document.querySelectorAll('[data-platform-panel]').forEach(p => {{
      p.style.display = p.dataset.platformPanel === plat ? '' : 'none';
    }});
  }});
}});
</script>
'''

font_faces = "\n".join(f'''
@font-face {{
  font-family: 'Inter';
  font-weight: {w};
  font-style: normal;
  src: url(data:font/woff2;base64,{fonts[name]}) format('woff2');
  font-display: swap;
}}''' for name, w in [("Regular", 400), ("Medium", 500), ("Bold", 700), ("Black", 900)])

for pid in MEDIAKIT:
    html = build_profile(pid)
    out_path = os.path.join(HERE, f"mediakit.html")
    with open(out_path, "w") as f:
        f.write(html)
    print("wrote", out_path, len(html) / 1024, "KB")
