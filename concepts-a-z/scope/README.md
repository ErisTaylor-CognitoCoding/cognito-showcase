# `scope` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/lCW5lShG6To)**

---

What's in your lunchbox is yours — nobody else can reach in and take the biscuit. What's on the shared table, anyone can help themselves to.

Code works the same way. A name you make **inside** a function stays locked in that function's lunchbox. A name you make **outside** sits on the shared table where everything can reach it. Try to grab an inside name from outside and Python says: `NameError: name 'treat' is not defined`. You're reaching into somebody else's box.

That's **scope**.

```python
def lunchbox():
    treat = "biscuit"

lunchbox()
print(treat)   # NameError: name 'treat' is not defined
```

Full example: [`example.py`](example.py)

---

## Quick rules

- A name created **inside** a function is **local** — only that function can see it
- A name created **outside** any function is **global** — any function can read it
- Trying to read a local name from outside raises `NameError: name '...' is not defined`

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
