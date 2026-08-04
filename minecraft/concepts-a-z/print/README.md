# `print()` — Ask Your Minecraft Turtle a Question

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/y0w1dPqi-I8)**

---

Ask the turtle a question — it answers.

`print()` puts whatever you give it on the screen. It's the first thing anyone does when learning to code — `print("hello")` and the computer talks back.

But you can ask it smarter questions. Chain a few prints and the turtle introduces itself:

```lua
print(os.getComputerID())       -- its ID number (e.g. 26)
print(os.getComputerLabel())    -- its name (e.g. "Bob")
print(turtle.getFuelLevel())    -- fuel remaining (0 = going nowhere)
```

And `turtle.inspect()` tells you what block it's currently looking at:

```lua
local ok, data = turtle.inspect()
if ok then
  print(data.name)              -- e.g. "minecraft:oak_log"
end
```

Take the prints out and the program runs silently — you can't tell where one job ends and the next starts. That's why `print()` is the first tool you reach for when debugging.

See [`print.lua`](./print.lua) for the starting file from the episode.

---

**Lane:** Fri Minecraft Short — ComputerCraft (CC:Tweaked) Lua

*[← back to minecraft concepts](../README.md)*
