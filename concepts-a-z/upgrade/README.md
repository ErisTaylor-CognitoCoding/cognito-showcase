# upgrade — Only Buy If You Can Afford It

> 📺 **12 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `num_items()`, threshold checks, `break`

---

## The Farmer Analogy

You want a faster drone. It costs 100 hay. You check your stores — if you have enough, you spend it and stop farming. If not, you keep harvesting until you do. You never spend what you don't have.

---

## The Pattern

```python
UPGRADE_COST = 100

while True:
    if can_harvest():
        harvest()

    if num_items(Items.Hay) >= UPGRADE_COST:
        use_item(Items.Hay, UPGRADE_COST)
        break   # upgrade purchased — exit the loop
```

---

## What `break` Does

Exits the loop immediately. Here it's used once the upgrade is purchased — no point continuing to harvest once the goal is reached.

Without `break`, the drone would keep farming forever even after buying the upgrade.

---

## The `>=` Operator

Greater-than-or-equal. Matches when the balance is *at least* the cost — not just exactly equal. Safer than `==` here because the inventory could jump past 100 between checks.

---

## What You're Really Learning

This is a **goal-oriented loop**:
1. Keep doing something (harvest)
2. Check if you've hit the target (inventory >= cost)
3. When you have — act and stop

The same pattern handles any "farm until you can afford X" scenario. It's also the foundation for resource-management AI in games.

---

## See What Comes Next

[full-farm →](../full-farm) — all concepts combined into one automated farm that never stops.

---

*[← trade](../trade) · [Back to concepts](../README.md) · Next: [full-farm →](../full-farm)*
