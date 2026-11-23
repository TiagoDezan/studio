"""Content of the Dec 2026 / Jan 2027 Instagram plan for @studio.noobperdido (English)."""
import json

HT_DEV = '#gamedev #indiedev #indiegame #pixelart #devlog #iosgames #madewithswift #noobperdido'
HT_GAMES = '#indiegame #iosgames #mobilegames #puzzlegame #gamedev #indiedev #noobperdido'
HT_KIDS = '#educationalgames #mathgames #kidsapps #homeschool #parenting #iosgames #noobperdido'
HT_STUDIO = '#appdevelopment #webdevelopment #startup #saas #iosdev #noobperdido'

P = []


def post(id, date, kind, tag, caption, slides=None, ig_type='POST', media=None):
    P.append(dict(id=id, date=date, kind=kind, tag=tag, caption=caption.strip(), slides=slides or [], ig_type=ig_type, media=media or []))


def phones(*srcs, h=820):
    return '<div class="phones">' + ''.join(f'<img src="{{A}}{s}" style="height:{h}px">' for s in srcs) + '</div>'


PH = 'border-radius:36px;border:3px solid rgba(50,204,254,.45)'

# 1 ─ Hello
post('01-hello-v2', '2026-12-02T20:00:00', 'Studio', 'HELLO, WORLD', """
Hi, we're Noob Perdido Studio 👓

We build apps, websites, custom systems and games. And now we help businesses use AI without the hype.

Swipe to see:
• what we do
• how we work, in four levels
• what you'll find here every week

We work in English, Spanish and Portuguese. 🇬🇧 🇪🇸 🇧🇷

Lost with your idea? We'll find the way. Tell us about it at studio.noobperdido.com (link in bio).

#noobperdido #gamedev #indiedev #appdevelopment #startup #iosdev
""", [
    dict(html="""<div style="display:flex;flex-direction:column;gap:56px;align-items:flex-start">
<img src="{A}glasses.svg" style="width:520px;filter:drop-shadow(0 0 40px rgba(50,204,254,.5))">
<h1 class="xl">HI, WE'RE<br><span class="b">NOOB PERDIDO</span><br>STUDIO</h1>
<p class="lead">Lost with your idea?<br>We'll find the way.</p><p class="small">English · Español · Português</p></div>"""),
    dict(html="""<h1>WHAT<br><span class="b">WE DO</span></h1>
<ul class="list">
<li><div>iPhone and Android apps<small>Native, fast and App Store ready</small></div></li>
<li><div>Websites that convert<small>Beautiful, light and built to sell</small></div></li>
<li><div>Custom systems and SaaS<small>From internal dashboards to full products</small></div></li>
<li><div>Mobile games<small>Ours and yours</small></div></li>
<li><div>AI consulting<small>No hype, no jargon</small></div></li></ul>"""),
    dict(html="""<h1 class="sm">FOUR LEVELS,<br><span class="b">NO SURPRISE</span><br>BOSS FIGHT</h1>
<div class="steps">
<div class="step"><span class="k">LEVEL 1</span><h3>Chat</h3><p>We learn the idea, the audience and the budget.</p></div>
<div class="step"><span class="k">LEVEL 2</span><h3>Prototype</h3><p>You see and tap it before investing big.</p></div>
<div class="step"><span class="k">LEVEL 3</span><h3>Build</h3><p>Weekly deliveries, no black box.</p></div>
<div class="step"><span class="k">LEVEL 4</span><h3>Launch</h3><p>We ship it and stay with you after.</p></div></div>"""),
    dict(html="""<h1>EVERY WEEK<br><span class="b">RIGHT HERE</span></h1>
<ul class="list">
<li><div>Monday: Nexus devlog<small>Our action RPG in development</small></div></li>
<li><div>Wednesday: Our games<small>Block Quest and Operation Absolute Zero</small></div></li>
<li><div>Friday: Studio<small>Case studies, behind the scenes and AI</small></div></li></ul>
<div class="chips"><span class="chip o">WE SPEAK</span><span class="chip">ENGLISH</span><span class="chip">ESPAÑOL</span><span class="chip">PORTUGUÊS</span></div>
<div class="cta">TELL US YOUR IDEA ▶<br>STUDIO.NOOBPERDIDO.COM</div>"""),
])

