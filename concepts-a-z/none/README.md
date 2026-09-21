# `none` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/Aok4aPejhTs)**

---

A weather app with a dead sensor shows a dash, not zero degrees — because zero is a real reading and a dash means no reading at all. Your code does the same.

`None` is how Python marks a value that isn't there yet. It is not zero and it is not an empty string — it means nothing has been filled in. Check for it before doing any maths, or you'll treat a missing sensor as a freezing one.

```python
reading = None
print(reading)        # None
print(reading == 0)   # False
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
