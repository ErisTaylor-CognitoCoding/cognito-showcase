# Controlling the Turtle — Lua, `edit` and Pastebin in Minecraft

> 📺 **[Watch on YouTube →](https://youtu.be/x8JjMrbETG4)**

**Series:** Minecraft ComputerCraft (CC:Tweaked)  
**Lane:** `wed_minecraft` · Long-form

---

## What we built

Three turtles, sat in a row. Same block, same little face — and by the end of this they'll have done three completely different jobs. The only thing that changes is how the code got in.

---

## Three ways to get code into a turtle

### 1. The Lua prompt

Right-click a turtle → type `lua` → you're in. Live line. Whatever you type runs the second you hit enter. No file, no saving, just you and the turtle.

Brilliant for poking about and learning what a command actually does. Useless for anything you want to run twice.

```lua
turtle.forward()    -- move one block forward (returns true/false)
turtle.turnLeft()   -- rotate 90° left
turtle.up()         -- move one block up
```

Every turtle command answers `true` or `false`. If something's in the way, you get `false` and the turtle stays put. Later on, that answer is what all the clever stuff gets built from.

**One thing first:** drop a marker block beside the turtle before you test movement — on flat grass, a turtle that's moved one block looks identical to one that hasn't.

### 2. The built-in editor (`edit`)

Type `edit <filename>` at the CraftOS prompt to open the editor. Write your program, Ctrl to bring up the menu, save and exit — then run it by typing its name.

The square from this episode uses a loop inside a loop:

```lua
-- square.lua
local SIDE = 5

turtle.select(1)
turtle.up()

for side = 1, 4 do
  for i = 1, SIDE do
    turtle.placeDown()
    turtle.forward()
  end
  turtle.turnRight()
end
```

Why 5 a side comes out 6 blocks long: the corner block belongs to two sides at once, so a run of 5 lands you one past the corner — which is where the next side starts. Want 5 across? Put 4 in.

Change `SIDE` to 10 for a big one. That's the only number you'd ever touch.

→ Full file: [`square.lua`](./square.lua)

### 3. Pastebin (`pastebin get`)

For anything long — or anything someone else has written. Paste your code at [pastebin.com](https://pastebin.com), get back an 8-character code, pull it into the turtle:

```
pastebin get faNjkUUP computers
```

Once it lands, it's just a file. Read it with `edit`, change any line you want, run it by name. The only bit that matters from the Pastebin URL is the 8 characters at the end.

**Gotcha:** `pastebin get` needs the HTTP API switched on. In single player, you're fine. On some servers it's off — you'll get a refused message and spend twenty minutes convinced you mistyped the code. You didn't. It's the server. Use `wget <raw-pastebin-url>` as the fallback.

The 90-line desk builder from this episode — advanced computer, disk drive, printer, modem, stairs tucked underneath, floor filled in — is at [pastebin.com/faNjkUUP](https://pastebin.com/faNjkUUP).

→ Full file: [`computer.lua`](./computer.lua)

---

## Slot inventory (desk builder)

The slot numbers are written into the program. It doesn't go hunting — it looks in a specific slot, and if it's empty, it stops silently.

| Slot | Item |
|---|---|
| 1 | Stairs |
| 3 | Advanced computer |
| 5 | Floor blocks |
| 6 | Disk drive |
| 7 | Printer |
| 8 | Wired modem (sits on the machine) |
| 9 | Wireless modems (roof network line) |
| 16 | Coal (fuel) |

---

## Other commands covered

| Command | What it does |
|---|---|
| `label set <name>` | Names the turtle — survives breaking and picking up |
| `refuel` | Eats fuel from the top-left slot |
| `refuel 0` | Checks fuel level without burning anything |
| `turtle.placeDown()` | Places a block from the selected slot beneath the turtle |
| `ls` | Lists files on the turtle |
| `delete <file>` | Removes a file |
| Ctrl+T | Kills a runaway program |

---

## Code in this episode

- [`square.lua`](./square.lua) — the square-drawing program from the editor demo
- [`computer.lua`](./computer.lua) — the 90-line desk builder from the Pastebin demo

Original Pastebin: [pastebin.com/faNjkUUP](https://pastebin.com/faNjkUUP)

---

*[← Back to Minecraft series](../README.md)*
