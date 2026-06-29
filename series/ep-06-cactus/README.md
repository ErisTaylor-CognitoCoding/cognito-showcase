# Episode 6 — Cactus

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)  
**Watch:** *(link coming)*

---

## What This Episode Covers

By episode 6, the farm is a multi-crop operation. This episode adds **cactus farming** and builds the orchestration layer that ties everything together.

### Concepts

| Concept | What it teaches |
|---------|----------------|
| `num_items()` | Check your inventory mid-loop to make decisions |
| Conditional crop swap | Switch which routine runs based on what you need |
| Orchestration | One controller calling multiple specialised functions |

### How the controller works

```
Always → main()           (grass, trees, carrots every loop)
If Power > 5000 → pumpkins()   (top up the power buffer)
If Cactus < 1000 → cactus()    (restock cactus supply)
```

Each crop lives in its own module. The controller just decides **when** to run each one.

---

## Files

| File | What it is |
|------|-----------|
| `controller.py` | The main orchestration loop — calls all crop modules |
| `cactus.py` | *(coming)* The cactus harvesting routine |
| `main.py` | *(coming)* Grass, trees and carrots combined |
| `pumpkins.py` | *(coming)* Pumpkin harvesting for Power |

---

## Previous Episodes

← [Episode 5 — Sunflowers](../ep-05-sunflowers) · [All Episodes](../README.md)
