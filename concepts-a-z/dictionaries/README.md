# `dictionaries` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/lkEoNwNhI0Y)**

---

## The Phone Book Trick

Would you read a whole phone book, front to back, just to find one number? Of course not. You flip straight to the name, and the number is sat right next to it.

That's exactly what a dictionary does in your code. You hand it a name — a key — and it hands you back whatever is stored under that name. No searching through a list. No counting by position. Look up the label, get the value.

```python
phone_book = {"Zero": "07123", "Nova": "07456"}
print(phone_book["Nova"])
```

Curly brackets hold the pairs — the name (key) on the left, the value on the right. Square brackets fetch one back out. Hand it `"Nova"` and it returns `"07456"` instantly.

See [`example.py`](./example.py) for the runnable file.

---

*[← back to concepts](../README.md)*