# 2 ─ Our games
post('02-our-games', '2026-12-03T20:00:00', 'Games', 'OUR GAMES', """
Three games, one studio 🎮

🛰️ Nexus: Last Signal: a pixel art action RPG for iPhone and iPad. In development, with a devlog every Monday.
🧮 Operation Absolute Zero: young spies save the world network by hacking firewalls with math. Ages 7 to 12, no ads.
🧩 Block Quest: The Lost Jewel: a block puzzle across five magical worlds. Out now on the App Store.

Which one do you want to see first? Tell us in the comments 👇

""" + HT_GAMES, [
    dict(html="""<h1 class="xl">OUR<br><span class="b">GAMES</span></h1>
<div class="row" style="justify-content:space-between">
<img src="{A}nexus-icon.jpg" style="width:290px;border-radius:64px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}zero-icon.png" style="width:290px;border-radius:64px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}en-bq-1.jpg" style="width:290px;height:290px;object-fit:cover;object-position:50% 22%;border-radius:64px;border:3px solid rgba(50,204,254,.5)"></div>
<p class="lead">One in development.<br>Two ready to play.</p>"""),
    dict(html="""<span class="status">IN DEVELOPMENT</span>
<h1 class="sm">NEXUS:<br><span class="b">LAST SIGNAL</span></h1>
<div class="media" style="flex:0 0 520px"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 30%"></div>
<p>Action RPG for iPhone and iPad. 3/4 pixel art, hybrid combat and 8 chapters.</p>"""),
    dict(html="""<span class="status ok">READY</span>
<h1 class="sm">OPERATION<br><span class="b">ABSOLUTE ZERO</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:stretch">
<img src="{A}en-zero-1.jpg" style="height:800px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:28px;justify-content:center"><p>Math becomes a spy mission.</p><p class="small">Ages 7–12 · 300 missions · no ads</p></div></div>"""),
    dict(html="""<span class="status ok">OUT NOW</span>
<h1 class="sm">BLOCK QUEST:<br><span class="b">THE LOST JEWEL</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:stretch">
<img src="{A}en-bq-2.jpg" style="height:800px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:28px;justify-content:center"><p>Fit pieces, clear lines and beat each level's mission.</p><p class="small">5 worlds · no ads · no timers</p></div></div>"""),
])

# 3 ─ Block Quest Reel
post('03-bq-reel', '2026-12-04T20:00:00', 'Games', 'BLOCK QUEST', """
Block Quest: The Lost Jewel in 30 seconds 🧩✨

Fit pieces on an 8×8 board, clear lines and beat each level's mission. Emerald Forest, Fire Valley, Crystal Ocean, Celestial Kingdom and more.

✔️ No ads
✔️ No timers
✔️ Chapter 1 free

Out now for iPhone and iPad. Link in bio.

""" + HT_GAMES, ig_type='REEL', media=['03-bq-reel.mp4'])

# 4 ─ Devlog #1
post('04-devlog-1', '2026-12-07T20:00:00', 'Devlog', 'DEVLOG #1', """
Devlog #1 · Nexus: Last Signal 🛰️

Year 2479. Humanity crosses the stars through the Nexus, a network of alien gates. Seventeen years ago, the first colony, New Aurora, vanished without a distress call.

Now a signal has come from there. The message says only one thing:
"The door was never meant to open."

Nexus: Last Signal is our action RPG for iPhone and iPad: 3/4 pixel art, hybrid combat and 8 chapters. Every Monday we'll share a piece of its development here.

Turn on notifications so you don't miss the signal 📡

""" + HT_DEV, [
    dict(html="""<div class="media"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 25%"></div>
<h1>NEXUS:<br><span class="b">LAST SIGNAL</span></h1>"""),
    dict(html="""<h1 class="xl">YEAR<br><span class="b">2479.</span></h1>
<p class="lead">Humanity crosses the stars through the Nexus, a network of alien gates.</p>
<p>Seventeen years ago, the first colony, New Aurora, vanished without a distress call. Others followed.</p>
<div class="media" style="flex:0 0 330px"><img src="{A}G01_art_bible_a.jpg" style="object-position:85% 70%"></div>"""),
    dict(html="""<h1>THE <span class="b">SIGNAL</span></h1>
<p>Benjamin, a former AEGIS agent, receives a message from New Aurora:</p>
<div class="quote">"The door was never meant to open."</div>
<div class="row" style="justify-content:center;gap:60px;margin-top:20px">
<img class="px" src="{A}portrait_benjamin.png" style="width:300px">
<img class="px" src="{A}portrait_orion.png" style="width:300px"></div>"""),
    dict(html="""<h1>WHAT'S<br><span class="b">COMING</span></h1>
<ul class="list">
<li>Pixel art in 3/4 perspective</li>
<li>Hybrid combat: weapons, dodge and skills</li>
<li>8 chapters, 8 bosses</li>
<li>iPhone and iPad, with iCloud saves</li></ul>
<div class="row" style="justify-content:space-between">
<img class="px" src="{A}portrait_benjamin.png" style="width:200px"><img class="px" src="{A}portrait_isabela.png" style="width:200px">
<img class="px" src="{A}portrait_orion.png" style="width:200px"><img class="px" src="{A}portrait_survivor.png" style="width:200px"></div>"""),
])

