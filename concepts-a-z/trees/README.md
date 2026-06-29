# trees — Harvest Multiple Resources

> 📺 **22 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `if/elif`, multiple entity types, routing by crop

---

## The Farmer Analogy

A mixed field has different crops on different tiles. You don't treat a tree the same way you treat a bush — but you don't want to write two separate loops either. One pass, branch on what you find.

---

## What `if/elif` Does

A chain of conditions. Python checks each one in order and runs the *first* block that matches.

```python
entity = get_entity_type()

if entity == Entities.Tree:
    if can_harvest():
        harvest()   # gets Wood

elif entity == Entities.Bush:
    if can_harvest():
        harvest()   # gets Fruit
```

One loop. Two crop types handled correctly.

---

## Why Not Two Separate Loops?

Two loops = two full passes over the entire grid. One loop with `if/elif` = one pass, every tile handled once. Faster and simpler once you have more than two crop types.

---

## The Pattern Scales

```python
for x in range(get_world_size()):
    for y in range(get_world_size()):
        entity = get_entity_type()

        if entity == Entities.Tree:
            if can_harvest():
                harvest()
        elif entity == Entities.Bush:
            if can_harvest():
                harvest()
        # add more elif branches as you unlock more crops

        move(North)
    move(East)
```

Every new crop type is just another `elif` branch.

---

## See It in the Full Episode

[Episode 2](../../series/ep-02-operators) — three crops (bushes, hay, carrots) handled in one pass, each routed differently.

---

*[← dead-crops](../dead-crops) · [Back to concepts](../README.md) · Next: [cactus →](../cactus)*
