# Snail Sort — Traverse a Matrix in a Clockwise Spiral

**Source:** [Codewars — 4 kyu](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1)
**Category:** Algorithmic
**Difficulty:** Intermediate
**Estimated time:** 1–2 hr

> Nothing makes you think about arrays spatially like a clockwise spiral — and the moment the pattern clicks the solution almost writes itself. Classic "aha" kata.

## The challenge

Given an n×n 2D array, return all elements arranged from outermost to centre, travelling clockwise — like a snail's shell. The kata is [4 kyu on Codewars](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1) with 85,000+ completions: well-trodden enough to have great discussion, but tricky enough to make you think spatially. The solution fits in under 20 lines once the pattern clicks.

## Approach

> 🚧 Zero's walkthrough notes land here after the YouTube video ships.

## Solution

> 🚧 Solution code coming soon — Zero will push it via `/work [Code] → Git`.

## Concepts used

- **2D array traversal** — moving through a grid using indices to control direction rather than relying on nested loops alone
- **Clockwise spiral** — tracking direction changes (right → down → left → up) to peel one complete ring off the matrix per cycle
- **Layer-by-layer reduction** — each pass strips the outermost ring and works inward until the array is empty
- **Edge-case handling** — correctly terminating when the matrix is empty (`[]`) or the final ring is a single element

[← back to challenges index](../../README.md)
