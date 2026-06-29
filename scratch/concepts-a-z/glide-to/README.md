# Glide To — Smooth Movement

> 📺 ***(Short coming Wed 5 Aug 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Motion (blue)

---

## What This Block Does

`glide (1) secs to x: (0) y: (0)` moves a sprite smoothly from where it is to a destination in a set time. Scratch handles the path automatically — you just say where and how long.

No maths, no loops, no intermediate positions. One block does it all.

---

## The Analogy

A taxi. You tell it "get me to the station in 10 minutes." The driver figures out the route. You just wait and arrive.

`glide to` is the taxi. You give the destination and the time. Scratch calculates the path.

---

## How It Works

```
when green flag clicked
glide (2) secs to x: (200) y: (0)
glide (2) secs to x: (-200) y: (0)
glide (2) secs to x: (0) y: (150)
```

Three glides in sequence. The sprite moves smoothly to each point, one after another. No `forever`, no `change x`, no manual calculation.

---

## When to Use It — and When Not To

`glide to` is great for menu animations, enemy patrol paths, or any movement that should feel smooth and controlled.

It is *not* right for player control — because the script is locked into the glide until it finishes. You can't interrupt it with a keypress. For responsive player movement, use `change x by` inside a `forever` loop instead (see [arrow-keys →](../arrow-keys)).

In the arcade series, `glide to` is used for non-player motion — the UFO crossing the top of Space Invaders, title screen animations.

---

## In the Arcade Series

**Appears in:** [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders) (UFO movement)

*[← costumes](../costumes) · [Back to concepts →](../README.md) · Next: [variables →](../variables)*
