# Compile & Defend — Demo Tutorial

> 📺 **[Watch on YouTube →](https://youtu.be/zaU8RfnUAtg)**

**Game:** [Compile & Defend on Steam](https://store.steampowered.com/app/4915240/) · Free demo now · Full game 23 July 2026  
**Language:** Python  
**Lane:** Specials

---

## What this is

Tower defence where you never click a tower to shoot. Every tower on the field runs your Python, over and over, and the script is the whole game. Seven waves in the demo tutorial, and each one breaks the code that beat the last. By wave seven it's flyers and armour together — and the thing that finally got me three stars wasn't code at all.

---

## The seven waves

| Wave | Problem | Key concept |
|---|---|---|
| 1 | Shoot everything in range | `for` loop |
| 2 | Pick one from a list | indexing + guard against empty list |
| 3 | Closest to the exit wins | tracking a minimum |
| 4 | Flyers — only the tesla can hit them | type-matching filter |
| 5 | Armour — only the sniper gets through | filter + `found` flag |
| 6 | Swarm — remove the filter | knowing when NOT to filter |
| 7 | Flyers and armour together | priority ladder |

---

## The code

All seven waves are in [`allwaves.py`](./allwaves.py).

Each wave builds on the last. Start from wave 1 and read forward — every added line solves a problem the previous wave couldn't handle.

---

## Concepts covered

### `for` loop over a list
Run a block of code once for each item in `me.enemies_in_range`. The weapon of choice when you don't know how many enemies there'll be.

```python
for e in me.enemies_in_range:
    me.shoot(e)
```

### Guard against an empty list
Reach into an empty list and the whole script falls over. One `if len(...)` before any indexing prevents it.

```python
if len(me.enemies_in_range) > 0:
    target = me.enemies_in_range[0]
    me.shoot(target)
```

### Tracking a minimum
Start with the first item as your best candidate, then walk the whole list replacing it when something better appears. Classic pattern — comes back in waves 4, 5, and 7.

```python
target = me.enemies_in_range[0]
for e in me.enemies_in_range:
    if e.distance_to_exit < target.distance_to_exit:
        target = e
me.shoot(target)
```

### Type-matching filter + `found` flag
A filter only yields some enemies. You can't index into the result, so a flag tracks whether you've found a match yet.

```python
found = False
for e in me.enemies_in_range:
    if e.is_armored == me.is_sniper:
        if not found:
            target = e
            found = True
        elif e.distance_to_exit < target.distance_to_exit:
            target = e
if found:
    me.shoot(target)
```

### Priority ladder
When multiple criteria matter, stack the comparisons. Flying beats ground. Armoured beats unarmoured. Closest to exit breaks ties.

```python
target = 0
for e in me.enemies_in_range:
    if e.is_flying == False or me.can_hit_air == True:
        if target == 0:
            target = e
        elif e.is_flying != target.is_flying:
            if e.is_flying:
                target = e
        elif e.is_armored != target.is_armored:
            if e.is_armored:
                target = e
        elif e.distance_to_exit < target.distance_to_exit:
            target = e
if target != 0:
    me.shoot(target)
```

---

## Why the third star wasn't code

The wave 7 script was already correct. The winning move was selling one arrow tower and buying a tesla further up the path. The code runs where the tower is placed. Sometimes the best debug is moving the hardware.

---

## The game

Compile & Defend is made by Codx.io. Your code runs on every tower, once per tick — choose Python, JavaScript, C++, C#, Rust, Zig or Lua.

[Free demo + full game → Steam](https://store.steampowered.com/app/4915240/)

---

[← back to showcase root](../../README.md)