# 5 ─ Operation Absolute Zero
post('05-absolute-zero', '2026-12-09T20:00:00', 'Games', 'ABSOLUTE ZERO', """
Operation Absolute Zero 🧮🕵️

Cipher-Zero, a mischievous AI, has hacked the world network. Only a team of young spies can break its shields, and their weapon is math.

• 300 missions across 3 operations
• Difficulty adapts to each child
• Parent dashboard to follow every skill
• No ads, no purchases, no data collection

For kids aged 7 to 12, on iPhone and iPad. Tag a parent who needs to see this 👇

""" + HT_KIDS, [
    dict(html="""<div class="media"><img src="{A}zero-cipher.jpg" style="object-position:50% 45%"></div>
<h1 class="sm">OPERATION<br><span class="b">ABSOLUTE ZERO</span></h1>
<p class="lead">Math becomes a mission.</p>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}en-zero-1.jpg" style="height:960px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:30px"><h2>HACK WITH MATH</h2><p>Young spies break firewalls by building equations to stop a rogue AI.</p></div></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<div style="display:flex;flex-direction:column;gap:30px"><h2>300 MISSIONS</h2><p>Three operations, from an abandoned subway to the cloud. The difficulty grows with the child.</p></div>
<img src="{A}en-zero-2.jpg" style="height:960px;""" + PH + """"></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}en-zero-3.jpg" style="height:960px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:30px"><h2>PARENT DASHBOARD</h2><p>See what your child has mastered and where they need practice.</p><p class="small">No ads. No data leaves the device.</p></div></div>"""),
])

# 6 ─ Case Reunio
post('06-case-reunio', '2026-12-11T20:00:00', 'Studio', 'CASE STUDY', """
Case study: Reunio ⛪📱

@app.reunio was born inside a real church, from the system we built for @iglesiapresbiteriana.alhaurin (Iglesia Semilla de Vida). Today it's a SaaS serving several churches on the web, iPhone and Android.

What we delivered:
• Members, full treasury, rotas and announcements
• Push notifications
• Spanish, Portuguese and English, with dark mode
• App live on the App Store

Have an idea that could become a product like this? DM us or visit studio.noobperdido.com.

""" + HT_STUDIO, [
    dict(html="""<h1>CASE STUDY:<br><span class="b">REUNIO</span></h1>
<p class="lead">From one church to many.</p>
<div class="media" style="flex:0 0 520px;background:#0b0d10"><img src="{A}reunio-1.webp" style="object-fit:contain"></div>
<p>Church management on web, iPhone and Android.</p>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}en-reunio-1.jpg" style="height:960px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:30px"><h2>HOW IT STARTED</h2><p>It began as the management system for Iglesia Semilla de Vida and grew into a SaaS for many churches.</p><p class="small">Web · iPhone · Android</p></div></div>"""),
    dict(html="""<h1>WHAT WE<br><span class="b">DELIVERED</span></h1>
<ul class="list"><li>Members, treasury, rotas and announcements</li><li>Push notifications</li><li>Spanish, Portuguese and English</li><li>Live on the App Store</li></ul>
<div class="chips"><span class="chip o">REACT</span><span class="chip o">TYPESCRIPT</span><span class="chip o">SUPABASE</span><span class="chip o">SWIFTUI</span></div>
<div class="cta">GOT AN IDEA LIKE THIS? ▶<br>TALK TO US</div>"""),
])

