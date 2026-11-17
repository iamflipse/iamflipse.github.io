import html
B = "https://iamflipse.github.io/"
groups = [
("Faith & meaning",[
("sermon-on-the-mount-wiki","Sermon on the Mount","Full text of Matthew 5–7 with Jordan Peterson's lecture commentary, plus four video reels."),
("maps-of-meaning-wiki","Maps of Meaning","Plain-language study wiki for Peterson's Two Ways of Looking at the World lectures."),
]),
("Leadership & marketing",[
("joseph-tsar-channel-wiki","Joseph Tsar on Speaking","99 long-form YouTube videos: clarity, words, and presence, 2023 to 2026."),
("joseph-tsar-leader-wiki","Communicate Like a Leader","Joseph Tsar's full training: intention, focus, body and breath, source and release."),
("jay-yang-wiki","Jay Yang Wiki","Jay Yang's marketing ideas, distilled."),
("jay-yang-course","Writing Words That Make People Buy","Jay Yang's marketing course, from the Full Courses trilogy."),
]),
("Health, aging & longevity",[
("martin-picard-wiki","Martin Picard Interviews","24 long-form YouTube interviews: mitochondria, energy, stress, and gray hair."),
("maha-roundtable-wiki","MAHA Roundtable","American Health & Nutrition: A Second Opinion."),
("biological-age-omics-wiki","Biological Age & Lifestyle","You, Horvath et al. 2026: ageing clocks, and how activity, sleep and diet shape them."),
("intrinsic-health-wiki","Intrinsic Health","Cohen 2026: intrinsic vs realized health, and how to measure it."),
("aging-hallmarks-wiki","Hallmarks of Aging","The 14 hallmarks of aging, from mechanisms to the clinic."),
("cr-aging-biomarkers-wiki","CR & Biological Aging","Guida et al. 2026: caloric restriction and a biomarker index in older adults."),
("if-chrononutrition-wiki","Chrononutrition & Fasting","Ma et al. 2026 on meal timing and intermittent fasting."),
("mets-nma-wiki","Metabolic Syndrome Lifestyle","Chen et al. 2026: exercise, diet and combined interventions compared."),
("mitoq-wiki","MitoQ","The mitochondria-targeted antioxidant and age-related decline."),
("tcm-aging-wiki","TCM & Aging","Traditional Chinese medicine formulas and anti-aging mechanisms."),
("infrared-light-mitochondria-wiki","When Light Meets Metabolism","Roger Seheult, Nov 2026: infrared light, mitochondria, and electron transfer."),
("longevity-scenarios-2031-wiki","Longevity 2031","David Wood's three scenarios and ten levers for 2031."),
("ai-longevity-law-wiki","AI, Longevity & Law","Truby & Kantiana 2026: AI longevity tech and international law."),
("ai-critical-thinking-wiki","AI & Critical Thinking","Pearson 2026 (Nature): AI's effect on memory and reasoning."),
]),
]
n = sum(len(g[1]) for g in groups)

def slug(name):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in name).strip("-")

side = []
body = []
for name, items in groups:
    sid = slug(name)
    side.append(f'<li class="chapter-item expanded part" data-part="{html.escape(sid)}"><a href="#{html.escape(sid)}">{html.escape(name)}</a></li>')
    side.append('<li><ol class="section">')
    entries = []
    for repo, title, desc in items:
        href = f"{B}{repo}/"
        blob = html.escape(f"{title} {desc} {name}".lower())
        side.append(
            f'<li class="chapter-item" data-text="{blob}"><a href="{href}">{html.escape(title)}</a></li>'
        )
        entries.append(
            f'<article class="entry" data-text="{blob}">'
            f'<h3><a href="{href}">{html.escape(title)}</a></h3>'
            f'<p>{html.escape(desc)}</p></article>'
        )
    side.append("</ol></li>")
    side.append('<li class="spacer"></li>')
    body.append(
        f'<section id="{html.escape(sid)}" data-part="{html.escape(sid)}">'
        f'<h2>{html.escape(name)}</h2>'
        + "".join(entries)
        + "</section>"
    )

