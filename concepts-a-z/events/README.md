# `events` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/05kT65nEGtk)**

---

Nobody sits in the kitchen all night sniffing for smoke. So why should your program? An event is a signal — a button pressed, a key tapped, a file arriving — that your program waits for quietly and reacts to the moment it happens. Instead of checking over and over in a loop, you hand a function to a trigger once. The function runs only when it's needed.

```python
import tkinter as tk
def alarm(): print("Beep! Beep!")
tk.Button(text="Smoke", command=alarm).pack()
tk.mainloop()
```

Full file: [`example.py`](example.py)

---

*Part of the **Coding Concepts** series — one concept per Short.*  
*[← Back to concepts](../README.md)*
