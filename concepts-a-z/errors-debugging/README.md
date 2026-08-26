# `errors-debugging` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/L56qAxir5Wo)**

---

A satnav that can't find your address doesn't drive off and hope — it stops, and it names exactly what it couldn't find.

Your code does the same. When something goes wrong it halts, then tells you which file, which name, which line. An error message is not a telling-off — it is the fastest clue you will ever get. Read it, fix it; don't change things at random and hope.

```python
scores = open("scores.txt")
print(scores.read())

# FileNotFoundError: [Errno 2] No such file or directory: 'scores.txt'
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
