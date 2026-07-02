# `turtle.refuel()` + `turtle.place()` — your robot's first block

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/H7q7i1xO6XE)**

**Lane:** Minecraft ComputerCraft Shorts (CC:Tweaked · Lua)

---

## The Concept

Three words. Your first block.

Before a CC:Tweaked turtle does anything, it needs fuel. Drop coal into slot 1 and run `turtle.refuel()` — the turtle burns it for energy. Then swap to slot 2 (your building blocks) and call `turtle.place()`. The block appears directly in front of the turtle. Two commands and your robot's already building.

`turtle.placeUp()` stacks a block above the turtle's head instead. Same idea, different face.

---

## The Code

See [`turtle.lua`](./turtle.lua) in this folder — the exact code from the episode.

```lua
-- Ep 01: wake the turtle + place your first block
-- Slot 1: coal (fuel). Slot 2: building blocks.
turtle.select(1)
turtle.refuel()
turtle.select(2)
turtle.place()
```

---

## Pre-req

Install [CC:Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) from CurseForge or Modrinth (free).

---

*[← back to Minecraft concepts](../README.md)*
