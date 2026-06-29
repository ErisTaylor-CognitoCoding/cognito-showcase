# Broadcast and Receive — Sprites Talking to Each Other

> 📺 ***(Short coming Wed 19 Aug 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Events (yellow)

---

## What This Teaches

How sprites in Scratch communicate with each other.

`broadcast [message]` shouts a message to every sprite in the project. Any sprite with `when I receive [message]` hears it and runs whatever's stacked below.

---

## The Analogy

A school tannoy. The headteacher says "fire drill." Every classroom hears it and responds — some classes line up at the door, some put books away, some head straight to the fire exit. One message, many reactions. Nobody had to ring each classroom individually.

---

## How It Works

```
# Ball script — when someone reaches 11:
broadcast [GAME OVER]

# Game Over sprite:
when I receive [GAME OVER]
go to x: (0) y: (0)
show
start sound [game over]
```

The ball doesn't know the Game Over sprite exists. It just broadcasts. The Game Over sprite is listening and reacts.

---

## Broadcast vs Broadcast and Wait

- `broadcast [message]` — sends the message and carries on immediately (fire and forget).
- `broadcast [message] and wait` — sends the message and pauses until every receiver has finished running.

In Space Invaders, `broadcast [formation step] and wait` holds the formation controller until all 55 alien clones have moved. Without the `and wait`, the controller would immediately fire the next step while clones are still mid-move — the formation would glitch.

---

## In the Arcade Series

Broadcast is the coordination layer across every game:
- **Pong** — `broadcast [GAME OVER]` when score hits 11
- **Snake** — `broadcast [draw body]` every step to redraw all segments
- **Space Invaders** — `broadcast [formation step] and wait` to move all 55 clones in unison

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 2 — Snake →](../../series/ep-02-snake) · [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders)

*[← variables](../variables) · [Back to concepts →](../README.md) · Next: [random-numbers →](../random-numbers)*
