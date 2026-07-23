# `nested-loops` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/uOElKYS1y8U)**

---

## The School Register Trick

Picture a teacher taking the register. Two classes. She doesn't just read out the class names — she opens Year 3, reads every name in it, then opens Year 4 and reads every name in that one too. One list sitting inside another list.

That's a nested loop: a loop inside a loop. The outer one walks through the groups. The inner one walks through every item inside whichever group you're in. Three lines of Python, and the computer reads out every name in every class — no copying, no pasting.

---

## The Code

```python
for classroom in ["Year 3", "Year 4"]:
    for name in ["Ada", "Alan"]:
        print(classroom, name)
```

The outer `for` moves through each classroom. The inner `for` reads every name in that classroom before the outer loop moves on.

---

*[← back to concepts](../README.md)*
