# Upwork Actor Memory — neatrat/upwork-job-scraper

**Status:** WORKING ✅  
**Last verified:** 2026-04-26  
**Actor ID:** `neatrat/upwork-job-scraper`

---

## Confirmed Working Input Schema

```json
{
  "searchQuery": "AI automation",
  "maxItems": 25
}
```

**Key rules:**
- Use `searchQuery` (NOT `searchUrl`) — the old `searchUrl` guidance was wrong
- `maxItems` appears to be treated as a soft minimum page size — actor may return more than requested (observed 25 results with maxItems:3)
- Input is plain-text keyword, not a URL

---

## Critical: Timeout Requirement

**The actor STALLS / returns `status=RUNNING` at the default 60-second wait.**

This was the cause of today's (2026-04-26) actor failure during the daily scan. All 5 proposals ended up from Freelancer because Upwork was dead.

**Always set `wait_seconds: 150` minimum** when calling via `apify_run_actor`:

```python
apify_run_actor(
    actor_id="neatrat/upwork-job-scraper",
    input={"searchQuery": "AI automation", "maxItems": 25},
    wait_seconds=150   # <-- REQUIRED. 60 will stall.
)
```

Do NOT use default (90s) either — observed failures at 60s and uncertainty at 90s. 150s is confirmed safe.

---

## Output Schema

Each result item contains:

| Field | Notes |
|---|---|
| `id` | Upwork internal job ID |
| `subId` | Full `~0x...` formatted ID |
| `title` | Job title (use for proposal title, verbatim) |
| `description` | Full job description text (use for `job_description` in proposal, first 2000 chars) |
| `url` | Direct job URL (use for `job_url`) |
| `budget` | Client's listed budget (string, may be "N/A") |
| `jobType` | "Fixed" or "Hourly" |
| `experienceLevel` | "Entry Level", "Intermediate", "Expert" |
| `paymentVerified` | bool — skip unverified if budget is tiny |
| `clientLocation` | Country string |
| `clientAvgHourlyRate` | Float — low values (<£10) signal budget-constrained clients |
| `clientHireRatePercent` | Hire rate % — context on client quality |
| `clientTotalSpent` | Total $ spent on Upwork — low spend = unproven client |
| `proposals` | Proposal count — **skip if ≥ 20** |
| `tags` | Array of skill tags |
| `questions` | Array of screening questions — answer them in proposal body |
| `relativeDate` | "Posted N minutes/hours ago" |
| `absoluteDate` | ISO timestamp |

---

## Filter Rules (apply after fetching)

1. **Skip if `proposals >= 20`** — too competitive
2. **Skip if `paymentVerified = false` AND budget < £100** — high abandon risk
3. **Skip if `budget = "$0"` or `budget = "$6"` etc clearly sub-£50** — not worth the time
4. **Hard rejects**: mobile-native, blockchain/crypto, WordPress theme, equity-only, ToS-violation asks (auto-apply on platforms, bot-posting through platform UIs)
5. **Apply reframe lens before rejecting on budget** — many under-budget listings convert to Apollo/SBA/Athena monthly products

---

## Search Queries — Rotate Daily (pick 4–5 per run)

- "AI automation"
- "AI chatbot"
- "AI executive assistant"
- "small business app"
- "workflow automation"
- "Flask Python"
- "React dashboard"
- "AI consultancy"
- "EdTech"
- "tutoring platform"
- "SaaS development"
- "business process automation"

---

## Failure History

| Date | Failure | Root Cause | Fix |
|---|---|---|---|
| 2026-04-26 | status=RUNNING, all results blank | wait_seconds=60 too short | Use wait_seconds=150 |

---

## Notes

- The actor returns results in reverse-chronological order (most recent first)
- `clientAvgHourlyRate` is the avg they've paid OTHER freelancers — useful signal for budget calibration
- `questions` field is important — if present, answer each question explicitly inside the proposal body or risk auto-rejection
- No authentication needed — scrapes public Upwork search results only (ToS-compliant)
