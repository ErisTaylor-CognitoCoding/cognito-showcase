# `slicing-lists` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/x6CRaS4n_vM)**

---

Pick out four holiday photos to show a friend — you flip to the third one and stop at the sunset. The album never changes — nothing gets taken out. That's slicing a list: you ask for a stretch, and you get a copy back.

Counting starts at zero, so `2` means the third item. The second number is where the slice stops — that position is never included. `photos[2:4]` gives you items at positions 2 and 3, and the original list is untouched.

```python
photos = ["beach", "castle", "market", "sunset", "harbour"]
print(photos[2:4])
# ['market', 'sunset']
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
