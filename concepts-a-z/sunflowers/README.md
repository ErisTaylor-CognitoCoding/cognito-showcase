# sunflowers — Track the Best

> 📺 **8 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `measure()`, running maximum, variables

---

## The Farmer Analogy

You're standing at the edge of a field of 144 sunflowers. Only one is worth cutting — the one with the most petals. You can't tell from the edge which one it is. You have to walk the whole field, holding a mental note of the biggest one you've seen so far. Every time you find something bigger, update the note.

That's a running maximum.

---

## The Running-Max Pattern

```python
max_petals = 0   # start with the worst possible value

for x in range(get_world_size()):
    for y in range(get_world_size()):
        if get_entity_type() == Entities.Sunflower:
            if measure() > max_petals:
                max_petals = measure()   # new champion — update the best
        move(North)
    move(East)
```

By the end, `max_petals` holds the highest petal count anywhere in the field. Not a guess — a fact.

---

## What `measure()` Returns

A number you can compare — the sunflower's petal count. Higher petals = higher value. The game only drops a Sun when you harvest the sunflower with the *most* petals. Cut any other and it's wasted.

---

## The Three Lines That Matter

```python
max_petals = 0           # 1. start at zero (worst case)
if measure() > max_petals:   # 2. found something better?
    max_petals = measure()   # 3. update the champion
```

This three-line pattern works for finding the tallest, longest, heaviest, cheapest, fastest — anything you're comparing across a collection.

---

## See It in the Full Episode

[Episode 5](../../series/ep-05-sunflowers) — full sunflower mechanic including the double sweep to find and then harvest the champion.

---

*[← pumpkins](../pumpkins) · [Back to concepts](../README.md) · Next: [dead-crops →](../dead-crops)*
