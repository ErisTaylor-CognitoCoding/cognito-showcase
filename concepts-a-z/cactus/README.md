# cactus — Wait for Full Growth

> 📺 **29 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `get_growth()`, patience in code, grow-then-harvest

---

## The Farmer Analogy

Cacti grow slowly. Harvest one too early and you get nothing — the cut is wasted. A good farmer checks the cactus before cutting. Only when it's fully grown does it pay out.

The drone does the same: `get_growth() == 1` means fully grown. Anything else means leave it.

---

## Why `can_harvest()` Isn't Enough Here

`can_harvest()` tells you whether it's *possible* to harvest the tile. For a cactus that's growing, it might still return `True` — but harvesting early yields nothing.

The growth check is the extra layer: *is this one ready to pay out?*

```python
if get_entity_type() == Entities.Cactus:
    if get_growth() == 1:   # fully grown — worthwhile
        harvest()
    # else: leave it, come back next pass
```

---

## The Full Pattern

```python
while True:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            if get_entity_type() == Entities.Cactus:
                if get_growth() == 1:
                    harvest()
            move(North)
        move(East)
```

The drone sweeps the entire field on every pass. Unripe cacti are skipped every time until they're ready. No wasted cuts.

---

## The Lesson

Patience isn't a feeling in code — it's a condition. "Wait until `get_growth() == 1`" is how you express it. The drone doesn't get impatient; it just checks and skips until the condition is met.

---

*[← trees](../trees) · [Back to concepts](../README.md) · Next: [trade →](../trade)*
