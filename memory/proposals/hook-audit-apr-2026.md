# Proposal Hook Audit — April 2026

**Date:** 2026-04-26 (updated)
**Audited by:** Scout
**Scope:** Last 10 Upwork proposals (IDs 82–91, dated 2026-04-23 and 2026-04-24)
**Win rate:** 13+ proposals sent, **0 wins**

---

## Upwork Actor Status

**Actor:** `neatrat/upwork-job-scraper`
**Status:** ✅ WORKING — confirmed 2026-04-26 at ~08:00 BST
**Fix:** Must use `wait_seconds=150`. Default 60s and 90s both stall at RUNNING.
**Root cause of today's failure:** Daily scan used wait_seconds=60 → actor returned status=RUNNING → 0 results → all 5 proposals came from Freelancer.
**Memory file updated:** `memory/apify/upwork/neatrat~upwork-job-scraper.md`

---

## TL;DR — The Primary Failure

**All 10 proposals had `**Strand: [type]**` as the literal first line.**

On Upwork, clients see ~300 characters in the feed preview before clicking "Read More." Every single proposal showed internal metadata as the first visible text. Clients scanning 50 proposals in a competitive feed saw:

> `**Strand: Athena (ai_consultancy_multi_agent)**`

…as the opener. This is an instant disqualification signal — it telegraphs that the proposal is AI-templated. Click-through rate is effectively 0%.

**This is a Scout formatting error.** The `pantheon-proposal-writing` skill is explicit: strand label goes at the END, after `---`, marked `[INTERNAL — DELETE BEFORE SUBMITTING]`. Not at the top.

---

## Full 10-Proposal Breakdown (82–91)

### Proposal 82 — Build AI Agents for Real Estate Lead Generation
- **First line sent**: `**Strand: Pantheon (custom_build)**` ❌
- **Actual hook** (buried): *"You said 'NOT a basic Zapier setup.' Good — because what you've described isn't workflow plumbing. It's a decision-making system."*
- **Hook quality**: ✅ STRONG — Variant A (Insight). Mirrors their explicit requirement, reframes to the real problem. Would earn a click.
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 83 — Python + Supabase Operator (Whiskey Database)
- **First line sent**: `**Strand: Pantheon (bespoke_build)**` ❌
- **Actual hook** (buried): *"WHISKEY\n\nThe acceptance criterion — 'scroll for 5 minutes without a glitch' — is actually a clearer brief than most data projects."*
- **Hook quality**: ✅ STRONG — all-caps WHISKEY satisfies the hidden test instruction in the brief; the insight that follows ("clearer brief than most — I know exactly what done means") is genuine Variant A.
- **Verdict**: Strong, brief-aware proposal. Killed by label placement.

### Proposal 84 — Make.com AI Automation for Real Estate Deal Scouting
- **First line sent**: `**Strand: Athena (ai_automation)**` ❌
- **Actual hook** (buried): *"Make.com gives you workflow plumbing. It moves data when conditions are met. Real estate deal scouting is a different problem — you need something that reads signals and decides which properties are worth chasing. Those aren't the same job."*
- **Hook quality**: ✅ STRONG — Variant A/B hybrid. Challenges the tool choice with insight. Specific and credible.
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 85 — Lead Generation & Email Finder (B2B Daily Pipeline)
- **First line sent**: `**Strand: Athena (ai_automation)**` ❌
- **Actual hook** (buried): *"You've described a job for a human to spend their day in Hunter looking up emails and copying them into Airtable. That's not a hiring problem — it's an automation gap."*
- **Hook quality**: ✅ STRONG — Variant A (Insight). Names the exact bottleneck (Hunter + Airtable), labels it correctly ("automation gap"). Clean.
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 86 — Supply Chain Web App (React, Node.js, API Integrations)
- **First line sent**: `**Strand: Pantheon (custom_build)**` ❌
- **Actual hook** (buried): *"You've designed the prototype and know what you want. The build risk isn't the frontend or the Shipsgo integration — it's getting the Claude AI layer to do something actually useful rather than sitting there as a chatbot bolted onto a dashboard."*
- **Hook quality**: ✅ STRONG — Variant A (Insight). Names the real risk they haven't addressed. Specific to their brief (Shipsgo named, Claude AI layer named).
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 87 — AI Claude Integration Specialist
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent)**` ❌
- **Actual hook** (buried): *"The bottleneck isn't knowledge — it's structure. Your team has 20 years of data and a full MS suite, but reports are slow, decisions feel patchy, and the workflows that should be automatic aren't. That's not a people problem."*
- **Hook quality**: ✅ STRONG — Variant A (Insight). Mirrors the brief, names the unspoken problem.
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 88 — Deep Research Contractor, B2B Contact Enrichment (Commercial Real Estate)
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent)**` ❌
- **Actual hook** (buried): *"A 45-day contractor gives you a list. A £750/month system gives you a list you can refresh next quarter, next year, for every new market you enter."*
- **Hook quality**: ✅ STRONG — Variant B (Reframe). Clean ROI contrast, specific price, no adversarial framing.
- **Verdict**: Strong proposal. Killed by label placement.

