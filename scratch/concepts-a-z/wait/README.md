# wait — Pause Before Doing the Next Thing

> 📺 **16 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 16 Sep 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A traffic light. The light turns red — you stop. After a set amount of time, it turns green — you go. The `wait` block is that red light. Nothing in that script moves until the timer runs out.

---

## What it does

`wait [N] secs` pauses the current script for N seconds. Scripts in other sprites keep running. Only the script containing the `wait` block pauses.

This is essential for anything time-based: delays between events, animation pacing, spawn intervals, invincibility frames.

---

## `wait` vs `forever`

The `forever` block runs as fast as possible — up to 30 times per second. Sometimes you need things to happen slower than that. `wait [0.5]` inside a loop makes something happen twice a second, not 30 times.

---

## Where games use it

**Staggering enemy spawns in Frogger:**

Cars in a lane appear one at a time with random gaps between them, not all at once. Each clone waits a random interval before starting its glide.

**Explosion animation timing:**

Switch to explosion costume, wait a fraction of a second, switch to next frame, wait again, then hide. Without `wait`, all three costume switches happen in the same frame — invisible to the player.

**Invincibility frames after being hit:**

Set invincible flag to true, wait 2 seconds, set it back to false. The player flashes during those 2 seconds and can't be hit again.

**Ghost scatter timer in Pac-Man:**

Ghosts chase for 20 seconds, scatter for 7, chase again. `wait [20]` then `broadcast [scatter]`. Timing the modes is what creates the rhythm of the game.

---

## Where it appears in the series

- [Frogger →](../../series/ep-03-frogger) — staggered car spawns
- [Space Invaders →](../../series/ep-04-space-invaders) — alien fire rate control
- [Pac-Man →](../../series/ep-06-pac-man) — ghost scatter and chase timer
- [Tetris →](../../series/ep-08-tetris) — piece drop speed scaling

---

*[← Back to concepts](../README.md)*
