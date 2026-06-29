# glide-to — Smooth Movement on Autopilot

> 📺 **5 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 5 Aug 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A travelator at an airport. You step on, it carries you to the destination smoothly, then stops. You don't calculate each step — you just tell it where you're going and how long it should take.

`glide [N] secs to x: [X] y: [Y]` is exactly that. Tell Scratch where to go and how long it has. Scratch handles everything in between.

---

## What it does

`glide` moves a sprite from its current position to a target in a straight line over a set number of seconds. The movement is smooth — no jitter, no per-frame calculation required.

Critically, `glide` **pauses the script** until it's done. The next block doesn't run until the sprite arrives. This makes it perfect for scripted movement sequences: go here, wait until arrived, go there.

---

## Where `glide` wins

In Frogger, every car drives across a lane. Without `glide`, you'd manually change x by a small amount every frame in a loop, then reset when it goes off screen. With `glide`: pick a start position, glide to the other side, repeat. Three blocks, done.

---

## When NOT to use `glide`

Player-controlled movement. Because `glide` pauses the script, no input can interrupt it mid-glide. Player characters need per-frame position updates, not glides — otherwise holding a key feels sticky and unresponsive.

---

## Where it appears in the series

- [Frogger →](../../series/ep-03-frogger) — every car and log lane uses glide
- [Pac-Man →](../../series/ep-06-pac-man) — ghost movement between grid tiles

---

*[← Back to concepts](../README.md) · Next: [variables →](../variables)*
