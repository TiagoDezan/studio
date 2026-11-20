// "Bug Hunt": a tiny original arcade shooter that lives inside the hero card.
// The noob's glasses defend the code from a swarm of descending bugs.

type Labels = { help: string; helpTouch: string; over: string; again: string; wave: string };

const PLAYER = [
  '.###.....###.',
  '#...#####...#',
  '#...#...#...#',
  '#..b#...#..b#',
  '.###.....###.',
];
// a little beetle with antennae, two walking frames
const BUG = [
  [
    '.#.....#.',
    '..#...#..',
    '...###...',
    '#.#####.#',
    '.###.###.',
    '#.#####.#',
    '...#.#...',
  ],
  [
    '#.......#',
    '.#.....#.',
    '...###...',
    '.#######.',
    '#.##.##.#',
    '.#######.',
    '#..#.#..#',
  ],
];
const W = 200;

export function mountBugHunt(card: HTMLElement, labels: Labels) {
  const canvas = document.createElement('canvas');
  canvas.className = 'bh-canvas';
  canvas.setAttribute('aria-label', 'Bug Hunt');
  const ctx = canvas.getContext('2d')!;
  const overlay = document.createElement('div');
  overlay.className = 'bh-overlay pixel';
  const quit = document.createElement('button');
  quit.type = 'button';
  quit.className = 'bh-quit pixel';
  quit.textContent = '×';
  quit.setAttribute('aria-label', card.dataset.quit || 'Quit');

  const hudL = card.querySelector<HTMLElement>('.hud-tl')!;
  const hudR = card.querySelector<HTMLElement>('.hud-tr')!;
  const hudB = card.querySelector<HTMLElement>('.hud-b')!;
  const original = { l: hudL.textContent, r: hudR.textContent, b: hudB.innerHTML };

  const touch = matchMedia('(pointer: coarse)').matches;
  let H = 200;
  let hi = 0;
  try { hi = Number(localStorage.getItem('np_bughunt_hi') || 0); } catch {}

  let colors = { ink: '#fff', blue: '#32ccfe', faint: '#66727b' };
  const readColors = () => {
    const cs = getComputedStyle(card);
    colors = { ink: cs.getPropertyValue('--text').trim() || '#fff', blue: cs.getPropertyValue('--blue').trim() || '#32ccfe', faint: cs.getPropertyValue('--faint').trim() || '#888' };
  };

  // game state
  let running = false, over = false, raf = 0, last = 0, visible = true;
  let score = 0, lives = 3, wave = 1;
  let px = 0, targetX: number | null = null;
  const keys = { left: false, right: false, fire: false };
  let fireQueued = false;
  let shots: { x: number; y: number }[] = [];
  let bombs: { x: number; y: number }[] = [];
  let bugs: { x: number; y: number; alive: boolean; blue: boolean }[] = [];
  let swarmDir = 1, stepTimer = 0, frame = 0, bombTimer = 0, cooldown = 0, hitFlash = 0;
  let particles: { x: number; y: number; vx: number; vy: number; t: number }[] = [];

  const pad = (n: number) => String(n).padStart(5, '0');
  const hud = () => {
    hudL.textContent = `1UP ${pad(score)}`;
    hudR.textContent = `HI ${pad(Math.max(hi, score))}`;
    hudB.textContent = `${labels.wave} ${wave} · ${'♥'.repeat(Math.max(0, lives))}`;
  };

  const size = () => {
    const r = card.getBoundingClientRect();
    H = Math.round((W * r.height) / r.width);
    canvas.width = W;
    canvas.height = H;
  };

  const spawnWave = () => {
    bugs = [];
    const cols = 7, rows = 4;
    const x0 = (W - (cols - 1) * 18 - 9) / 2;
    for (let r = 0; r < rows; r++)
      for (let c = 0; c < cols; c++)
        bugs.push({ x: x0 + c * 18, y: 26 + r * 13, alive: true, blue: r === 0 });
    swarmDir = 1; stepTimer = 0; bombs = []; shots = [];
  };

  const reset = () => {
    score = 0; lives = 3; wave = 1; over = false;
    px = W / 2; particles = [];
    spawnWave();
    overlay.hidden = true;
    hud();
  };

  const sprite = (rows: string[], x: number, y: number, ink: string, accent = colors.blue) => {
    for (let j = 0; j < rows.length; j++)
      for (let i = 0; i < rows[j].length; i++) {
        const c = rows[j][i];
        if (c === '.') continue;
        ctx.fillStyle = c === 'b' ? accent : ink;
        ctx.fillRect(Math.round(x + i), Math.round(y + j), 1, 1);
      }
  };

  const burst = (x: number, y: number) => {
    for (let i = 0; i < 10; i++) particles.push({ x, y, vx: (Math.random() - 0.5) * 70, vy: (Math.random() - 0.7) * 70, t: 0.5 });
  };

  const gameOver = () => {
    over = true;
    if (score > hi) { hi = score; try { localStorage.setItem('np_bughunt_hi', String(hi)); } catch {} }
    overlay.innerHTML = `<b>${labels.over}</b><span>${pad(score)}</span><small>${labels.again}</small>`;
    overlay.hidden = false;
    hud();
  };

  const update = (dt: number) => {
    // player
    const speed = 110;
    if (targetX !== null) px += Math.max(-speed * dt, Math.min(speed * dt, targetX - px));
    if (keys.left) px -= speed * dt;
    if (keys.right) px += speed * dt;
    px = Math.max(8, Math.min(W - 8, px));
    cooldown -= dt;
    if ((keys.fire || fireQueued || (touch && targetX !== null)) && cooldown <= 0 && shots.length < 2) {
      shots.push({ x: px, y: H - 14 });
      cooldown = 0.28;
      fireQueued = false;
    }
    for (const s of shots) s.y -= 170 * dt;
    shots = shots.filter((s) => s.y > -4);

    // swarm moves in steps, faster as it shrinks and with each wave
    const alive = bugs.filter((b) => b.alive);
    const interval = Math.max(0.03, (0.3 - wave * 0.03) * (alive.length / bugs.length) + 0.03);
    stepTimer += dt;
    if (stepTimer >= interval) {
      stepTimer = 0;
      frame ^= 1;
      const minX = Math.min(...alive.map((b) => b.x)), maxX = Math.max(...alive.map((b) => b.x + 9));
      if ((swarmDir > 0 && maxX + 3 > W - 4) || (swarmDir < 0 && minX - 3 < 4)) {
        swarmDir *= -1;
        for (const b of bugs) b.y += 6;
      } else for (const b of bugs) b.x += 3 * swarmDir;
    }

    // bugs drop errors
    bombTimer -= dt;
    if (bombTimer <= 0 && alive.length) {
      bombTimer = Math.max(0.35, 1.2 - wave * 0.12) * (0.6 + Math.random() * 0.8);
      const cols = new Map<number, (typeof alive)[number]>();
      for (const b of alive) { const k = Math.round(b.x); const cur = cols.get(k); if (!cur || b.y > cur.y) cols.set(k, b); }
      const shooters = [...cols.values()];
      const s = shooters[Math.floor(Math.random() * shooters.length)];
      bombs.push({ x: s.x + 4, y: s.y + 7 });
    }
    for (const b of bombs) b.y += (55 + wave * 6) * dt;
    bombs = bombs.filter((b) => b.y < H + 4);

    // collisions
    for (const s of shots)
      for (const b of alive)
        if (b.alive && s.x >= b.x && s.x <= b.x + 9 && s.y >= b.y && s.y <= b.y + 7) {
          b.alive = false; s.y = -10; score += b.blue ? 30 : 10; burst(b.x + 4, b.y + 3);
        }
    for (const b of bombs)
      if (b.x >= px - 7 && b.x <= px + 7 && b.y >= H - 12 && b.y <= H - 6) {
        b.y = H + 10; lives--; hitFlash = 0.4; burst(px, H - 9);
        if (lives <= 0) return gameOver();
      }
    if (alive.some((b) => b.alive && b.y + 7 >= H - 14)) { lives = 0; return gameOver(); }
    if (!bugs.some((b) => b.alive)) { wave++; score += 50; spawnWave(); }

    for (const p of particles) { p.x += p.vx * dt; p.y += p.vy * dt; p.vy += 120 * dt; p.t -= dt; }
    particles = particles.filter((p) => p.t > 0);
    hitFlash = Math.max(0, hitFlash - dt);
    hud();
  };

  const draw = () => {
    ctx.clearRect(0, 0, W, H);
    for (const b of bugs) if (b.alive) sprite(BUG[frame], b.x, b.y, b.blue ? colors.blue : colors.ink);
    ctx.fillStyle = colors.blue;
    for (const s of shots) ctx.fillRect(Math.round(s.x), Math.round(s.y), 1, 3);
    ctx.fillStyle = colors.ink;
    for (const b of bombs) { const y = Math.round(b.y); ctx.fillRect(Math.round(b.x), y, 1, 1); ctx.fillRect(Math.round(b.x) + 1, y + 1, 1, 1); ctx.fillRect(Math.round(b.x), y + 2, 1, 1); }
    for (const p of particles) { ctx.fillStyle = Math.random() > 0.5 ? colors.blue : colors.ink; ctx.fillRect(Math.round(p.x), Math.round(p.y), 1, 1); }
    if (!(hitFlash > 0 && Math.floor(hitFlash * 20) % 2)) sprite(PLAYER, px - 6, H - 11, colors.ink);
    ctx.fillStyle = colors.faint;
    ctx.fillRect(0, H - 4, W, 1);
  };

  const loop = (t: number) => {
    raf = 0;
    if (!running) return;
    const dt = Math.min(0.05, (t - last) / 1000 || 0);
    last = t;
    if (visible && !document.hidden && !over) update(dt);
    draw();
    raf = requestAnimationFrame(loop);
  };

  const onKey = (e: KeyboardEvent, down: boolean) => {
    if (!running) return;
    const k = e.key;
    if (k === 'ArrowLeft' || k === 'a' || k === 'A') keys.left = down;
    else if (k === 'ArrowRight' || k === 'd' || k === 'D') keys.right = down;
    else if (k === ' ' || e.code === 'Space' || k === 'Spacebar' || k === 'ArrowUp' || k === 'w' || k === 'W') { keys.fire = down; if (down) fireQueued = true; }
    else if (k === 'Escape' && down) return stop();
    else if (k === 'Enter' && down && over) return reset();
    else return;
    e.preventDefault();
    targetX = null;
  };
  const kd = (e: KeyboardEvent) => onKey(e, true);
  const ku = (e: KeyboardEvent) => onKey(e, false);

  const toLocal = (e: PointerEvent) => {
    const r = canvas.getBoundingClientRect();
    return ((e.clientX - r.left) / r.width) * W;
  };
  const pm = (e: PointerEvent) => { if (e.pointerType !== 'mouse' || e.buttons || !touch) targetX = toLocal(e); };
  const pd = (e: PointerEvent) => {
    if ((e.target as HTMLElement).closest('.bh-quit')) return;
    if (over) { reset(); return; }
    targetX = toLocal(e);
    if (cooldown <= 0 && shots.length < 2) { shots.push({ x: px, y: H - 14 }); cooldown = 0.32; }
    if (e.pointerType !== 'mouse') canvas.setPointerCapture?.(e.pointerId);
  };
  const pu = (e: PointerEvent) => { if (e.pointerType !== 'mouse') targetX = null; };

  const io = new IntersectionObserver(([en]) => (visible = en.isIntersecting));
  const ro = new ResizeObserver(() => { if (running) size(); });

  function start() {
    if (running) return;
    readColors();
    card.classList.add('playing');
    card.append(canvas, overlay, quit);
    size();
    reset();
    hudB.textContent = touch ? labels.helpTouch : labels.help;
    running = true;
    last = performance.now();
    addEventListener('keydown', kd);
    addEventListener('keyup', ku);
    canvas.addEventListener('pointermove', pm);
    canvas.addEventListener('pointerdown', pd);
    overlay.addEventListener('pointerdown', pd);
    canvas.addEventListener('pointerup', pu);
    io.observe(card);
    ro.observe(card);
    canvas.tabIndex = 0;
    canvas.focus({ preventScroll: true });
    setTimeout(() => { if (running && !over) hud(); }, 2200);
    raf = requestAnimationFrame(loop);
  }

  function stop() {
    running = false;
    if (raf) cancelAnimationFrame(raf);
    removeEventListener('keydown', kd);
    removeEventListener('keyup', ku);
    io.disconnect();
    ro.disconnect();
    canvas.remove(); overlay.remove(); quit.remove();
    card.classList.remove('playing');
    hudL.textContent = original.l;
    hudR.textContent = hi ? `HI ${pad(hi)}` : original.r;
    hudB.innerHTML = original.b;
    card.querySelector<HTMLElement>('.press-start')?.focus({ preventScroll: true });
  }

  quit.addEventListener('click', stop);
  if (hi) hudR.textContent = `HI ${pad(hi)}`;
  return { start, stop };
}