# 7 ─ Devlog #2 Benjamin
post('07-devlog-2', '2026-12-14T20:00:00', 'Devlog', 'DEVLOG #2', """
Devlog #2 · Meet Benjamin 🎨

Former AEGIS special operations agent, 30. Quiet, observant, decides fast. He's the one who receives the signal from New Aurora.

Swipe to follow his path into the game:
1. Concept: the armor, the visor and the palette
2. Turnaround: front, back and side, so he looks the same from every angle
3. Sprite: the pixel art you control on your iPhone

Which part of the process should we show in the next devlog?

""" + HT_DEV, [
    dict(html="""<div class="media"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 20%"></div>
<h1>MEET<br><span class="b">BENJAMIN</span></h1>"""),
    dict(html="""<h2>1 CONCEPT ▶ 2 TURNAROUND</h2>
<p>Front, back and side drawn together, so the character looks the same from every angle.</p>
<div class="media" style="flex:0 0 auto;background:#ff00ff"><img src="{A}G02_benjamin_turnaround.jpg" style="height:auto"></div>
<p class="small">The pink background is on purpose: it gets removed when the art becomes a sprite.</p>"""),
    dict(html="""<h2>3 SPRITE</h2>
<p>The pixel art you control: idle, walking, running and interacting.</p>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;align-items:center">
<div style="width:880px;height:220px;background:url({A}benjamin_south_idle.png) 0 0/880px 220px no-repeat;image-rendering:pixelated"></div>
<div style="width:960px;height:160px;background:url({A}benjamin_east_run.png) 0 0/960px 160px no-repeat;image-rendering:pixelated"></div></div>"""),
])

# 8 ─ Block Quest worlds
post('08-bq-worlds', '2026-12-16T20:00:00', 'Games', 'BLOCK QUEST', """
Five worlds. One lost jewel. 💎🧩

In Block Quest: The Lost Jewel you fit pieces on an 8×8 board, clear lines and beat each level's mission, from the Emerald Forest to the Celestial Kingdom.

• Fair by design: pieces are dealt so no level is impossible because of bad luck
• No ads and no timers, play at your own pace
• Chapter 1 is free

Which world would you start with? 👇

Out now on iPhone and iPad. Link in bio.

""" + HT_GAMES, [
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<img src="{A}en-bq-1.jpg" style="height:980px;""" + PH + """">
<h1 class="sm">FIVE <span class="b">WORLDS.</span> ONE LOST JEWEL.</h1></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<div style="display:flex;flex-direction:column;gap:30px"><h2>8×8 BOARD</h2><p>Fit pieces, clear lines and beat each level's mission.</p></div>
<img src="{A}en-bq-2.jpg" style="height:980px;""" + PH + """"></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<img src="{A}en-bq-4.jpg" style="height:980px;""" + PH + """">
<div style="display:flex;flex-direction:column;gap:30px"><h2>FAIR BY DESIGN</h2><p>Pieces are dealt so no level is impossible because of bad luck.</p></div></div>"""),
    dict(html="""<h1>5 WORLDS.<br><span class="b">YOUR PACE.</span></h1>
""" + phones('en-bq-3.jpg', 'en-bq-5.jpg', 'en-bq-6.jpg', h=640) + """
<div class="chips"><span class="chip">NO ADS</span><span class="chip">NO TIMERS</span><span class="chip">CHAPTER 1 FREE</span></div>"""),
])

