"""Generate the decorative SVGs in assets/ from data/achievements.json.

Run from the repository root:  python scripts/generate_badges.py

Badge images are not generated: the guide links GitHub's official artwork at
https://github.githubassets.com/images/modules/profile/achievements/<id>-<tier>.png
and prints that table of URLs so you can check every one still resolves.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "achievements.json").read_text(encoding="utf-8"))
TIERS = {t["id"]: t for t in DATA["tiers"]}
TIER_ORDER = ["default", "bronze", "silver", "gold"]
BADGE_URL = DATA["badge_url"]

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Courier New',monospace"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def starfield(width, height, count, seed=1):
    return "".join(
        f'<circle cx="{(37 * k * k + 91 * k * seed) % width}" cy="{(53 * k + 17 * k * k) % height}" r="{1 + k % 3 * 0.6}" fill="#fff">'
        f'<animate attributeName="opacity" values=".1;1;.1" dur="{2 + k % 5}s" begin="{k % 7 * 0.4}s" repeatCount="indefinite"/></circle>'
        for k in range(1, count)
    )


def hero():
    """Arcade title screen: neon title, perspective grid, filling XP bar, blinking prompt."""
    grid_v = "".join(
        f'<line x1="{600 + (x - 600) * 0.18}" y1="250" x2="{x}" y2="420" stroke="#f778ba" stroke-opacity=".35" stroke-width="1.5"/>'
        for x in range(-600, 1801, 120)
    )
    grid_h = "".join(
        f'<line x1="0" y1="{250 + d}" x2="1200" y2="{250 + d}" stroke="#f778ba" stroke-opacity=".35" stroke-width="1.5">'
        f'<animate attributeName="y1" values="{250 + d};{250 + d * 1.6}" dur="2s" repeatCount="indefinite"/>'
        f'<animate attributeName="y2" values="{250 + d};{250 + d * 1.6}" dur="2s" repeatCount="indefinite"/></line>'
        for d in (6, 18, 38, 68, 110)
    )
    coins = "".join(
        f'<g transform="translate({x} {y})"><circle r="9" fill="#ffd33d" stroke="#d29922" stroke-width="3">'
        f'<animate attributeName="r" values="9;3;9" dur="1.2s" begin="{i * 0.25}s" repeatCount="indefinite"/></circle>'
        f'<animateTransform attributeName="transform" type="translate" values="{x} {y};{x} {y - 10};{x} {y}" dur="2s" begin="{i * 0.3}s" repeatCount="indefinite"/></g>'
        for i, (x, y) in enumerate([(120, 90), (1080, 80), (190, 200), (1010, 190), (70, 300), (1130, 300)])
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-label="Level up your GitHub: collect every achievement">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset=".6" stop-color="#2a1250"/><stop offset="1" stop-color="#5a1e5c"/></linearGradient>
<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd33d"/><stop offset="1" stop-color="#f778ba"/></linearGradient>
<linearGradient id="title" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#79c0ff"/><stop offset=".5" stop-color="#d2a8ff"/><stop offset="1" stop-color="#ffa657"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0;-1 0" dur="8s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="xp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3fb950"/><stop offset="1" stop-color="#a5f3a0"/></linearGradient>
<filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="sunclip"><rect x="0" y="0" width="1200" height="250"/></clipPath>
</defs>
<rect width="1200" height="420" rx="20" fill="url(#sky)"/>
{starfield(1200, 230, 60)}
<g clip-path="url(#sunclip)"><circle cx="600" cy="250" r="120" fill="url(#sun)" opacity=".85"/>
<rect x="470" y="200" width="260" height="6" fill="#2a1250"/><rect x="470" y="218" width="260" height="8" fill="#2a1250"/><rect x="470" y="236" width="260" height="10" fill="#2a1250"/></g>
<rect x="0" y="250" width="1200" height="170" fill="#140a2a"/>
{grid_v}{grid_h}
{coins}
<text x="600" y="62" text-anchor="middle" font-family="{MONO}" font-size="18" font-weight="700" letter-spacing="8" fill="#ffd33d">★ PLAYER 1 ★</text>
<text x="600" y="138" text-anchor="middle" font-family="{SANS}" font-size="74" font-weight="900" fill="url(#title)" filter="url(#glow)">LEVEL UP YOUR</text>
<text x="600" y="214" text-anchor="middle" font-family="{SANS}" font-size="82" font-weight="900" fill="#ffffff" filter="url(#glow)" letter-spacing="4">GITHUB</text>
<g transform="translate(350 300)">
<text x="0" y="-12" font-family="{MONO}" font-size="15" font-weight="700" fill="#a5f3a0">XP</text>
<text x="500" y="-12" text-anchor="end" font-family="{MONO}" font-size="15" font-weight="700" fill="#a5f3a0">NEXT BADGE ▸</text>
<rect width="500" height="24" rx="12" fill="#0d1117" stroke="#3fb950" stroke-width="3"/>
<rect x="4" y="4" width="0" height="16" rx="8" fill="url(#xp)"><animate attributeName="width" values="0;492;492;0" keyTimes="0;.7;.9;1" dur="5s" repeatCount="indefinite"/></rect>
</g>
<text x="600" y="380" text-anchor="middle" font-family="{MONO}" font-size="22" font-weight="700" letter-spacing="6" fill="#ffffff">PRESS ★ TO START<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></text>
</svg>
"""


