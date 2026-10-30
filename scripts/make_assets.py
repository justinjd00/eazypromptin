#!/usr/bin/env python3
"""Generate the README artwork (animated SVGs, dark and light) into assets/.

    python3 scripts/make_assets.py

Pure SVG + CSS animations, no external fonts or scripts, so GitHub renders them inside <img>.
"""
from __future__ import annotations

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(
        bg="#0A0B10", panel="#12141B", line="#262A36", text="#F4F5F7", muted="#8A90A2",
        soft="#C9CDD8", accent="#C8F542", accent2="#9B7BFF", ok="#5BE49B", grid="#FFFFFF", grid_op="0.06",
        glow1="#C8F542", glow2="#7C5CFF",
    ),
    "light": dict(
        bg="#FAFAF7", panel="#FFFFFF", line="#E3E4DF", text="#0F1115", muted="#6B7080",
        soft="#3A3F4B", accent="#4E7A00", accent2="#6A45F5", ok="#11845B", grid="#000000", grid_op="0.07",
        glow1="#C8F542", glow2="#9B7BFF",
    ),
}


def fade_keyframes(name: str, start: float, total: float, hold_end: float = 0.95) -> str:
    """Element invisible until `start` seconds, fades in, stays, fades out at loop end."""
    s = start / total * 100
    e = min(s + 2.5, hold_end * 100 - 1)
    return (
        f"@keyframes {name}{{0%,{s:.2f}%{{opacity:0}}{e:.2f}%,{hold_end*100:.0f}%{{opacity:1}}100%{{opacity:0}}}}"
        f".{name}{{opacity:0;animation:{name} {total}s linear infinite}}"
    )


def defs(t: dict, w: int, h: int) -> str:
    return f"""
  <defs>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.2" fill="{t['grid']}" fill-opacity="{t['grid_op']}"/>
    </pattern>
    <radialGradient id="g1" cx="0.12" cy="0.1" r="0.55">
      <stop offset="0" stop-color="{t['glow1']}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{t['glow1']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="0.9" cy="0.95" r="0.6">
      <stop offset="0" stop-color="{t['glow2']}" stop-opacity="0.24"/>
      <stop offset="1" stop-color="{t['glow2']}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="{t['bg']}"/>
  <rect width="{w}" height="{h}" fill="url(#dots)"/>
  <rect width="{w}" height="{h}" fill="url(#g1)"/>
  <rect width="{w}" height="{h}" fill="url(#g2)"/>"""