# 9 ─ AI without the hype
post('09-ai-no-hype', '2026-12-18T20:00:00', 'Studio', 'AI', """
AI without the hype 🤖

No jargon, no miracle promises. We find where AI saves time and money in your business, plug it into the tools you already use and train your team.

Five ways to start:
1. AI assessment
2. Assistants and agents
3. Automation and integration
4. AI inside your product
5. Team training

Want to know where AI makes sense for you? Talk to us at studio.noobperdido.com.

""" + HT_STUDIO, [
    dict(html="""<h1 class="xl">AI<br><span class="b">NO HYPE</span></h1>
<p class="lead">We find where AI saves time and money in your business.</p>
<img src="{A}glasses.svg" style="width:420px;align-self:flex-end;opacity:.9">"""),
    dict(html="""<h1 class="sm">FIVE WAYS<br><span class="b">TO START</span></h1>
<ul class="list">
<li><div>AI assessment<small>Where it pays off, and where it doesn't</small></div></li>
<li><div>Assistants and agents<small>Support and repetitive tasks</small></div></li>
<li><div>Automation and integration<small>With the tools you already use</small></div></li>
<li><div>AI inside your product<small>New features for your customers</small></div></li>
<li><div>Team training<small>For everyday work</small></div></li></ul>"""),
    dict(html="""<h1>WHERE TO<br><span class="b">START?</span></h1>
<p class="lead">A short assessment shows where AI makes a difference in your business.</p>
<p>No long contracts, no jargon.</p>
<div class="cta">TALK TO US ▶<br>STUDIO.NOOBPERDIDO.COM</div>"""),
])

# 10 ─ Devlog #3 skills and arsenal
SK = [('skill_emp.png', 'EMP PULSE'), ('skill_energy_shield.png', 'SHIELD'), ('skill_nexus_surge.png', 'NEXUS SURGE'),
      ('skill_precision_shot.png', 'PRECISION'), ('skill_emergency_recovery.png', 'RECOVERY'), ('skill_energy_burst.png', 'ENERGY BURST')]
IT = [('item_plasma_pistol.png', 'PLASMA PISTOL'), ('item_pulse_rifle.png', 'PULSE RIFLE'), ('item_heavy_blaster.png', 'HEAVY BLASTER'),
      ('item_nova_cannon.png', 'NOVA CANNON'), ('item_aegis_vest.png', 'AEGIS VEST'), ('item_reactor_core.png', 'REACTOR CORE')]


def grid(items, cols=3):
    return f'<div class="grid" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(
        f'<div class="cell"><img src="{{A}}{s}"><span>{n}</span></div>' for s, n in items) + '</div>'


post('10-devlog-3', '2026-12-21T20:00:00', 'Devlog', 'DEVLOG #3', """
Devlog #3 · Skills and arsenal ⚡🔫

Combat in Nexus is hybrid: two equipped weapons, dodge and skills, all on your iPhone screen. Every icon here became 64×64 pixel art for the game.

Swipe to see some of Benjamin's skills and gear.

Question of the day: which one do you take on the first mission? Vote in our stories 👀

""" + HT_DEV, [
    dict(html="""<h1>SKILLS AND<br><span class="b">ARSENAL</span></h1>
<p>Two equipped weapons, dodge and skills.</p>""" + grid(SK)),
    dict(html="""<h2>ARSENAL</h2><p>Every item becomes a 64×64 pixel icon in the game.</p>""" + grid(IT)),
    dict(html="""<h1>WHICH ONE<br><span class="b">DO YOU TAKE</span><br>ON THE MISSION?</h1>""" + grid(SK[:3]) + """<p class="lead">Vote in our stories 👀</p>"""),
])

# 11 ─ Holidays
post('11-holidays', '2026-12-23T20:00:00', 'Games', 'HAPPY HOLIDAYS', """
A gift that teaches 🎄🧮

Operation Absolute Zero turns math into a spy mission for kids aged 7 to 12.

No ads, no purchases, no data collection, and a parent dashboard to follow every skill. A different way to spend the holidays playing and learning.

Happy holidays from everyone at Noob Perdido 💙

""" + HT_KIDS, [
    dict(html="""<h1>A GIFT<br><span class="b">THAT TEACHES</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:center;justify-content:center;gap:40px">
<img src="{A}zero-icon.png" style="width:380px;border-radius:84px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}en-zero-1.jpg" style="height:720px;border-radius:32px;border:3px solid rgba(50,204,254,.45)"></div>
<div class="chips"><span class="chip">AGES 7–12</span><span class="chip">NO ADS</span><span class="chip o">HAPPY HOLIDAYS</span></div>"""),
])