def quest_map():
    """Five-level journey from first commit to legend, with a runner moving along the road."""
    stops = [
        (110, "LV 1", "ROOKIE", "Quickdraw · YOLO", "#3fb950"),
        (355, "LV 2", "CONTRIBUTOR", "Pull Shark · Pair", "#58a6ff"),
        (600, "LV 3", "MENTOR", "Galaxy Brain", "#d2a8ff"),
        (845, "LV 4", "PATRON", "Public Sponsor", "#f778ba"),
        (1090, "LV 5", "LEGEND", "Starstruck · Gold tiers", "#ffd33d"),
    ]
    road = "M110 110 C230 40 235 180 355 110 S480 40 600 110 S725 180 845 110 S970 40 1090 110"
    nodes = "".join(
        f'<g transform="translate({x} 110)">'
        f'<circle r="34" fill="#0d1117" stroke="{c}" stroke-width="5"/>'
        f'<circle r="34" fill="none" stroke="{c}" stroke-width="2" opacity=".6"><animate attributeName="r" values="34;48" dur="2s" begin="{i * 0.4}s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values=".6;0" dur="2s" begin="{i * 0.4}s" repeatCount="indefinite"/></circle>'
        f'<text y="7" text-anchor="middle" font-family="{MONO}" font-size="18" font-weight="800" fill="{c}">{lv}</text>'
        f'<text y="112" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="800" fill="{c}">{name}</text>'
        f'<text y="138" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="600" fill="#8b949e">{sub}</text></g>'
        for i, (x, lv, name, sub, c) in enumerate(stops)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="270" viewBox="0 0 1200 270" role="img" aria-label="Quest map: Rookie, Contributor, Mentor, Patron, Legend">
<defs><linearGradient id="road" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3fb950"/><stop offset=".25" stop-color="#58a6ff"/><stop offset=".5" stop-color="#d2a8ff"/><stop offset=".75" stop-color="#f778ba"/><stop offset="1" stop-color="#ffd33d"/></linearGradient></defs>
<path d="{road}" fill="none" stroke="url(#road)" stroke-width="10" stroke-linecap="round" opacity=".35"/>
<path d="{road}" fill="none" stroke="url(#road)" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 14"><animate attributeName="stroke-dashoffset" values="32;0" dur="1s" repeatCount="indefinite"/></path>
{nodes}
<g><polygon points="0,-11 3.2,-3.4 11,-3.4 4.8,1.6 7,9.5 0,5 -7,9.5 -4.8,1.6 -11,-3.4 -3.2,-3.4" fill="#ffffff"/>
<animateMotion dur="9s" repeatCount="indefinite" path="{road}" rotate="0"/></g>
</svg>
"""


def divider():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="24" viewBox="0 0 1200 24" preserveAspectRatio="none" role="img" aria-label="">
<defs><linearGradient id="d" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#79c0ff" stop-opacity="0"/><stop offset=".2" stop-color="#79c0ff"/><stop offset=".5" stop-color="#d2a8ff"/><stop offset=".8" stop-color="#ffa657"/><stop offset="1" stop-color="#ffa657" stop-opacity="0"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-.3 0;.3 0;-.3 0" dur="6s" repeatCount="indefinite"/></linearGradient></defs>
<rect x="0" y="10" width="1200" height="4" rx="2" fill="url(#d)"/>
<g fill="#ffd33d"><circle cx="600" cy="12" r="6"><animate attributeName="r" values="4;7;4" dur="1.5s" repeatCount="indefinite"/></circle></g>
</svg>
"""


def tier_legend():
    cells = []
    for n, tid in enumerate(TIER_ORDER):
        t = TIERS[tid]
        x = 20 + n * 200
        cells.append(
            f'<g transform="translate({x} 20)"><rect width="180" height="64" rx="32" fill="{t["color"]}" stroke="{t["dark"]}" stroke-width="3"/>'
            f'<text x="90" y="30" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="800" fill="#24292f">{t["label"]}</text>'
            f'<text x="90" y="50" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="600" fill="#24292f">{t["suffix"] or "base badge"}</text></g>'
        )
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="820" height="104" viewBox="0 0 820 104" role="img" aria-label="Tier legend">{"".join(cells)}</svg>\n'


def badge_urls():
    for a in DATA["achievements"]:
        for tier in TIER_ORDER[: len(a["tiers"])]:
            yield f"{a['id']}-{tier}", BADGE_URL.format(id=a["id"], tier=tier)


def main():
    assets = ROOT / "assets"
    for name, svg in [("hero", hero()), ("quest-map", quest_map()), ("divider", divider()), ("tier-legend", tier_legend())]:
        (assets / f"{name}.svg").write_text(svg, encoding="utf-8")
    for name, url in badge_urls():
        print(f"{name:40} {url}")


if __name__ == "__main__":
    main()
