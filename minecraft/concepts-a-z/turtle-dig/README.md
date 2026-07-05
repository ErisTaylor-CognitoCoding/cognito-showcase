# `turtle.dig()` + `for` loop — dig a tunnel

> 📺 **Coming 17 Jul 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Lane:** Minecraft ComputerCraft Shorts (CC:Tweaked · Lua)

---

## The Concept

One word to dig. One line to do it three times.

`turtle.dig()` breaks the block directly in front of the turtle and pockets it. Wrap that in a `for` loop and it repeats as many times as you say — type `3`, get a 3-block tunnel; type `100`, get a 100-block tunnel. Same code, different number.

That's the whole point of a loop: write it once, run it as many times as you need.

---

## The Code

See [`dig_and_place.lua`](./dig_and_place.lua) — the exact code from the episode.

```lua
turtle.select(1)
for i = 1, 3 do
  turtle.digDown()
  turtle.placeDown()
  turtle.forward()
end
```

---

## Pre-req

Install [CC:Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) from CurseForge or Modrinth (free).

---

*[← back to Minecraft concepts](../README.md)*
