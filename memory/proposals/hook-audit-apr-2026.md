# Proposal Hook Audit — April 2026

**Date:** 2026-04-26  
**Audited by:** Scout  
**Scope:** Last 5 Upwork proposals (IDs 87–91, all dated 2026-04-24)  
**Win rate:** 13+ proposals sent, **0 wins**

---

## TL;DR — The Primary Failure

**All 5 proposals had `**Strand: [type]**` as the literal first line.**

On Upwork, clients see ~300 characters in the feed preview before clicking "Read More." Every single proposal showed internal metadata as the first visible text. Clients scanning 50 proposals in a competitive feed saw:

> `**Strand: Athena (ai_consultancy_multi_agent)**`

…as the opener. This is an instant disqualification signal — it telegraphs that the proposal is AI-templated. Click-through rate is effectively 0%.

**This is a Scout formatting error.** The `pantheon-proposal-writing` skill is explicit: strand label goes at the END, after `---`, marked `[INTERNAL — DELETE BEFORE SUBMITTING]`. Not at the top.

---

## Per-Proposal Breakdown

### Proposal 87 — AI Claude Integration Specialist
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent)**` ❌
- **Actual hook** (buried): *"The bottleneck isn't knowledge — it's structure. Your team has 20 years of data and a full MS suite, but reports are slow, decisions feel patchy, and the workflows that should be automatic aren't."*
- **Hook quality**: ✅ STRONG — Variant A (Insight), names the unspoken problem, specific to the brief
- **Verdict**: Good proposal. Completely killed by label placement.

### Proposal 88 — Deep Research Contractor, B2B Contact Enrichment
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent)**` ❌
- **Actual hook** (buried): *"A 45-day contractor gives you a list. A £750/month system gives you a list you can refresh next quarter, next year, for every new market you enter."*
- **Hook quality**: ✅ STRONG — Variant B (Reframe), clean ROI contrast, specific price, no adversarial framing
- **Verdict**: Strong proposal. Completely killed by label placement.

### Proposal 89 — Python Developer, Bulk Lead Enrichment Pipeline
- **First line sent**: `**Strand: Pantheon (bespoke_custom_build)**` ❌
- **Actual hook** (buried): *"Spec's ready, API waterfall defined, deliverable clear — this is exactly how we like to work."*
- **Hook quality**: ⚠️ WEAK — confirms their framing rather than naming a problem or showing proof. Could apply to any pipeline brief. No insight, no reframe, no named proof point.
- **Verdict**: Two problems — bad placement AND weak hook. See revised hook below.

### Proposal 90 — Bot to Visit Site and Verify Appointments
- **First line sent**: `**Strand: Small Business App (£9.99/mo hosted)**` ❌
- **Actual hook** (buried): *"You don't need a contractor for this — you need a tool you own that runs on a schedule forever."*
- **Hook quality**: ❌ BANNED — "You don't need X" is explicitly listed as adversarial framing in the `pantheon-proposal-writing` skill. Banned because it's confrontational before trust is established.
- **Verdict**: Two violations — bad placement AND banned opener pattern.

### Proposal 91 — Data Research Specialist, Exporter List Build
- **First line sent**: `**Strand: Athena (ai_consultancy_multi_agent) — pilot first, then automated pipeline**` ❌
- **Actual hook** (buried): *"I can cover both tasks in your pilot. But let me also show you the longer game."*
- **Hook quality**: ⚠️ WEAK — "I can cover both tasks" is generic confirmation. "Let me show you the longer game" is vague without substance. No problem named, no reframe, no proof.
- **Verdict**: Bad placement AND weak hook. See revised hook below.

---

## Root Cause Analysis

The `pantheon-proposal-writing` skill output format shows:

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

What Scout has been saving to Pantheon:

```
**Strand: Athena (ai_consultancy_multi_agent)**

[hook line 1 — buried]

...
```

The label is at the TOP, not the bottom. This means:
1. The Pantheon `body` field has the label as line 1
2. When Zero copies from `/proposals` and pastes into Upwork, the label is the first thing clients see
3. The pre-submit checklist ("delete from `---` separator downward") can't work if the separator is at the top

**Fix**: All future proposals must have the strand label at the very END, after the second `---` separator, below the sign-off. The first character of `body` must be the hook.

---

## Revised Hook Patterns for Weak Proposals

### For listing type: "Spec-ready pipeline build" (like #89)
**Weak**: "Spec's ready, API waterfall defined, deliverable clear — this is exactly how we like to work."

**Revised (Variant C — Proof):**
> Scout — my production proposal agent — runs a CSV-in, enriched-CSV-out waterfall pipeline daily: Apify ingest, API enrichment, Postgres per-record status, async queue, error logging. Your pipeline is the same architecture against your data.
> Fixed-fee quote within 24 hours of seeing your spec. No hourly.

**Why stronger**: Names a specific Cognito system (Scout), describes the actual architecture match, leads with proof not confirmation.

---

### For listing type: "Solo operator wants monitoring/automation tool" (like #90)
**Banned**: "You don't need a contractor for this — you need a tool you own..."

**Revised (Variant A — Insight):**
> Appointment slots at [target site] fill in minutes — by the time you're manually checking, they're gone.
> A headless monitor that checks every 5 minutes and emails you the moment one opens costs £9.99/month and never blinks. Free to build; billing starts when it's working.

**Why stronger**: Names the actual urgency (slots fill fast), shows the mechanic (headless + email), states the price and USP without being adversarial.

---

### For listing type: "Pilot research project with implied ongoing need" (like #91)
**Weak**: "I can cover both tasks in your pilot. But let me also show you the longer game."

**Revised (Variant B — Reframe):**
> Building an exporter list manually means repeating the same researcher hours every time you enter a new market — the work doesn't compound.
> An Athena pipeline runs the build on demand: registry scrape, contact enrichment, enriched CSV — £750/month, no setup fee, same output the second time costs you nothing extra.

**Why stronger**: Names the specific ongoing cost of the manual approach (non-compounding work), shows exactly what the product does differently, states the price upfront.

---

## Impact Assessment

| Proposal | Label as line 1 | Hook quality | Recoverable? |
|---|---|---|---|
| 87 — Claude Integration | ❌ FATAL | ✅ Strong (A) | Yes — move label to bottom |
| 88 — B2B Enrichment | ❌ FATAL | ✅ Strong (B) | Yes — move label to bottom |
| 89 — Pipeline Build | ❌ FATAL | ⚠️ Weak | Needs hook rewrite + label fix |
| 90 — Appointment Bot | ❌ FATAL | ❌ Banned opener | Needs full hook rewrite + label fix |
| 91 — Exporter List | ❌ FATAL | ⚠️ Weak | Needs hook rewrite + label fix |

**Conservative estimate**: proposals 87 and 88 would have earned clicks with correct formatting. Proposals 89, 90, 91 needed hook rewrites regardless.

---

## Corrective Actions (for all future proposals)

### 1. Label placement — non-negotiable
```
[hook line 1]
[hook line 2]
...
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

The `body` field saved to `pantheon_create_proposal` must start with the hook, never with `**Strand:**`.

### 2. Hook checklist before saving
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

April 24 (24 % 3 = 0) → should have been Variant C. Not determinable from saved proposals.  
April 26 (26 % 3 = 2) → Variant B (Reframe) today.

---

## A/B Test Status

**Cannot report reliable variant data** because all submitted proposals had strand labels as line 1 — clients never saw the actual hook variant. The A/B test is effectively corrupted for April 17–26. 

Once the label placement is fixed, the variant tracking will be meaningful. First clean data after 2026-04-26.