### Proposal 89 — Python Developer, Bulk Lead Enrichment Pipeline
- **First line sent**: `**Strand: Pantheon (bespoke_custom_build)**` ❌
- **Actual hook** (buried): *"Spec's ready, API waterfall defined, deliverable clear — this is exactly how we like to work."*
- **Hook quality**: ⚠️ WEAK — Confirms their framing rather than naming a problem. Could apply to any pipeline brief. No insight, no reframe, no named proof point.
- **Verdict**: Two problems — bad placement AND weak hook. See revised hook below.

### Proposal 90 — Bot to Visit Site and Verify Appointments
- **First line sent**: `**Strand: Small Business App (£9.99/mo hosted)**` ❌
- **Actual hook** (buried): *"You don't need a contractor for this — you need a tool you own that runs on a schedule forever."*
- **Hook quality**: ❌ BANNED — "You don't need X" is explicitly listed as adversarial framing in the `pantheon-proposal-writing` skill.
- **Verdict**: Two violations — bad placement AND banned opener pattern.

### Proposal 91 — Data Research Specialist, Exporter List Build
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent) — pilot first, then automated pipeline**` ❌
- **Actual hook** (buried): *"I can cover both tasks in your pilot. But let me also show you the longer game."*
- **Hook quality**: ⚠️ WEAK — "I can cover both tasks" is generic confirmation. "Longer game" is vague. No problem named, no reframe, no proof.
- **Verdict**: Bad placement AND weak hook.

---

## Score Summary (all 10)

| ID | Title snippet | Label at top | Hook quality | Recoverable? |
|---|---|---|---|---|
| 82 | Real Estate AI Agents | ❌ FATAL | ✅ Strong (A) | Move label to bottom |
| 83 | Whiskey Database | ❌ FATAL | ✅ Strong (A+hidden test) | Move label to bottom |
| 84 | Make.com Real Estate | ❌ FATAL | ✅ Strong (A/B) | Move label to bottom |
| 85 | B2B Lead Enrichment | ❌ FATAL | ✅ Strong (A) | Move label to bottom |
| 86 | Supply Chain Web App | ❌ FATAL | ✅ Strong (A) | Move label to bottom |
| 87 | Claude Integration | ❌ FATAL | ✅ Strong (A) | Move label to bottom |
| 88 | B2B Contact Enrichment | ❌ FATAL | ✅ Strong (B) | Move label to bottom |
| 89 | Pipeline Build | ❌ FATAL | ⚠️ Weak | Hook rewrite + label fix |
| 90 | Appointment Bot | ❌ FATAL | ❌ Banned | Hook rewrite + label fix |
| 91 | Exporter List | ❌ FATAL | ⚠️ Weak | Hook rewrite + label fix |

**10 of 10 proposals have the strand label as line 1.** 7 of 10 have strong underlying hooks that would have earned clicks if the label hadn't blocked them. 3 of 10 need hook rewrites.

---

## Root Cause Analysis

The `pantheon-proposal-writing` skill specifies:

```
[hook line 1]
[insight paragraph]
[build bullets]
[credentials]
[close]
---
See our work: https://github.com/ErisTaylor-CognitoCoding/cognito-showcase

Best,
Eris

---
[INTERNAL — DELETE BEFORE SUBMITTING TO CLIENT]
Strand: Athena (ai_automation)
Hook variant used: B (Reframe)
```

What Scout has been saving to Pantheon's `body` field:

```
**Strand: Athena (ai_consultancy_multi_agent)**

