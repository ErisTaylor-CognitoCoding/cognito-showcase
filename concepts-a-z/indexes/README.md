# `indexes` — Why Coders Call the Front Seat Zero

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/a66jdoxvNQg)**

---

Get on a bus and the front seat isn't seat one — it's seat zero.

Python counts from zero because a list's index tells you how many steps to walk from the start before you grab something. Zero steps: you haven't moved — you're still at the first item. One step: you've moved once, you're at the second. That gap between "position one" and "index zero" is where off-by-one bugs are born.

---

## The snippet

```python
seats = ["Ada", "Grace", "Alan"]
print(seats[0])   # Ada    — zero steps, first item
print(seats[1])   # Grace  — one step, second item
```

`seats[0]` — zero steps from the front, grab the first item.  
`seats[1]` — one step in, grab the second.  
`seats[2]` — two steps, the third (and last).  
`seats[3]` — nobody there. Python raises `IndexError`.

Full example: [`example.py`](example.py)

---

## Key rule

> The index is how many steps from the front — not which seat number it is.

A list of 3 items has valid indexes `0`, `1`, `2`. The highest valid index is always `len(list) - 1`.

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
