# `while-loops` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/K51aYn5CgGI)**

---

## The Kettle Trick

You never decide up front how many times you'll check the kettle. You just keep checking while it's still cold — and the second it boils, you stop.

That's a `while` loop. The word `while` at the top isn't a number — it's a question the program keeps asking: *keep going while this is still true.* The moment it isn't true, the program walks off and gets on with its day.

A `while` loop doesn't count. It waits for something to change.

---

## The Code

```python
temperature = 20
while temperature < 100:
    temperature = temperature + 10
print("Boiled!")
```

`temperature` starts at 20. Before every pass the loop asks "is this still under 100?" — if yes, add 10 and go again. Once `temperature` hits 100 the condition is false, the loop stops, and "Boiled!" prints. No guessing how many times up front — the loop finds out as it goes.

See [`example.py`](./example.py) for the runnable file.

---

## `while` vs `for` — the key difference

| | runs | stops |
|---|---|---|
| `for i in range(n)` | exactly `n` times | automatically after `n` steps |
| `while condition` | unknown number of times | when `condition` turns false |

Use `while` when you don't know in advance how many repeats you'll need — waiting for user input, a game state changing, a sensor reading a threshold.

---

*[← back to concepts](../README.md)*
