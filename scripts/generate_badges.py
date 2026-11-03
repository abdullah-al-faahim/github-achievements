"""Generate every SVG in assets/ from data/achievements.json.

Run from the repository root:  python scripts/generate_badges.py
All artwork is original and drawn here as simple vector shapes; it is a
fan-made interpretation, not GitHub's official badge art.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "achievements.json").read_text(encoding="utf-8"))
TIERS = {t["id"]: t for t in DATA["tiers"]}
TIER_ORDER = ["default", "bronze", "silver", "gold"]

W = "#ffffff"

# Each glyph is drawn inside a 160x160 canvas, centred on (80, 80).
GLYPHS = {
    "star": f'<polygon points="80,44 89.4,67 114,68.9 95.2,84.9 101.2,109 80,96 58.8,109 64.8,84.9 46,68.9 70.6,67" fill="{W}"/>',
    "shark": (
        f'<path d="M58 92 C66 70 78 52 98 46 C92 60 92 76 100 92 Z" fill="{W}"/>'
        f'<path d="M44 100 q9 -8 18 0 t18 0 t18 0 t18 0" fill="none" stroke="{W}" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M50 113 q8 -6 15 0 t15 0 t15 0 t15 0" fill="none" stroke="{W}" stroke-width="4" stroke-linecap="round" opacity=".7"/>'
    ),
    "pair": (
        f'<circle cx="64" cy="64" r="11" fill="{W}"/><circle cx="96" cy="64" r="11" fill="{W}"/>'
        f'<path d="M44 106 a20 20 0 0 1 40 0 Z" fill="{W}"/><path d="M76 106 a20 20 0 0 1 40 0 Z" fill="{W}" opacity=".8"/>'
    ),
    "planet": (
        f'<circle cx="80" cy="80" r="20" fill="{W}"/>'
        f'<ellipse cx="80" cy="80" rx="38" ry="11" fill="none" stroke="{W}" stroke-width="5" transform="rotate(-22 80 80)"/>'
        f'<circle cx="52" cy="52" r="3" fill="{W}"/><circle cx="110" cy="108" r="2.5" fill="{W}"/><circle cx="114" cy="50" r="2" fill="{W}"/>'
    ),
    "bolt": f'<polygon points="88,40 56,86 76,86 70,120 104,72 84,72" fill="{W}"/>',
    "dice": (
        f'<rect x="50" y="50" width="60" height="60" rx="12" fill="none" stroke="{W}" stroke-width="6"/>'
        f'<circle cx="66" cy="66" r="5.5" fill="{W}"/><circle cx="80" cy="80" r="5.5" fill="{W}"/><circle cx="94" cy="94" r="5.5" fill="{W}"/>'
    ),
    "heart": f'<path d="M80 114 C46 92 44 70 54 60 C64 50 76 54 80 64 C84 54 96 50 106 60 C116 70 114 92 80 114 Z" fill="{W}"/>',
    "sleeve": (
        f'<path d="M80 110 C50 90 48 70 57 61 C66 52 76 56 80 65 C84 56 94 52 103 61 C112 70 110 90 80 110 Z" fill="none" stroke="{W}" stroke-width="6" stroke-linejoin="round"/>'
        f'<text x="80" y="92" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="22" font-weight="800" fill="{W}">?</text>'
    ),
    "snow": "".join(
        f'<g transform="rotate({a} 80 80)"><line x1="80" y1="42" x2="80" y2="118" stroke="{W}" stroke-width="5" stroke-linecap="round"/>'
        f'<polyline points="70,50 80,60 90,50" fill="none" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'
        f'<polyline points="70,110 80,100 90,110" fill="none" stroke="{W}" stroke-width="4" stroke-linecap="round"/></g>'
        for a in (0, 60, 120)
    ),
    "heli": (
        f'<line x1="42" y1="52" x2="118" y2="52" stroke="{W}" stroke-width="5" stroke-linecap="round"/>'
        f'<line x1="50" y1="62" x2="110" y2="62" stroke="{W}" stroke-width="4" stroke-linecap="round" opacity=".75"/>'
        f'<line x1="80" y1="52" x2="80" y2="74" stroke="{W}" stroke-width="4"/>'
        f'<rect x="64" y="74" width="32" height="22" rx="6" fill="{W}"/>'
        f'<path d="M66 96 L54 118 M94 96 L106 118 M80 96 L80 116" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'
    ),
    "wand": (
        f'<line x1="52" y1="112" x2="96" y2="68" stroke="{W}" stroke-width="7" stroke-linecap="round"/>'
        f'<polygon points="104,42 108,54 120,58 108,62 104,74 100,62 88,58 100,54" fill="{W}"/>'
        f'<circle cx="62" cy="58" r="3" fill="{W}"/><circle cx="116" cy="92" r="3" fill="{W}"/>'
    ),
    "pro": f'<text x="80" y="92" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="34" font-weight="800" letter-spacing="2" fill="{W}">PRO</text>',
    "code": (
        f'<polyline points="66,58 46,80 66,102" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<polyline points="94,58 114,80 94,102" fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<line x1="86" y1="52" x2="74" y2="108" stroke="{W}" stroke-width="6" stroke-linecap="round"/>'
    ),
    "bug": (
        f'<ellipse cx="80" cy="86" rx="18" ry="24" fill="{W}"/><circle cx="80" cy="58" r="10" fill="{W}"/>'
        f'<path d="M62 76 L46 68 M62 90 L44 90 M64 104 L48 114 M98 76 L114 68 M98 90 L116 90 M96 104 L112 114 M74 50 L68 40 M86 50 L92 40" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'
    ),
    "cap": (
        f'<polygon points="80,50 122,70 80,90 38,70" fill="{W}"/>'
        f'<path d="M56 80 V100 C66 110 94 110 104 100 V80 L80 92 Z" fill="{W}" opacity=".85"/>'
        f'<line x1="116" y1="73" x2="116" y2="100" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'
    ),
    "shield": (
        f'<path d="M80 42 L112 54 V80 C112 100 98 112 80 120 C62 112 48 100 48 80 V54 Z" fill="{W}"/>'
        f'<polyline points="66,82 76,92 96,70" fill="none" stroke="#24292f" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "staff": (
        f'<circle cx="80" cy="64" r="16" fill="{W}"/><path d="M50 116 a30 28 0 0 1 60 0 Z" fill="{W}"/>'
    ),
}


def medallion(item, tier="default", label=None, status="active"):
    """One round badge. `tier` colours the outer ring and adds the xN pill."""
    i = item["id"]
    c1, c2 = item["colors"]
    t = TIERS[tier]
    ring = t["color"] if tier != "default" else "#6e7681"
    ring_dark = t["dark"] if tier != "default" else "#30363d"
    dashed = ' stroke-dasharray="10 7"' if status == "unreleased" else ""
    gray = ' filter="url(#gray-%s)"' % i if status == "retired" else ""
    pill = ""
    if t["suffix"]:
        pill = (
            f'<g transform="translate(112 118)"><rect x="-22" y="-14" width="44" height="28" rx="14" fill="{ring}" stroke="{ring_dark}" stroke-width="3"/>'
            f'<text x="0" y="6" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="17" font-weight="800" fill="#24292f">{t["suffix"]}</text></g>'
        )
    ribbon = ""
    if status in ("retired", "unreleased"):
        word = "RETIRED" if status == "retired" else "UNRELEASED"
        ribbon = (
            f'<rect x="20" y="126" width="120" height="22" rx="11" fill="#24292f" stroke="{W}" stroke-width="2"/>'
            f'<text x="80" y="141.5" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="800" letter-spacing="1.5" fill="{W}">{word}</text>'
        )
    title = label or item["name"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 160 160" role="img" aria-label="{title}">
<title>{title}</title>
<defs>
<radialGradient id="g-{i}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient>
<linearGradient id="r-{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{ring}"/><stop offset="1" stop-color="{ring_dark}"/></linearGradient>
<filter id="gray-{i}"><feColorMatrix type="saturate" values="0.35"/></filter>
</defs>
<g{gray}>
<circle cx="80" cy="80" r="74" fill="url(#r-{i})"{dashed}/>
<circle cx="80" cy="80" r="64" fill="url(#g-{i})" stroke="{ring_dark}" stroke-width="2"{dashed}/>
<path d="M30 62 A52 52 0 0 1 120 38" fill="none" stroke="{W}" stroke-width="5" stroke-linecap="round" opacity=".28"/>
{GLYPHS[item["glyph"]]}
</g>
{pill}{ribbon}
</svg>
"""


