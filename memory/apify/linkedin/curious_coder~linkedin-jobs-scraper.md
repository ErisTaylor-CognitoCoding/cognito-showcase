# LinkedIn Actor Memory — curious_coder/linkedin-jobs-scraper

**Status:** WORKING ✅  
**Last verified:** 2026-04-27  
**Actor ID:** `curious_coder/linkedin-jobs-scraper`

---

## Root Cause of Previous Timeout (2026-04-27)

The actor timed out on the first Scout run because `wait_seconds` was left at the default (90s). The actor needs **150s minimum**, exactly like Upwork. No memory file existed before this run, so the config was never persisted.

---

## Confirmed Working Input Schema

```json
{
  "urls": [
    "https://www.linkedin.com/jobs/search/?keywords=AI+automation&location=United+Kingdom&f_TPR=r86400&f_WT=2"
  ],
  "maxItems": 25
}
```

**Key rules:**
- `urls` must be a full LinkedIn search URL (NOT raw keywords)
- Always include `f_TPR=r86400` — filters to jobs posted in the last 24 hours
- `f_WT=2` = remote jobs only (recommended for our use case; omit for all location types)
- Multiple URLs supported — pass one per search query in the array
- Input must be an array, even for a single URL

---

## Critical: Timeout Requirement

**The actor stalls / returns `status=RUNNING` at the default 90-second wait.**

This caused today's (2026-04-27) timeout — 0 results returned.

**Always set `wait_seconds: 150` minimum** when calling via `apify_run_actor`:

```python
apify_run_actor(
    actor_id="curious_coder/linkedin-jobs-scraper",
    input={
        "urls": ["https://www.linkedin.com/jobs/search/?keywords=AI+automation&location=United+Kingdom&f_TPR=r86400&f_WT=2"],
        "maxItems": 25
    },
    wait_seconds=150   # <-- REQUIRED. 90 will stall.
)
```

---

## Output Schema

Each result item contains:

| Field | Notes |
|---|---|
| `id` | LinkedIn internal job ID |
| `link` | Direct job URL — **use this as `job_url` in pantheon_create_proposal** (NOT `applyUrl`) |
| `title` | Job title (use verbatim) |
| `companyName` | Hiring company name |
| `companyLinkedinUrl` | Company LinkedIn URL |
| `location` | Location string |
| `postedAt` | ISO8601 timestamp |
| `descriptionText` | Plain-text description — **use this** (NOT `descriptionHtml`) for `job_description`, truncate to 2000 chars |
| `descriptionHtml` | HTML version — do NOT use in proposals |
| `applicantsCount` | **String** (e.g. `"25"`, `"77"`) — parse to int before comparing. **Skip if >= 20** |
| `seniorityLevel` | e.g. "Mid-Senior level", "Not Applicable" |
| `employmentType` | e.g. "Full-time", "Part-time", "Contract" |
| `salary` | Often empty — unreliable |
| `salaryInsights` | Object, may contain `compensationBreakdown` with min/max salary |
| `workplaceTypes` | Array — e.g. `["Remote"]` |
| `applyUrl` | External apply URL — **do NOT use as `job_url`** |
| `inputUrl` | The search URL that produced this result |

---

## Filter Rules (apply after fetching)

1. **Skip if `int(applicantsCount) >= 20`** — too competitive (applicantsCount is a string, parse it)
2. **Apply Reframe Lens aggressively** — most LinkedIn results are full-time permanent hires. A "Senior AI Engineer £60k" is a Pantheon sale in disguise.
3. **Hard rejects**: mobile-native, blockchain/crypto, WordPress theme, equity-only, ToS-violation asks
4. **Content-writing-only roles** (e.g. "Content Writer") — no dev work, reject
5. **PhD-required R&D roles** (e.g. "Director of Research Development") — not our strand, reject
6. **Roles where `applicantsCount` is exactly `"25"` on LinkedIn** — LinkedIn caps display at 25; the real count may be higher. Treat `"25"` as "25+" and skip.

---

## Search URL Construction

Base: `https://www.linkedin.com/jobs/search/`

Key parameters:
- `keywords=AI+automation` — URL-encode spaces as `+`
- `location=United+Kingdom` — or `London` for city-level
- `f_TPR=r86400` — last 24 hours (86400 seconds)
- `f_WT=2` — remote only; omit for hybrid+onsite too
- `f_JT=C` — contract only (optional, useful for freelance queries)

Example URLs for each search query:
```
https://www.linkedin.com/jobs/search/?keywords=AI+automation&location=United+Kingdom&f_TPR=r86400&f_WT=2
https://www.linkedin.com/jobs/search/?keywords=AI+chatbot&location=United+Kingdom&f_TPR=r86400&f_WT=2
https://www.linkedin.com/jobs/search/?keywords=workflow+automation&location=United+Kingdom&f_TPR=r86400&f_WT=2
https://www.linkedin.com/jobs/search/?keywords=SaaS+development&location=United+Kingdom&f_TPR=r86400&f_WT=2
https://www.linkedin.com/jobs/search/?keywords=AI+consultant&location=United+Kingdom&f_TPR=r86400&f_WT=2
```

---

## LinkedIn-Specific Reframe Strategy

LinkedIn is dominated by full-time hires. The Reframe Lens is the primary tool here.

| Listing type | Reframe | Target strand |
|---|---|---|
| "Hire Senior AI Engineer £60k" | Fixed-scope Pantheon build = same outcome, lower risk | Pantheon £2,500+ |
| "Head of AI / AI Director wanted" | Athena fractional — £750/mo for 3 configured agents + debrief | Athena |
| "Operations Manager with automation experience" | Athena audit → workflow automation agents | Athena |
| "Python/Flask developer needed" | Project-scoped build, fixed fee | Pantheon or SBA |
| "Data analyst / BI dashboard" | React dashboard build, fixed fee | Pantheon |
| "Executive assistant / VA" | Apollo — £29.99/mo, no setup, built to their workflow | Apollo |

Always use the **Reframe Lens** before filtering on budget or listing type. LinkedIn job postings are the highest-value reframe channel we have.

---

## Failure History

| Date | Failure | Root Cause | Fix |
|---|---|---|---|
| 2026-04-27 | status=RUNNING, 0 results | wait_seconds=90 too short; no memory file existed | Set wait_seconds=150; created this file |

---

## Notes

- LinkedIn caps `applicantsCount` display at 25 — any value of `"25"` should be treated as "25+" and skipped
- `descriptionText` is the clean version; always use it over `descriptionHtml`
- `link` is the canonical job URL (uk.linkedin.com/jobs/view/...); `applyUrl` often redirects to external ATS
- The actor scrapes public LinkedIn job listings — no authentication required (ToS-compliant for public listings)
- Run one URL per search query; batch multiple queries by passing multiple URLs in the array to reduce total run time
