# arrow-keys — Keyboard Input

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/SXK-c77k0JM)**

---

## The Analogy

A TV remote. Press the button, something happens on screen. Release it, the thing stops. Arrow keys are the simplest form of player input: four buttons, four directions.

---

## What it does

Scratch can check whether any key is currently pressed using `key [name] pressed?`. This is a boolean — it's either true or false right now. Put it inside a `forever` loop and the game checks the keyboard 30 times per second.

Common pattern: inside `forever`, check `if key [right arrow] pressed`, then `change x by [5]`. Sprite moves right while you hold the key. Release it, the condition is false, movement stops.

---

## Two ways to handle input

**Polling (what most games use):** Put `if key [arrow] pressed` inside a `forever` loop. Check the state every frame. Smooth, continuous movement for platformers and shooters.

**Event blocks:** `when [right arrow] key pressed` fires once per keypress, not continuously. Better for turn-based games or menu navigation where you want one action per press.

---

## Where it appears in the series

- [Pong →](../../series/ep-01-pong) — two players, two sets of keys (arrows + WASD)
- [Donkey Kong →](../../series/ep-05-donkey-kong) — left/right movement and jump
- [Asteroids →](../../series/ep-07-asteroids) — rotate and thrust

---

*[← Back to concepts](../README.md) · Next: [forever-loop →](../forever-loop)*
