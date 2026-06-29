<!-- showcase-stub-v1 -->
# I Taught an AI to Farm — Ep 12: Combined Carrots, Grass, Trees & Power

**Lane:** The Farmer Was Replaced — long-form series
**Status:** Code committed (CODE-PAIR session 2026-06-29)

## What this episode covers

A unified farming loop that combines all four crop types into one script:

| Column / condition | Crop | Hat |
|--------------------|------|-----|
| Column 0 | Sunflower (power source) | 🚦 Traffic Cone |
| `x % 2 == y % 2` (diagonal) | Tree | 🌳 Tree Hat |
| Columns 1–3, non-diagonal | Grass | 🌾 Straw Hat |
| Column 4+, non-diagonal | Carrot | 🥕 Carrot Hat |

After each full column sweep the script finds the sunflower with the
best measurement and harvests only that one — keeping power topped up
without wasting the whole row.

## Key concepts

- Modulo arithmetic for spatial patterns (`goodForTree`)
- Multi-crop field layout using column index + position parity
- Targeted harvesting using `measure()` and a running `best` variable
- Water management loop to keep crops healthy

## Code

See [`main.py`](./main.py) in this folder.

## Watch on YouTube

🔗 Link added when the episode goes live on the
[Cognito Coding channel](https://www.youtube.com/@CognitoCoding01).

[← back to showcase root](../../README.md)