def tier_strip(item):
    """All four tiers side by side with their thresholds."""
    cells = []
    for n, (tier, need) in enumerate(zip(TIER_ORDER, item["tiers"])):
        t = TIERS[tier]
        x = n * 180
        svg = medallion(item, tier)
        inner = svg.split("\n", 2)[2].rsplit("</svg>", 1)[0]
        inner = inner.replace(f'-{item["id"]}"', f'-{item["id"]}-{tier}"').replace(f'-{item["id"]})', f'-{item["id"]}-{tier})')
        cells.append(
            f'<g transform="translate({x + 10} 10)">{inner}</g>'
            f'<text x="{x + 90}" y="196" text-anchor="middle" class="t">{t["label"]}</text>'
            f'<text x="{x + 90}" y="218" text-anchor="middle" class="n">{need:,}</text>'
        )
    width = 180 * len(item["tiers"])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="236" viewBox="0 0 {width} 236" role="img" aria-label="{item['name']} tiers">
<style>.t{{font:700 15px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#8b949e}}.n{{font:800 18px 'Segoe UI',Helvetica,Arial,sans-serif;fill:#58a6ff}}</style>
{''.join(cells)}
</svg>
"""


def banner():
    stars = "".join(
        f'<circle cx="{(37 * k * k + 91 * k) % 1200}" cy="{(53 * k + 17 * k * k) % 300}" r="{1 + k % 3 * 0.6}" fill="#fff">'
        f'<animate attributeName="opacity" values=".15;1;.15" dur="{2 + k % 5}s" begin="{k % 7 * 0.4}s" repeatCount="indefinite"/></circle>'
        for k in range(1, 70)
    )
    orbit = []
    active = [a for a in DATA["achievements"] if a["status"] == "active"]
    for n, a in enumerate(active):
        c1, c2 = a["colors"]
        orbit.append(
            f'<g transform="translate({760 + n * 60} {120 + (n % 2) * 70})">'
            f'<circle r="26" fill="{c2}" stroke="{c1}" stroke-width="4"><animate attributeName="r" values="26;28;26" dur="3s" begin="{n * 0.3}s" repeatCount="indefinite"/></circle>'
            f'<g transform="scale(.32) translate(-80 -80)">{GLYPHS[a["glyph"]]}</g></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="GitHub Achievements Showcase">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset=".55" stop-color="#161b45"/><stop offset="1" stop-color="#3b1d60"/></linearGradient>
<linearGradient id="tx" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#79c0ff"/><stop offset=".5" stop-color="#d2a8ff"/><stop offset="1" stop-color="#ffa657"/></linearGradient>
</defs>
<rect width="1200" height="300" rx="18" fill="url(#bg)"/>
{stars}
<text x="60" y="118" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="22" font-weight="700" letter-spacing="6" fill="#8b949e">THE COMPLETE GUIDE</text>
<text x="58" y="182" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="62" font-weight="900" fill="url(#tx)">GitHub Achievements</text>
<text x="60" y="226" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="22" fill="#c9d1d9">Every badge, every tier, and how to unlock it.</text>
{''.join(orbit)}
</svg>
"""


def tier_legend():
    cells = []
    for n, tid in enumerate(TIER_ORDER):
        t = TIERS[tid]
        x = 20 + n * 200
        fill = t["color"] if tid != "default" else "#8b949e"
        cells.append(
            f'<g transform="translate({x} 20)"><rect width="180" height="64" rx="32" fill="{fill}" stroke="{t["dark"]}" stroke-width="3"/>'
            f'<text x="90" y="30" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="18" font-weight="800" fill="#24292f">{t["label"]}</text>'
            f'<text x="90" y="50" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#24292f">{t["suffix"] or "base badge"}</text></g>'
        )
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="820" height="104" viewBox="0 0 820 104" role="img" aria-label="Tier legend">{"".join(cells)}</svg>\n'


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    for a in DATA["achievements"]:
        write(ROOT / "assets" / "badges" / f"{a['id']}.svg", medallion(a, status=a["status"]))
        if len(a["tiers"]) > 1:
            for tier in TIER_ORDER[1:]:
                label = f"{a['name']} {TIERS[tier]['label']}"
                write(ROOT / "assets" / "badges" / f"{a['id']}-{tier}.svg", medallion(a, tier, label))
            write(ROOT / "assets" / "tiers" / f"{a['id']}.svg", tier_strip(a))
    for h in DATA["highlights"]:
        write(ROOT / "assets" / "highlights" / f"{h['id']}.svg", medallion(h))
    write(ROOT / "assets" / "banner.svg", banner())
    write(ROOT / "assets" / "tier-legend.svg", tier_legend())
    print("SVGs written to", ROOT / "assets")


if __name__ == "__main__":
    main()
