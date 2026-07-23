# `turtle.digDown()` — dig a hole with one word

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/cfFXAYphEes?feature=share)**

**Series:** [Minecraft CC:Tweaked Shorts](../README.md) · **Lane:** Fri Minecraft Short · Ep 4

`turtle.digDown()` breaks the single block directly beneath the turtle — one word, one block. That's a dent. To dig a real hole you pair it with `turtle.down()` inside a loop: the turtle breaks the block below, drops into it, and repeats. Add a matching `up()` loop at the end and it climbs back to the surface.

## The command

```lua
turtle.digDown()   -- breaks exactly one block below the turtle
```

## The hole (full loop)

```lua
-- ep04 : turtle.digDown()
-- one word = one block. a hole needs a loop.

for i = 1, 10 do
  turtle.digDown()  -- break the block below
  turtle.down()     -- drop into it
end

for i = 1, 10 do
  turtle.up()       -- climb back to the top
end
```

See [`ep04_turtle_digdown.lua`](./ep04_turtle_digdown.lua) for the runnable file.

## What you need first

Fuel. `turtle.down()` and `turtle.up()` each cost 1 fuel — 20 moves for this 10-deep shaft. Put coal in a slot and run `turtle.refuel()` before you start, or the turtle digs one block and sits there dead.

**Pre-req:** [CC:Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) installed (free on CurseForge / Modrinth).

[← back to Minecraft concepts](../README.md)
