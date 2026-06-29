# Episode 4 — Coding Space Invaders

> 📺 **[Watch on YouTube →](https://youtu.be/mVugtGz6oL0)** · 🎮 **[Open in Scratch →](https://scratch.mit.edu/projects/1331615967/)**

**Series:** Scratch Arcade Games
**Headline concept:** Cloning — one sprite becomes a 55-alien formation

---

## What We Built

Space Invaders — the iconic 5×11 formation of 55 aliens, the accelerating heartbeat, three alien bullet types, four destructible bunkers, and a mystery UFO crossing the top. Arcade-faithful in Scratch.

---

## The Headline Trick — the Swarm Has No Brain

One Invader sprite spawns 55 clones at startup. There's no formation controller — no central brain telling each alien where to be.

Instead, every clone reads two shared variables:
- `Formation DX` — which direction the formation is moving
- `Animation Frame` — which of two costumes to show

When the formation controller broadcasts `formation step`, all 55 clones move by `Formation DX` simultaneously and switch costume. The formation moves as one, out of pure shared state.

**Edge detection is distributed.** When *any* clone hits the edge, it sets a shared `Edge Hit Flag`. The controller checks that flag once per cycle and reverses the formation direction. Multiple clones can trigger it in the same step — the flag is only read once, so it's safe.

---

## The Tempo Formula

```
Formation Step = Initial Step × (Aliens Left / 55)
```

One line. Fewer aliens alive = shorter wait between steps = faster formation. The last alien moves at terrifying speed. This is the formula that creates the iconic panic of the Space Invaders endgame.

---

## Other Key Ideas

**Single-bullet limit** — the original 1978 mechanic. Only one player bullet on screen at a time. Forces you to aim instead of spray.

**Destructible bunkers** — each bunker is ~22 tiny clones, each a small green square. When a bullet hits one, that clone deletes itself. The eroded shield shapes appear automatically — no pre-drawn art needed.

**Front-line firing** — only the alien in each column with no other alien below it can fire. A script scans the alive/dead grid list, finds the bottom alien per column, fires from there. That's why you can shelter behind a cluster.

---

## Coding Concepts in This Episode

- `create clone of [myself]` — spawning the 55-alien formation
- Shared variables (`Formation DX`, `Animation Frame`) — collective movement with no central brain
- `Formation Step × (Aliens Left / 55)` — the tempo formula
- `broadcast [formation step] and wait` — synchronised formation steps
- Lists as grids — the `Alien Grid` list tracks alive/dead by row and column

---

**Concept deep-dives:** [broadcast →](../../concepts-a-z/broadcast) · [variables →](../../concepts-a-z/variables) · [repeat →](../../concepts-a-z/repeat)

*[← Ep 3](../ep-03-frogger) · [Back to episode guide →](../README.md) · [Next: Ep 5 →](../ep-05-donkey-kong)*
