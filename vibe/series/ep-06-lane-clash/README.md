# Lane Clash: I Talked a 3v3 Roblox Tower Defence Into Existing

> 📺 **Watch on YouTube → *(link coming 30 Jun 2026)***

> 🤖 **Built with Roblox Studio Assistant** — 16 directed phases, no hand-written Luau. [Try Replit Agent →](https://replit.com/refer/cognitocoding)

---

## The Prompts I Gave

Not one prompt. Sixteen phases — each a focused brief for the next piece of the game.

**Phase 1 — the foundation:**
```
Create the foundation for a competitive tower defense game called Lane Clash.
Build a straight lane on a flat baseplate: a 4-stud-wide path made of LaneClashPath
parts running from a spawn point to a base. Add an Attachment-based waypoint folder
LaneClashWaypoints marking the path corners. Create one tower model LaneClashTowerBasic
that I place by clicking an empty grid tile beside the path. Placement only, no combat yet.
```

**Phase 13 — the hardest brief (shared team pool):**
```
Create LaneClashTeam with two teams per match, each holding its member players and ONE
shared LaneClashTeamBaseHealth pool. Roblox has no true mutex — use a single server-side
queue for LaneClashTeamBaseHealth writes. Describe your queue/debounce strategy BEFORE
writing the code, not after.
```

The full 16-phase prompt series is in Pantheon video doc #19.

---

## What the AI Built

Lane Clash is a competitive send-your-wave tower defence on Roblox — 1v1, 2v2 and 3v3 — where you don't just build towers; you spend cash to send enemy waves into your opponent's lane. Each team shares a single base health pool. The team that hits zero loses, or whoever has more health when the timer runs out wins.

This was an experiment, not a product launch. The core is proven — a playable game came out the other end. But Phase 7 (server-authoritative sends, no client trust) and Phase 13 (a shared team pool with no real Roblox mutex) are where "just talk to it" stopped being enough. The AI fought back. That struggle is the content — not the clean version where it works first time.

**Honest verdict:** Roblox Studio Assistant can build a working game core. The hard part is making it multiplayer-safe and server-authoritative. That difficulty is exactly what students need to see.

---

## Series

**Tue Vibe Coding** — one game or app per episode, built live by directing an AI. Every Tuesday on [Cognito Coding](https://www.youtube.com/@CognitoCoding01).

---

← [Back to Vibe series index](../README.md)
