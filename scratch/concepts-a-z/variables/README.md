# variables — A Named Box That Remembers a Number

> 📺 **12 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 12 Aug 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A scoreboard. It doesn't care about the past — it just shows the current number. Someone scores, the number goes up. Someone loses a life, the number goes down. The box remembers whatever you put in last.

That's a variable.

---

## What it does

A variable is a named storage location. Give it a name (`score`, `lives`, `speed`, `y-velocity`) and a starting value. Change it whenever something happens. Read it whenever you need to know the current state.

In Scratch:
- `set [score] to [0]` — initialise
- `change [score] by [1]` — increment
- `show variable [score]` — display on screen
- `if [score] > [100]` — use in a condition

---

## Variables make games dynamic

Without variables, every game session is identical. With variables, the score increases, lives decrease, speed ramps up, gravity accelerates. Variables are the memory of the game.

Every game in this series uses them. Gravity in Donkey Kong is a `y-velocity` variable changing every frame. The direction of the alien formation in Space Invaders is a variable flipping between 1 and -1. The snake's length in Snake is a variable tracking the list size.

---

## Where it appears in the series

- [Snake →](../../series/ep-02-snake) — score, snake length
- [Space Invaders →](../../series/ep-04-space-invaders) — lives, alien count, direction flag
- [Donkey Kong →](../../series/ep-05-donkey-kong) — y-velocity (gravity), score
- [Asteroids →](../../series/ep-07-asteroids) — vx and vy (vector velocity)

---

*[← Back to concepts](../README.md) · Next: [broadcast →](../broadcast)*
