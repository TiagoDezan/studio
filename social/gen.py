"""Builds the Noob Perdido Studio Instagram slides (1080x1350) from HTML with Playwright."""
import json, sys, html
from pathlib import Path

ROOT = Path('/home/claude/social')
A = 'file:///home/claude/social/a/'
FONTS = (ROOT / 'fonts/fonts.css').read_text()

CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;background:#05070a;overflow:hidden}
body{font-family:Manrope,sans-serif;color:#fff;position:relative}
.bgpat{position:absolute;inset:0;background:url(%(A)spattern.svg) center/900px auto repeat;opacity:.035}
.glow{position:absolute;width:900px;height:900px;border-radius:50%%;filter:blur(120px);opacity:.22;background:#32ccfe;right:-420px;top:-420px}
.glow.b{left:-460px;bottom:-460px;right:auto;top:auto;opacity:.12}
.frame{position:absolute;inset:0;padding:56px 60px 52px;display:flex;flex-direction:column}
header{display:flex;justify-content:space-between;align-items:center;height:56px;flex:none}
header img{height:46px}
.tag{font-family:'Press Start 2P';font-size:17px;color:#32ccfe;border:3px solid #32ccfe;padding:12px 16px 10px;letter-spacing:1px}
main{flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px;padding:30px 0 24px;min-height:0}
footer{display:flex;justify-content:space-between;align-items:center;height:40px;flex:none;font-weight:600;font-size:22px;color:#8a98a8}
footer .n{font-family:'Press Start 2P';font-size:16px;color:#32ccfe}
h1{font-family:'Press Start 2P';font-weight:400;font-size:50px;line-height:1.38;letter-spacing:-1px}
h1.xl{font-size:64px}
h1.sm{font-size:40px}
h1 .b,.b{color:#32ccfe}
h2{font-family:'Press Start 2P';font-weight:400;font-size:30px;line-height:1.45;color:#32ccfe}
p{font-size:36px;line-height:1.42;color:#d9e2ea}
p.lead{font-size:40px;font-weight:600;color:#fff}
p.small{font-size:28px;color:#8a98a8}
.media{border-radius:26px;overflow:hidden;border:3px solid rgba(50,204,254,.35);flex:1;min-height:0;position:relative}
.media img{width:100%%;height:100%%;object-fit:cover;display:block}
.phones{display:flex;gap:28px;justify-content:center;align-items:flex-start;flex:1;min-height:0;overflow:hidden}
.phones img{height:100%%;max-height:900px;border-radius:36px;border:3px solid rgba(50,204,254,.45);box-shadow:0 20px 60px rgba(0,0,0,.6)}
ul.list{list-style:none;display:flex;flex-direction:column;gap:26px}
ul.list li{font-size:38px;font-weight:600;display:flex;gap:26px;align-items:baseline;line-height:1.3}
ul.list li:before{content:'';flex:none;width:18px;height:18px;background:#32ccfe;transform:translateY(-4px)}
ul.list li small{display:block;font-size:28px;font-weight:400;color:#8a98a8;margin-top:6px}
.steps{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.step{border:3px solid rgba(50,204,254,.5);padding:30px 28px;min-height:230px;background:rgba(50,204,254,.05)}
.step .k{font-family:'Press Start 2P';color:#32ccfe;font-size:22px}
.step h3{font-family:'Press Start 2P';font-weight:400;font-size:26px;margin:22px 0 16px;line-height:1.4}
.step p{font-size:27px;line-height:1.35;color:#b8c4cf}
.grid{display:grid;gap:22px}
.cell{background:rgba(255,255,255,.04);border:2px solid rgba(50,204,254,.3);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:22px 10px 18px;gap:14px}
.cell img{image-rendering:pixelated;width:150px;height:150px;object-fit:contain}
.cell span{font-family:'Press Start 2P';font-size:15px;color:#cfe6f1;text-align:center;line-height:1.5}
.px{image-rendering:pixelated}
.chips{display:flex;flex-wrap:wrap;gap:14px}
.chip{font-family:'Press Start 2P';font-size:16px;padding:12px 16px 10px;background:#32ccfe;color:#05070a}
.chip.o{background:transparent;color:#32ccfe;border:2px solid #32ccfe}
.quote{border-left:10px solid #32ccfe;padding:10px 0 10px 34px;font-size:46px;font-weight:800;line-height:1.3;font-style:italic}
.row{display:flex;gap:40px;align-items:center}
.cta{font-family:'Press Start 2P';font-size:24px;background:#32ccfe;color:#05070a;padding:24px 26px 20px;align-self:flex-start;line-height:1.5}
.status{font-family:'Press Start 2P';font-size:16px;color:#05070a;background:#ffcc33;padding:10px 14px 8px;align-self:flex-start}
.status.ok{background:#4dffa6}
.center{align-items:center;text-align:center}
""" % {'A': A}


def page(tag, body, n=None, total=None, extra=''):
    num = f'<span class="n">{n}/{total} {"▶" if n < total else ""}</span>' if total and total > 1 else '<span></span>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>
<div class="bgpat"></div><div class="glow"></div><div class="glow b"></div>
<div class="frame"><header><img src="{A}logo-w.svg"><span class="tag">{tag}</span></header>
<main>{body}</main>
<footer><span>studio.noobperdido.com</span>{num}</footer></div></body></html>"""


def img(src, cls='', style=''):
    return f'<img class="{cls}" src="{A}{src}" style="{style}">'


POSTS = json.loads((ROOT / 'posts.json').read_text())


def render(only=None):
    hd = ROOT / 'html'
    hd.mkdir(exist_ok=True)
    for post in POSTS:
        if only and post['id'] not in only:
            continue
        slides = post.get('slides', [])
        for i, s in enumerate(slides, 1):
            body = s['html'].replace('{A}', A)
            (hd / f"{post['id']}-{i}.html").write_text(page(s.get('tag', post['tag']), body, i, len(slides), s.get('css', '')))


if __name__ == '__main__':
    render(sys.argv[1:] or None)
