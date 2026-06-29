# if-then-else — Two Paths, One Decision

> 📺 **9 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 9 Sep 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A fork in the road. You look at the signpost. If the condition is true, take the left path. If it's false, take the right path. You always take one of them — never both, never neither.

---

## What it does

`if [condition] then ... else ...` — the condition is checked once. If it's true, the "then" blocks run. If it's false, the "else" blocks run. Either way, execution continues below.

The basic `if [condition] then` has no else — if the condition is false, nothing happens and the script continues. The `if-then-else` block guarantees *something* always happens either way.

---

## Where games use it

**Gravity landing in Donkey Kong:**

- If touching platform → set y-velocity to 0 (landed)
- Else → change y-velocity by -1 (still falling)

Two states, one check, every frame.

**Ghost mode in Pac-Man:**

- If fright timer has run out → switch costume to normal, restore chase behaviour
- Else → keep blue costume, run away from Pac-Man

**Rock size after split in Asteroids:**

- If rock is large → create two medium clones
- Else if rock is medium → create two small clones
- Else → just delete (small rocks disappear)

---

## Where it appears in the series

- [Donkey Kong →](../../series/ep-05-donkey-kong) — gravity vs landing logic
- [Pac-Man →](../../series/ep-06-pac-man) — ghost behaviour mode switching
- [Asteroids →](../../series/ep-07-asteroids) — rock size after collision
- [Tetris →](../../series/ep-08-tetris) — piece rotation direction

---

*[← Back to concepts](../README.md) · Next: [wait →](../wait)*
