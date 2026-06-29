# trade — Convert Harvest to Gold

> 📺 **5 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** arithmetic, `num_items()`, calculating totals

---

## The Farmer Analogy

After a harvest, you take your hay to the market. 10 gold per bale. If you've got 25 hay, that's 250 gold. Simple multiplication — but the drone has to calculate it, not guess.

---

## What `num_items()` Returns

The current count of a specific item in the drone's inventory.

```python
hay = num_items(Items.Hay)     # how many hay bales do I have?
```

---

## The Arithmetic

```python
hay = num_items(Items.Hay)
gold_per_hay = 10

gold_earned = hay * gold_per_hay
```

Three lines. A count, a rate, a total.

---

## Why This Matters Beyond Trade

Once you can calculate totals, you can make decisions:
- *Do I have enough to buy the upgrade?* → check `num_items(Items.Hay) >= cost`
- *How many more harvests until I hit my target?* → `target - num_items(Items.Hay)`
- *Is this run profitable?* → compare before vs after

Arithmetic is the bridge between harvest counts and game progress. The same pattern appears in every system that tracks quantity and cost.

---

## See What Comes Next

[upgrade →](../upgrade) — uses `num_items()` to check a balance before spending.

---

*[← cactus](../cactus) · [Back to concepts](../README.md) · Next: [upgrade →](../upgrade)*
