# `modulo` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/Lq0eUeRJViI)**

---

Four kids, one bag of sweets — what's left in your hand?

You hand sweets out one each, round and round, until nobody can have another. Whatever's still in your hand is the leftover. Coders call that the **remainder** — and in Python the `%` operator (the percent sign) works it out for you.

```python
sweets = 22
kids = 4
print(sweets % kids)  # 2
```

`22 % 4` asks: share 22 into groups of 4, how many are left over? The answer is 2. The percent sign doesn't divide — it shares and hands you back the spare.

Full example: [`example.py`](example.py)

---

## Where to reach for it

- **Odd or even**: `n % 2 == 0` is even, `n % 2 != 0` is odd
- **Wrap a counter**: `counter % max_value` resets to zero instead of running off the end
- **Equal rows**: `index % columns` tells you which column any item lands in

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
