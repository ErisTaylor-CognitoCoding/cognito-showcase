# `os.sleep(N)` — make the turtle pause

**Lane:** Minecraft ComputerCraft Shorts (CC:Tweaked · Lua)

Scheduled: 2026-07-31 · Video showcase page will link here once the Short publishes.

---

## The Concept

Make the turtle pause.

`os.sleep(N)` freezes the program for `N` seconds, then carries on with the next line. Nothing complicated — the turtle just stops, waits, and moves on.

Useful when you want space between actions: give a redstone signal time to settle, let a block finish falling, or just space things out so you can watch what the turtle is doing without every step happening in one blur.

---

## The Code

See [`sleep.lua`](./sleep.lua) — the exact code from the episode.

```lua
-- file: sleep
for i = 1, 5 do
  turtle.forward()
end
os.sleep(2)
turtle.turnRight()

for i = 1, 3 do
  turtle.forward()
end
os.sleep(1)
turtle.turnRight()

for i = 1, 5 do
  turtle.forward()
end
os.sleep(2)
```

Turtle walks 5 blocks, waits 2 seconds, turns, walks 3, waits 1, turns, walks 5 more, waits 2. The pauses let the movement breathe.

---

## Pre-req

Install [CC:Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) from CurseForge or Modrinth (free). Drop a turtle, give it fuel (coal in slot 16, then `refuel`), and paste this in.