def banner(theme: str) -> str:
    t = THEMES[theme]
    w, h, total = 1280, 420, 11.0
    rows = [
        (0.3, t["muted"], ">", "i wanna make a game, dungeon thing, friends"),
        (1.8, t["accent"], "my read", "co-op roguelite, ~20 min runs"),
        (3.2, t["accent2"], "assuming", "laptop GPU · 10 h/week"),
        (4.6, t["soft"], "audit", "14 guesses → 2"),
        (6.0, t["ok"], "✓", "BRIEF.md  PROMPT.md  MILESTONES.md"),
    ]
    css = [fade_keyframes(f"r{i}", s, total) for i, (s, *_ ) in enumerate(rows)]
    css.append("@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}.cursor{animation:blink 1.1s steps(1) infinite}")
    px, py = 760, 88
    lines = []
    for i, (_, color, tag, text) in enumerate(rows):
        y = py + 74 + i * 46
        lines.append(
            f'<g class="r{i}"><text x="{px+28}" y="{y}" font-family="{MONO}" font-size="15" fill="{color}" font-weight="700">{escape(tag)}</text>'
            f'<text x="{px+(28 if tag in (">", "✓") else 128) + (22 if tag in (">", "✓") else 0)}" y="{y}" font-family="{MONO}" font-size="15" fill="{t["text"] if i else t["soft"]}">{escape(text)}</text></g>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="EazyPromptin: reads the intent behind your lazy prompt">
  <title>EazyPromptin</title>
  <style>{''.join(css)}</style>{defs(t, w, h)}
  <text x="80" y="118" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{t['muted']}">AGENT SKILL · OPEN SOURCE · ANY MODEL</text>
  <text x="76" y="212" font-family="{SANS}" font-size="88" font-weight="800" letter-spacing="-3" fill="{t['text']}">eazy<tspan fill="{t['accent']}">promptin</tspan></text>
  <rect class="cursor" x="672" y="146" width="14" height="72" fill="{t['accent']}"/>
  <text x="80" y="272" font-family="{SANS}" font-size="27" fill="{t['soft']}">Reads the intent behind your lazy prompt.</text>
  <text x="80" y="310" font-family="{SANS}" font-size="27" fill="{t['soft']}">Then builds exactly what you meant.</text>
  <rect x="80" y="344" width="56" height="4" fill="{t['accent']}"/>
  <rect x="142" y="344" width="28" height="4" fill="{t['accent2']}"/>
  <rect x="{px}" y="{py}" width="440" height="276" fill="{t['panel']}" fill-opacity="0.92" stroke="{t['line']}"/>
  <rect x="{px}" y="{py}" width="440" height="36" fill="{t['line']}" fill-opacity="0.45"/>
  <text x="{px+20}" y="{py+23}" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{t['muted']}">DEEP MODE · PHASE 2/5</text>
  <circle cx="{px+412}" cy="{py+18}" r="5" fill="{t['accent']}"><animate attributeName="fill-opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/></circle>
  {''.join(lines)}
</svg>
"""


def demo(theme: str) -> str:
    t = THEMES[theme]
    w, h, total = 960, 640, 20.0
    # (start_s, role, color, text)
    seq = [
        (0.3, "you", t["muted"], "i wanna make a game, some dungeon thing with monsters, pixel art, maybe with friends"),
        (1.8, "coach", t["accent"], "MY READ  a couch co-op roguelite you play with 1-2 friends, not a big RPG"),
        (2.6, "", t["soft"], "         why: \"with friends\", \"keep getting stronger\", \"a bit of godot\""),
        (3.4, "", t["soft"], "         could also be: a loot crawler you play for weeks"),
        (5.0, "", t["text"], "A  roguelite runs      B  loot crawler      C  horde survivor      ?  wildcard"),
        (6.4, "", t["text"], "Co-op?  a) local, one screen (recommended)   b) online, 3-5× the work"),
        (8.4, "you", t["muted"], "A. 2b, friends live in other cities"),
        (10.0, "coach", t["accent2"], "ASSUMING  runs on a normal gaming PC · ~5 h/week · Godot 4 + GDScript"),
        (12.0, "you", t["muted"], "laptop with integrated graphics. C# not gdscript. 10h a week. go"),
        (13.8, "coach", t["soft"], "AUDIT  3 simulated readers · 14 guesses → 2, both marked as assumptions"),
        (15.6, "", t["ok"], "✓ BRIEF.md     ✓ PROMPT.md     ✓ MILESTONES.md     M0 = one room, one enemy, online"),
    ]
    css = [fade_keyframes(f"d{i}", s, total) for i, (s, *_ ) in enumerate(seq)]
    css.append("@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}.cursor{animation:blink 1.1s steps(1) infinite}")
    x0, y0 = 40, 40
    out = []
    y = y0 + 92
    for i, (_, role, color, text) in enumerate(seq):
        if role:
            y += 12
        gap = 34 if role else 28
        role_txt = ""
        if role:
            rc = t["muted"] if role == "you" else t["accent"]
            role_txt = f'<text x="{x0+28}" y="{y}" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1.5" fill="{rc}">{role.upper()}</text>'
        weight = "700" if text.split(" ")[0].isupper() and len(text.split(" ")[0]) > 2 else "400"
        out.append(
            f'<g class="d{i}">{role_txt}<text x="{x0+108}" y="{y}" font-family="{MONO}" font-size="14.5" fill="{color}" font-weight="{weight}" xml:space="preserve">{escape(text)}</text></g>'
        )
        y += gap
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="An EazyPromptin session: vague game idea to brief, prompt and milestones">
  <title>EazyPromptin session</title>
  <style>{''.join(css)}</style>{defs(t, w, h)}
  <rect x="{x0}" y="{y0}" width="{w-2*x0}" height="{h-2*y0}" fill="{t['panel']}" fill-opacity="0.94" stroke="{t['line']}"/>
  <rect x="{x0}" y="{y0}" width="{w-2*x0}" height="44" fill="{t['line']}" fill-opacity="0.45"/>
  <text x="{x0+24}" y="{y0+28}" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{t['text']}" font-weight="700">eazy<tspan fill="{t['accent']}">promptin</tspan></text>
  <text x="{x0+170}" y="{y0+28}" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{t['muted']}">/ deep mode / game.md</text>
  <rect x="{w-x0-150}" y="{y0+14}" width="128" height="16" fill="none" stroke="{t['line']}"/>
  <rect x="{w-x0-150}" y="{y0+14}" width="128" height="16" fill="{t['accent']}" fill-opacity="0.85">
    <animate attributeName="width" values="0;26;26;52;52;77;77;102;102;128;128;0" keyTimes="0;0.08;0.25;0.33;0.5;0.58;0.68;0.74;0.8;0.86;0.98;1" dur="{total}s" repeatCount="indefinite"/>
  </rect>
  {''.join(out)}
  <rect class="cursor" x="{x0+108}" y="{y-8}" width="9" height="16" fill="{t['accent']}"/>
</svg>
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for theme in THEMES:
        (OUT / f"banner-{theme}.svg").write_text(banner(theme), encoding="utf-8")
        (OUT / f"demo-{theme}.svg").write_text(demo(theme), encoding="utf-8")
        print(f"wrote assets/banner-{theme}.svg, assets/demo-{theme}.svg")


if __name__ == "__main__":
    main()
