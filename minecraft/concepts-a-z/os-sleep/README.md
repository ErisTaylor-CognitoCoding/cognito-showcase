# `os.sleep(N)` — make the turtle pause

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/ME77v-mlmfw?feature=share)**

---

Make the turtle pause.

`os.sleep(N)` stops the whole program for N seconds — no thinking, no moving, just waiting. Drop it between two commands and the gap becomes visible: the turtle walks, hangs there, then carries on. Take the sleeps out and the whole thing's over in a blink — you can't tell where one job ends and the next starts.

Every one of those gaps is a single line. The number in the brackets is seconds.

```lua
-- block to place goes in slot 1
-- coal in slot 16
turtle.select(1)

os.sleep(5)           -- wait 5 seconds before starting

for i = 1, 5 do
  turtle.forward()    -- walk five blocks
end
os.sleep(1)           -- pause so you can see the turtle stop

for i = 1, 5 do
  turtle.place()      -- build a tower upward
  turtle.up()
end
os.sleep(1)
```

See [`sleep.lua`](./sleep.lua) for the full working script.

---

**Lane:** Fri Minecraft Short — ComputerCraft (CC:Tweaked) Lua

*[← back to minecraft concepts](../README.md)*
