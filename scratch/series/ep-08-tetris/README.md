# Episode 8 — Tetris

> 📺 *(coming 17 Jul 2026)*

**Series:** Scratch Arcade Series  
**Live Scratch Project:** *(link coming 17 Jul 2026)*

---

## What We Built

Tetris — pieces fall, you rotate them, full lines clear. The board fills. The speed increases. You lose when you run out of space.

This is the most data-heavy game in the series. The board isn't a visual — it's a **2D grid stored as a list**. Every cell is either empty or filled. The game reads the list and draws accordingly.

---

## Headline Concept: 2D Arrays (Lists of Lists)

### The analogy

Think of a spreadsheet. Rows and columns. Each cell has a row number and a column number. In Tetris, every tile on the board is a cell. To check if row 3, column 5 is filled: look up entry `[(3 × width) + 5]` in a single flat list. One list represents the entire 2D grid.

### How line clearing works

Scan each row. If every cell in that row is filled, delete those entries from the list and insert empty cells at the top. The whole board shifts down — no sprites moved, just list entries reshuffled.

### Piece rotation

Each tetromino is defined as four coordinate offsets from a centre point. Rotating 90° swaps the x and y offsets according to a rotation rule. Seven pieces × four rotations = 28 stored shapes, all as lists of offsets.

### Blocks used in this episode

- `replace item [n] of [board] with [1]` — mark cell filled
- `item [n] of [board]` — read cell state
- `delete [n] of [board]` — line clear
- `insert [0] at [1] of [board]` — add empty row at top
- `repeat [width]` — scan a row
- Variables `[piece-x]`, `[piece-y]`, `[rotation]` — active piece state
- `broadcast [line-clear]` — trigger score update

---

## Concepts in this episode

- [variables →](../../concepts-a-z/variables)
- [repeat →](../../concepts-a-z/repeat)
- [if-then-else →](../../concepts-a-z/if-then-else)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [broadcast →](../../concepts-a-z/broadcast)
- [wait →](../../concepts-a-z/wait)

---

*[← Back to episode guide](../README.md)*
