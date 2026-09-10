# `range` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/3Z4i5E1QWHg)**

---

Nobody printing pages 1 to 20 types out every number in between — you fill in the first page, fill in the last, and the printer works out the rest.

Code does the same. Give `range()` a start and a stop, and it counts every step between them for you. The second number is where the counting stops rather than the last one printed — so `range(1, 21)` gives you 1 all the way to 20.

```python
for page in range(1, 21):
    print("Printing page", page)
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