# 12 ─ Year in review
post('12-year-in-review', '2026-12-28T20:00:00', 'Studio', '2026 RECAP', """
2026 in pixels 👾

The year Noob Perdido became a studio:
• Block Quest: The Lost Jewel launched on the App Store
• Operation Absolute Zero finished
• Reunio live on the App Store, serving several churches
• The Semilla de Vida system running every single day
• The Nexus: Last Signal engine up and running, from combat to iCloud saves
• A new studio website in three languages

Thank you to everyone who played, tested and trusted our work. There's more coming in 2027 💙

#noobperdido #yearinreview #gamedev #indiedev #appdevelopment
""", [
    dict(html="""<h1 class="xl">2026<br><span class="b">IN PIXELS</span></h1>
<p class="lead">The year Noob Perdido became a studio.</p>
<img src="{A}glasses.svg" style="width:460px;align-self:center;margin-top:40px">"""),
    dict(html="""<h2>WHAT HAPPENED</h2>
<ul class="list">
<li>Block Quest launched on the App Store</li>
<li>Operation Absolute Zero finished</li>
<li>Reunio live on the App Store</li>
<li>Semilla de Vida in production every day</li>
<li>The Nexus engine up, from combat to iCloud</li>
<li>A new website in three languages</li></ul>"""),
    dict(html="""<h1>THANKS FOR<br><span class="b">PLAYING</span><br>WITH US</h1>
<p class="lead">More is coming in 2027.</p>
<div class="row" style="justify-content:space-between;margin-top:30px">
<img src="{A}nexus-icon.jpg" style="width:280px;border-radius:60px"><img src="{A}zero-icon.png" style="width:280px;border-radius:60px">
<img src="{A}en-bq-1.jpg" style="width:280px;height:280px;object-fit:cover;object-position:50% 22%;border-radius:60px"></div>"""),
])

# 13 ─ 2027
post('13-signal-2027', '2026-12-30T20:00:00', 'Devlog', 'NEXUS', """
2027: the signal grows stronger 📡

Next up for Nexus: Last Signal is Chapter 1, The Fallen City. It's where Benjamin reaches New Aurora to find out who sent the signal.

Devlogs keep coming every Monday. Turn on notifications and come along.

Happy New Year 🎆

""" + HT_DEV, [
    dict(html="""<div class="media" style="flex:0 0 760px"><img src="{A}nexus-icon.jpg" style="object-position:50% 45%"></div>
<h1>2027:<br>THE SIGNAL<br><span class="b">GROWS STRONGER</span></h1>"""),
])

# 14 ─ Case Semilla (January)
post('14-case-semilla', '2027-01-08T20:00:00', 'Studio', 'CASE STUDY', """
Case study: Iglesia Semilla de Vida 🌱

For @iglesiapresbiteriana.alhaurin, a church in Spain, we built the website and their church management system:
• Members and role-based permissions
• Treasury with PDF reports
• A native iPhone app

It runs in production every day, and it's where @app.reunio was born.

Is your organization still running on spreadsheets? We can fix that. studio.noobperdido.com

""" + HT_STUDIO, [
    dict(html="""<h1>CASE STUDY:<br><span class="b">SEMILLA DE VIDA</span></h1>
<div class="media" style="background:#3e4c59;display:flex;align-items:center;justify-content:center"><img src="{A}semilla-logo.svg" style="width:80%;height:auto;object-fit:contain"></div>
<p class="lead">Website, system and app for a church in Spain.</p>"""),
    dict(html="""<h2>WHAT WE BUILT</h2>
<div class="media" style="flex:0 0 480px"><img src="{A}semilla-sge.svg"></div>
<ul class="list"><li>Members and role-based permissions</li><li>Treasury with PDF reports</li><li>A native iPhone app</li></ul>"""),
    dict(html="""<h1>IN PRODUCTION<br><span class="b">EVERY DAY</span></h1>
<p class="lead">And it's where Reunio was born.</p>
<div class="chips"><span class="chip o">REACT</span><span class="chip o">SUPABASE</span><span class="chip o">SWIFTUI</span><span class="chip o">DOCKER</span></div>
<div class="cta">STILL ON SPREADSHEETS? ▶<br>TALK TO US</div>"""),
])

json.dump(P, open('/home/claude/social/posts.json', 'w'), ensure_ascii=False, indent=1)
print(len(P), 'posts', sum(len(p['slides']) for p in P), 'slides')
