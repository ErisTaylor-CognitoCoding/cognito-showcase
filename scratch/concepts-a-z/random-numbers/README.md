# Random Numbers — Controlled Unpredictability

> 📺 ***(Short coming Wed 26 Aug 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Operators (green)

---

## What This Block Does

`pick random (1) to (10)` gives you a random whole number between 1 and 10. Different every time.

Without random numbers, games are deterministic — the same thing happens every time. That's not a game, that's a movie.

---

## The Analogy

Rolling a dice. You know the range (1 to 6). You don't know the result. That uncertainty is what makes it interesting.

---

## How It Works — Three Games, Same Block

```
# Pong — random serve angle so the ball never serves the same way twice:
point in direction (pick random 30 to 150)

# Frogger — apple position snapped to the 20px movement grid:
set x to ((pick random -11 to 11) * 20)

# Donkey Kong — the chaos rule (1-in-8 chance a barrel drops down a ladder):
if <(pick random 1 to 8) = 1> then
  [drop down ladder]
end
```

Three games. Three different purposes. Same block.

---

## The Chaos Rule in Donkey Kong

Every barrel has a 1-in-8 chance to drop *down* a ladder instead of rolling past it. That one `pick random 1 to 8` check is what makes the level feel alive. Without it, every barrel behaves identically — you'd memorise the pattern in one run and never lose.

Randomness is a design tool, not a fallback.

---

## In the Arcade Series

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 3 — Frogger →](../../series/ep-03-frogger) · [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders) · [Ep 5 — Donkey Kong →](../../series/ep-05-donkey-kong)

*[← broadcast](../broadcast) · [Back to concepts →](../README.md) · Next: [repeat →](../repeat)*
