# Coding Tetris — Ep 8 (2D Arrays, Rotation, Line Clearing)

> 📺 **[Watch on YouTube →](https://youtu.be/jzBlCuoY1HY)**

**Series:** Scratch Arcade Series  
🎮 **[Play the project on Scratch →](https://scratch.mit.edu/projects/1362768609/)**

---

## What We Built

Tetris — properly retro-accurate. The headline trick is the 10×20 grid stored as a flat Scratch list with `row × 10 + col` index math — once you see that pattern, you can store any 2D world in a Scratch list. Add proper rotation via offset-table lookups, real line clearing that rewrites the grid in place, and NES-accurate drop-speed scaling all the way to the kill-screen.

---

## Block Coding Concepts Covered

| Block | What it does |
|---|---|
| `replace item [n] of [Grid]` | Writes a colour into one cell of the board |
| `item [n] of [Grid]` | Reads whether a cell is filled — the board read |
| `delete [n] of [Grid]` | Removes a row when a line clears |
| `insert [0] at [1] of [Grid]` | Adds a blank row at the top after a line clear |
| `repeat [width]` | Scans one row checking whether every cell is filled |
| Variables `[piece-x]` `[piece-y]` `[rotation]` | Track the active piece position and orientation |
| `broadcast [line-clear]` | Tells the score sprite to update after a line clears |
| `create clone of [Playfield]` | Stamps 200 individual cell sprites onto the board in one go |

---

## The Big Insight

A 2D grid in a 1D list: `index = row × 10 + col`. NES Tetris used this same trick in 1989. Once you see it, every grid-based project — chess boards, dungeon maps, Pac-Man mazes — looks the same.

---

## Remix It on Scratch

[Remix the project →](https://scratch.mit.edu/projects/1362768609/)

Challenge: add a **ghost piece** — the translucent shadow showing where the active piece would land on a hard drop. Then turn it OFF and play without it. Drop a 🧩 in the comments with your highest level without the ghost.

---

*[← Back to Scratch Arcade Series](../README.md)*
