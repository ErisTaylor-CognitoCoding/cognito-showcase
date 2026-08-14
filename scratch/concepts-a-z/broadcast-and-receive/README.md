# `broadcast-and-receive` — How Sprites Talk to Each Other

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/fN3hD4fYHrU?feature=share)**

🎮 **[Play the project on Scratch →](https://scratch.mit.edu/projects/1365762442/)**

---

How sprites talk to each other in Scratch.

One sprite shouts a message. Every sprite with a matching `when I receive` block hears it — at the exact same moment. Nobody queues. The sender never names the receivers.

---

## The blocks

**`broadcast [message]`** — sends a message out to the whole project. The sprite sending it doesn't name anyone. It just shouts.

**`when I receive [message]`** — sits in any sprite, listening. The moment that message arrives, everything stacked underneath runs.

One `broadcast` block can trigger ten sprites simultaneously. Add an eleventh sprite and the original sender's script doesn't change by a single block.

---

## When to use it

- **Game Over** — one sprite detects the losing condition, broadcasts "Game Over", every other sprite stops
- **Level Up** — broadcast triggers a scene change, new enemies, a fanfare — all at once
- **Start** — a controller sprite kicks everything off with one broadcast rather than timing each sprite separately

---

## Remix it on Scratch

Open the [project →](https://scratch.mit.edu/projects/1365762442/) and try:
1. Add a fourth sprite
2. Give it a `when I receive [Game Over]` block
3. Notice: the broadcasting sprite's script doesn't change at all

---

*[← Back to concepts](../README.md)*