css = r'''
@font-face{font-family:"Open Sans";font-style:normal;font-weight:400;src:local("Open Sans"),local("OpenSans"),url("fonts/open-sans-v17-all-charsets-regular.woff2") format("woff2")}
@font-face{font-family:"Open Sans";font-style:normal;font-weight:700;src:local("Open Sans Bold"),local("OpenSans-Bold"),url("fonts/open-sans-v17-all-charsets-700.woff2") format("woff2")}
:root{--sidebar-width:300px;--page-padding:15px;--content-max-width:750px;--menu-bar-height:50px;font-size:62.5%}
.light{--bg:hsl(0,0%,100%);--fg:#000;--sidebar-bg:#fafafa;--sidebar-fg:#000;--sidebar-active:#1f1fff;--sidebar-spacer:#f4f4f4;--scrollbar:#8f8f8f;--icons:#747474;--icons-hover:#000;--links:#20609f;--table-border-color:hsl(0,0%,95%);--searchbar-border-color:#aaa;--searchbar-bg:#fafafa;--searchbar-fg:#000}
.coal{--bg:hsl(200,7%,8%);--fg:#98a3ad;--sidebar-bg:#292c2f;--sidebar-fg:#a1adb8;--sidebar-active:#3473ad;--sidebar-spacer:#393939;--scrollbar:#a1adb8;--icons:#43484d;--icons-hover:#b3c0cc;--links:#2b79a2;--table-border-color:hsl(200,7%,13%);--searchbar-border-color:#aaa;--searchbar-bg:#b7b7b7;--searchbar-fg:#000}
.navy{--bg:hsl(226,23%,11%);--fg:#bcbdd0;--sidebar-bg:#282d3f;--sidebar-fg:#c8c9db;--sidebar-active:#2b79a2;--sidebar-spacer:#2d334f;--scrollbar:#c8c9db;--icons:#737480;--icons-hover:#b7b9cc;--links:#2b79a2;--table-border-color:hsl(226,23%,16%);--searchbar-border-color:#aaa;--searchbar-bg:#aeaec6;--searchbar-fg:#000}
.ayu{--bg:hsl(210,25%,8%);--fg:#c5c5c5;--sidebar-bg:#14191f;--sidebar-fg:#c8c9db;--sidebar-active:#ffb454;--sidebar-spacer:#2d334f;--scrollbar:#c8c9db;--icons:#737480;--icons-hover:#b7b9cc;--links:#0096cf;--table-border-color:hsl(210,25%,13%);--searchbar-border-color:#848484;--searchbar-bg:#424242;--searchbar-fg:#fff}
*{box-sizing:border-box}
html{font-family:"Open Sans",sans-serif;color:var(--fg);background:var(--bg);scrollbar-color:var(--scrollbar) var(--bg)}
body{margin:0;font-size:1.6rem}
#sidebar{position:fixed;left:0;top:0;bottom:0;width:var(--sidebar-width);background:var(--sidebar-bg);color:var(--sidebar-fg);overflow-y:auto;z-index:100;padding:12px 14px 24px;transform:translateX(calc(0px - var(--sidebar-width)))}
html.sidebar-visible #sidebar{transform:none}
#q{width:100%;margin:8px 0 12px;padding:8px 10px;font:inherit;font-size:1.4rem;color:var(--searchbar-fg);background:var(--searchbar-bg);border:1px solid var(--searchbar-border-color);border-radius:4px}
.chapter,.section{list-style:none;margin:0;padding:0}
.section{padding-left:16px}
.chapter-item{line-height:1.7em;margin-top:.35em}
.chapter-item a{color:var(--sidebar-fg);text-decoration:none}
.chapter-item a:hover,.chapter-item a.active{color:var(--sidebar-active)}
.part>a{font-weight:700}
.spacer{height:3px;margin:8px 0;background:var(--sidebar-spacer);list-style:none}
.hide{display:none}
.page-wrapper{margin-left:0}
@media (min-width:620px){
  html.sidebar-visible .page-wrapper{margin-left:var(--sidebar-width)}
}
#menu-bar{position:sticky;top:0;z-index:101;display:flex;align-items:center;height:var(--menu-bar-height);background:var(--bg);border-bottom:1px solid var(--table-border-color);padding:0 12px}
#menu-bar button{border:0;background:none;color:var(--icons);font:inherit;font-size:1.4rem;cursor:pointer;padding:0 8px;line-height:var(--menu-bar-height)}
#menu-bar button:hover,#menu-bar button[aria-pressed="true"]{color:var(--icons-hover)}
.menu-title{margin:0 auto 0 8px;font-size:1.6rem;font-weight:400}
.content{max-width:var(--content-max-width);margin:0 auto;padding:24px var(--page-padding) 64px}
.content h1{font-size:2.2em;font-weight:400;margin:0 0 .4em}
.content h2{font-size:1.6em;font-weight:400;margin:1.4em 0 .4em;border-bottom:1px solid var(--table-border-color);padding-bottom:.2em}
.content h3{font-size:1.15em;font-weight:600;margin:1.1em 0 .2em}
.content p{line-height:1.45em;margin:.2em 0 .8em}
.content a{color:var(--links);text-decoration:none}
.content a:hover{text-decoration:underline}
.updated{margin-top:2.5em;color:var(--fg);opacity:.7;font-size:.9em}
'''