[hook line 1 — buried]
...
```

The label is at the TOP, not the bottom. Result: Upwork clients see `**Strand: Athena (ai_consultancy_multi_agent)**` in the 300-char preview. Every proposal is self-identifying as AI-templated before a human reads a word.

**The fix is entirely in Scout's output structure**, not in the content quality.

---

## Revised Hook Patterns for Weak/Banned Proposals

### For listing type: "Spec-ready pipeline build" (like #89)
**Weak**: "Spec's ready, API waterfall defined, deliverable clear — this is exactly how we like to work."

**Revised (Variant C — Proof):**
> Scout — my production proposal agent — runs a CSV-in, enriched-CSV-out waterfall daily: Apify ingest, API enrichment, Postgres per-record status, async queue, error logging. Your pipeline is the same architecture against your data.
> Fixed-fee quote within 24 hours of seeing your spec. No hourly.

**Why stronger**: Names a specific Cognito system (Scout), describes the actual architecture match, leads with proof not confirmation.

---

### For listing type: "Solo operator wants monitoring/automation tool" (like #90)
**Banned**: "You don't need a contractor for this — you need a tool you own..."

**Revised (Variant A — Insight):**
> Appointment slots at a high-demand booking site fill in minutes — by the time you're manually checking, they're gone.
> A headless monitor checking every 5 minutes, emailing you the instant one opens, costs £9.99/month and never blinks. Free to build; billing starts when it's working.

**Why stronger**: Names the actual urgency (slots fill fast), shows the mechanic (headless + email), states the price and USP without being adversarial.

---

### For listing type: "Pilot research project with implied ongoing need" (like #91)
**Weak**: "I can cover both tasks in your pilot. But let me also show you the longer game."

**Revised (Variant B — Reframe):**
> Building an exporter list manually means repeating the same researcher hours every time you enter a new market — the work doesn't compound.
> An Athena pipeline runs the build on demand: registry scrape, contact enrichment, enriched CSV — £750/month, no setup fee, same output the second time costs nothing extra.

**Why stronger**: Names the specific ongoing cost of the manual approach (non-compounding work), shows exactly what the product does differently, states the price upfront.

---

## Corrective Actions (for all future proposals — non-negotiable)

### 1. Label placement fix
The `body` field saved to `pantheon_create_proposal` must start with the hook. The strand label goes at the very end, after sign-off:

```
[hook line 1 — THIS is the first character of `body`]
[hook line 2]

[insight paragraph]

[build bullets]

[credentials]

[close]

---
See our work: https://github.com/ErisTaylor-CognitoCoding/cognito-showcase

Best,
Eris

---
[INTERNAL — DELETE BEFORE SUBMITTING TO CLIENT]
Strand: [type]
Hook variant used: [A/B/C]
```

### 2. Pre-save hook checklist
Before calling `pantheon_create_proposal`, verify:
- [ ] First character of `body` is NOT `*` (bold metadata marker)
- [ ] First 2 lines pass the "300 chars test" — does this earn a click on its own?
- [ ] Chosen Variant (A/B/C) matches today's calendar rule (`calendar_day % 3`)
- [ ] "You don't need X" banned pattern is not in lines 1-2
- [ ] No "Hi, I'm Eris Taylor from Cognito Coding" opener
- [ ] Hook is specific to THIS brief — couldn't apply to 20 other listings unchanged

### 3. Variant assignment by calendar day
| Day % 3 | Variant | Style |
|---|---|---|
| 0 | C — Proof Hook | Lead with a named Cognito system |
| 1 | A — Insight Hook | Name the unspoken problem |
| 2 | B — Reframe Hook | Show the product alternative with price |

April 26 (26 % 3 = 2) → **Variant B (Reframe)** today.

---

## A/B Test Status

**Cannot report reliable variant data** because all submitted proposals had strand labels as line 1 — clients never saw the actual hook variant. The A/B test is effectively corrupted for all proposals before 2026-04-26.

Once the label placement is fixed, variant tracking will be meaningful. First clean data after 2026-04-26.

---

## Key Insight for Zero

**The proposals are not bad.** 7 of 10 contain strong, specific hooks that follow the PITCH framework correctly. The underlying content quality is acceptable to good.

**The format is broken.** The strand label at the top of every body field is the single highest-impact fix available. Correcting it could immediately lift click-through rates without changing any proposal content.

**Hypothesis**: If the label issue is fixed and 0 clicks → 0 wins persists after 15 clean proposals (3 more daily runs), the root cause is the body quality, not the preview. At that point, audit the credential section and the CTA specificity.
