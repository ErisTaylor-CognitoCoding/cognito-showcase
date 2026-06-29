# costumes — Animation by Switching Outfits

> 📺 **29 Jul 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 29 Jul 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A flipbook. Draw a ball slightly further along on each page. Flick through fast enough and it looks like the ball is moving. Costumes work the same way — each is a single frame; switch between them fast enough and you get animation.

---

## What it does

Every Scratch sprite can have multiple costumes — different images assigned to the same sprite. Switch between them with `next costume` or `switch costume to [name]`.

A walking character might have four costumes: right foot forward, feet together, left foot forward, feet together. Loop through them at 10 frames per second — the character looks like it's walking.

---

## Beyond animation

Costumes also handle **game states**. A Pac-Man ghost has a blue "frightened" costume and a coloured "normal" costume. Switch costume based on game state, not just animation frame. One block — completely different appearance.

In Space Invaders, the explosion when an alien dies is a costume switch to an explosion frame, followed by `hide`.

---

## Key blocks

`next costume` — advance one costume in the list, looping back to the first.

`switch costume to [name]` — jump directly to a named costume.

`costume number` — which costume is currently showing (useful for cycling and tracking state).

---

## Where it appears in the series

- [Space Invaders →](../../series/ep-04-space-invaders) — alien explosion animation
- [Donkey Kong →](../../series/ep-05-donkey-kong) — Mario walking and jumping frames
- [Pac-Man →](../../series/ep-06-pac-man) — ghost frightened state

---

*[← Back to concepts](../README.md) · Next: [glide-to →](../glide-to)*