page = f'''<!doctype html>
<html lang="en" class="light sidebar-visible">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Steve's Wikis</title>
<meta name="description" content="Study wikis by Steve Flipse">
<style>{css}</style>
</head>
<body>
<nav id="sidebar" aria-label="Wikis">
<input id="q" type="search" placeholder="Search" aria-label="Search">
<ol class="chapter">
<li class="chapter-item"><a href="#top">Steve's Wikis</a></li>
<li class="spacer"></li>
{''.join(side)}
</ol>
</nav>
<div class="page-wrapper">
<div id="menu-bar">
<button id="sidebar-toggle" type="button" aria-label="Toggle sidebar">Menu</button>
<div class="menu-title">Steve's Wikis</div>
<button type="button" data-theme="light" aria-pressed="true">Light</button>
<button type="button" data-theme="coal">Coal</button>
<button type="button" data-theme="navy">Navy</button>
<button type="button" data-theme="ayu">Ayu</button>
</div>
<main class="content">
<h1 id="top">Steve's Wikis</h1>
<p>{n} study wikis: faith, leadership, marketing, health and longevity.</p>
{''.join(body)}
<p class="updated">Updated 2026-11-16 · <a href="https://github.com/iamflipse">github.com/iamflipse</a></p>
</main>
</div>
<script>
const themes=["light","coal","navy","ayu"];
const root=document.documentElement;
function setTheme(t){{
  if(!themes.includes(t)) t="light";
  themes.forEach(x=>root.classList.remove(x));
  root.classList.add(t);
  document.querySelectorAll("[data-theme]").forEach(b=>b.setAttribute("aria-pressed", b.dataset.theme===t ? "true" : "false"));
  try{{localStorage.setItem("mdbook-theme", t)}}catch(e){{}}
}}
try{{
  const saved=localStorage.getItem("mdbook-theme");
  if(themes.includes(saved)) setTheme(saved);
}}catch(e){{}}
document.querySelectorAll("[data-theme]").forEach(b=>b.addEventListener("click",()=>setTheme(b.dataset.theme)));
document.getElementById("sidebar-toggle").addEventListener("click",()=>root.classList.toggle("sidebar-visible"));
document.getElementById("q").addEventListener("input",e=>{{
  const v=e.target.value.toLowerCase();
  document.querySelectorAll(".chapter-item[data-text], .entry").forEach(el=>{{
    el.classList.toggle("hide", v && !el.dataset.text.includes(v));
  }});
  document.querySelectorAll("section[data-part]").forEach(s=>{{
    const any=[...s.querySelectorAll(".entry")].some(el=>!el.classList.contains("hide"));
    s.classList.toggle("hide", !any);
    const part=document.querySelector('.part[data-part="'+s.dataset.part+'"]');
    if(part) part.classList.toggle("hide", !any);
  }});
}});
</script>
</body></html>
'''
open("index.html", "w").write(page)
print(n)
