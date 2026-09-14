# `text-to-numbers` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/4HuQz7GJo2Y)**

---

When you type something in, Python hands it back as text rather than a number. That's why typing `2` and then `3` and adding them gives you `23` instead of `5` — you're joining two labels together, not doing maths.

A price label is just ink on paper. It says £3, but it can't add itself to anything until the till reads it. `int()` is the till — pass the text through it and it becomes a whole number you can add, subtract and compare. If the text isn't a number at all, Python raises a `ValueError`, which is its way of saying it couldn't read the label.

```python
price = "3"
total = int(price) + 2
print(total)  # 5, not 32
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
