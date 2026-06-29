# full-farm — Everything Together

> 📺 **19 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** combining loops, conditionals, variables, and entity checks

---

## The Farmer Analogy

A real automated farm doesn't run one crop. It runs all of them — hay, carrots, pumpkins, sunflowers — in a coordinated sequence. Every concept from the series runs together in one set of passes.

This is the culmination.

---

## What It Pulls Together

| Concept | Where it appears |
|---------|-----------------|
| `while True` | outer loop — farm runs forever |
| Nested `for` loops | snake pattern — every tile visited |
| `get_entity_type()` | know which crop is on each tile |
| `get_growth()` | check pumpkin state (ripe/dead) |
| `measure()` | find the champion sunflower |
| `max_petals` variable | remember the best across the sweep |
| `if/elif` | branch on what action each tile needs |
| `harvest()`, `plant()` | act on what's found |

---

## The Architecture

```
while True:
    Pass 1: scan sunflowers → find max_petals
    Pass 2: act on every tile
            ├── Sunflower at max_petals → harvest (collect the Sun)
            ├── Dead pumpkin           → harvest (clear the tile)
            ├── Ripe pumpkin           → harvest (collect the merge)
            └── Anything else ready   → harvest
```

Two passes per cycle. The first is read-only (just finding the champion). The second acts on everything.

---

## See It in the Full Episodes

This draws on all five series episodes:
- [Ep 1](../../series/ep-01-first-program) — `harvest()`, `while True`, `if can_harvest()`
- [Ep 2](../../series/ep-02-operators) — operators, navigation, multi-crop
- [Ep 3](../../series/ep-03-functions) — functions, DRY
- [Ep 4](../../series/ep-04-pumpkins) — variables, tile state
- [Ep 5](../../series/ep-05-sunflowers) — `measure()`, running max

---

*[← upgrade](../upgrade) · [Back to concepts](../README.md)*
