# Episode 3 — Functions

> 📺 **[Watch on YouTube →](https://youtu.be/FMUXw4UKyLI?si=vdR-_AmSTZTkQyH_)**

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

In Episode 2 we got the 3×3 harvest working — but the code was a mess. The same harvest block copy-pasted everywhere. Episode 3 spots the pattern and wraps it in our first function. `harvest_field(size)` replaced ten repeated lines with one clean call.

The payoff: *"I replaced ten lines with one."*

---

## Coding Concepts Covered

### `def` — defining a function
Group a block of reusable code under a name. Call it wherever you need it instead of repeating the block.

```python
def harvest_field(size):
    for x in range(size):
        for y in range(size):
            if can_harvest():
                harvest()
            move(North)
        move(East)
```

### Parameters
Pass data into a function so it works at different scales. `harvest_field(3)` runs a 3×3. `harvest_field(6)` runs a 6×6. Same function — different size.

### DRY — Don't Repeat Yourself
The rule behind every refactor. If you paste the same block twice, it's time for a function.

```python
# Before: harvest block copy-pasted three times
# After: one clean call
while True:
    harvest_field(get_world_size())
```

---

## Cliffhanger

The function is clean — but it does the exact same thing every run. No memory. To grow the farm or track what's been planted, the drone needs to remember a value *between passes*. That's **variables**. Next episode: pumpkins.

---

## End-State Code

See [`farm.py`](./farm.py)

---

*[← Ep 2](../ep-02-operators) · [Back to guide](../README.md) · [Next: Ep 4 →](../ep-04-pumpkins)*
