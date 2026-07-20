# `turtle.forward()` + `turnLeft()` + `turnRight()` — walk and turn

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/nEzpFaMe9AY)**

**Lane:** Minecraft ComputerCraft Shorts (CC:Tweaked · Lua)

---

## The Concept

Walk one way. Turn. Walk another.

`turtle.forward()` moves your turtle one block ahead — wherever it's facing. `turtle.turnLeft()` and `turtle.turnRight()` spin it 90 degrees on the spot, no movement involved.

Combine them and you've got directional control. Forward. Left. Forward. Right. Forward. That's an L-shaped path — three commands, and your turtle's already navigating.

Everywhere your turtle will ever go — even in massive auto-farms — is built from these three commands.

---

## The Code

See [`ep02_walk_turn.lua`](./ep02_walk_turn.lua) — the exact code from the episode.

```lua
-- ep02 : forward + turnLeft + turnRight
-- coal in slot 16 — refuel first if empty

turtle.forward()
turtle.turnLeft()
turtle.forward()
turtle.turnRight()
turtle.forward()
```

---

## Pre-req

Install [CC:Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) from CurseForge or Modrinth (free).

---

*[← back to Minecraft concepts](../README.md)*
