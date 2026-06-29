# Coding Snake — Episode 2

> 📺 **[Watch on YouTube →](https://youtu.be/8qaxgK9FrbM)**

🎮 **[Play the project on Scratch →](https://scratch.mit.edu/projects/1328679090)**

---

## What we built

Snake — the classic game — rebuilt block by block in Scratch. The headline trick is using a **list** to remember every position the snake has ever visited. That list IS the snake. Every step, the head adds a new position to the end; if you didn't eat, the oldest position is deleted from the front. The body sprites are clones that draw themselves at each coordinate pair in the list.

---

## Block coding concepts covered

### Lists — storing the snake's body

A `Snake` list holds every body position as coordinate pairs (x, y, x, y…). This is the architecture of the whole game.

> **`add (x position) to [Snake]`** + **`add (y position) to [Snake]`** — before the head moves, we remember where it just was. Two adds because every position is a pair.

### Clones — one sprite, many copies

The Snake Body sprite uses `create clone of myself` to stamp a copy at each coordinate pair in the list. One sprite, unlimited body segments on screen.

> **`when I start as a clone → go to x: (item i of Snake) y: (item i+1 of Snake) → show`**

### Direction blocking — the "can't reverse" rule

You can't turn straight back into yourself. Right key does nothing while the snake is moving left. This is the classic 1997 Snake rule.

> **`if key [right arrow] pressed and not Direction = 2`** — only turn right if not currently going left.

### Grid-snapping — `× 20`

The apple picks a random cell then multiplies by 20 to land on the same pixel grid the snake moves on. Without this, the apple floats between squares and can never be eaten.

> **`set x to (pick random -11 to 11) × 20`**

### Modulo — pulling digits out of the score

`Score mod 10` gives just the ones digit (e.g. 47 mod 10 = 7), which selects the right costume for the score display. Same costume-font trick from Pong Ep 1.

---

## Remix it on Scratch

Open the project, click **See Inside**, and try the challenge:

> **Make the snake speed up every 5 apples eaten.** Change `wait 0.1 seconds` to `wait (Speed) seconds`, where Speed starts at 0.1 and shrinks a little each time the snake eats. How high a score can you reach before it's unplayable?

[Fork the project on Scratch →](https://scratch.mit.edu/projects/1328679090)

---

← [Back to Scratch series](../README.md)
