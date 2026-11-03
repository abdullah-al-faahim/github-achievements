"""Generate the banner and tier legend in assets/ from data/achievements.json.

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


def banner():
    stars = "".join(
        f'<circle cx="{(37 * k * k + 91 * k) % 1200}" cy="{(53 * k + 17 * k * k) % 300}" r="{1 + k % 3 * 0.6}" fill="#fff">'
        f'<animate attributeName="opacity" values=".15;1;.15" dur="{2 + k % 5}s" begin="{k % 7 * 0.4}s" repeatCount="indefinite"/></circle>'
        for k in range(1, 70)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="GitHub Achievements Showcase">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset=".55" stop-color="#161b45"/><stop offset="1" stop-color="#3b1d60"/></linearGradient>
<linearGradient id="tx" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#79c0ff"/><stop offset=".5" stop-color="#d2a8ff"/><stop offset="1" stop-color="#ffa657"/></linearGradient>
</defs>
<rect width="1200" height="300" rx="18" fill="url(#bg)"/>
{stars}
<text x="600" y="118" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="22" font-weight="700" letter-spacing="6" fill="#8b949e">THE COMPLETE GUIDE</text>
<text x="600" y="182" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="66" font-weight="900" fill="url(#tx)">GitHub Achievements</text>
<text x="600" y="226" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="22" fill="#c9d1d9">Every badge, every tier, and how to unlock it.</text>
</svg>
"""


def tier_legend():
    cells = []
    for n, tid in enumerate(TIER_ORDER):
        t = TIERS[tid]
        x = 20 + n * 200
        cells.append(
            f'<g transform="translate({x} 20)"><rect width="180" height="64" rx="32" fill="{t["color"]}" stroke="{t["dark"]}" stroke-width="3"/>'
            f'<text x="90" y="30" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="18" font-weight="800" fill="#24292f">{t["label"]}</text>'
            f'<text x="90" y="50" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13" font-weight="600" fill="#24292f">{t["suffix"] or "base badge"}</text></g>'
        )
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="820" height="104" viewBox="0 0 820 104" role="img" aria-label="Tier legend">{"".join(cells)}</svg>\n'


def badge_urls():
    for a in DATA["achievements"]:
        for tier in TIER_ORDER[: len(a["tiers"])]:
            yield f"{a['id']}-{tier}", BADGE_URL.format(id=a["id"], tier=tier)


def main():
    (ROOT / "assets" / "banner.svg").write_text(banner(), encoding="utf-8")
    (ROOT / "assets" / "tier-legend.svg").write_text(tier_legend(), encoding="utf-8")
    for name, url in badge_urls():
        print(f"{name:40} {url}")


if __name__ == "__main__":
    main()
