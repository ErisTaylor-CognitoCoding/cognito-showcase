# Moirai

> **AI Consultancy & Multi-Agent Deployment — the bridge between Apollo and Pantheon.**
>
> *"Add wisdom."*

**Price**: £750 fixed fee

## Status

🟢 **[Live demo at moirai.cognitocoding.app](https://moirai.cognitocoding.app)** — Social Media vertical end-to-end, seeded with the PeakForm demo client. Anyone can click through and see Moirai in action. No paying clients yet. Real social API publishing (Instagram / Facebook / X) and live DM/comment ingestion are V2 milestones.

## Overview

Moirai is Cognito's mid-tier AI engagement: a **full business audit** to identify where AI adds value, plus **2–3 configured specialist agents** deployed for your highest-value workflows. **Apollo sits on top as your single point of contact — you instruct Apollo in plain English, Apollo briefs the specialist agents underneath. You never manage the stack — you manage Apollo.**

```
         YOU
          │
          ▼
    ┌─────────────┐
    │    APOLLO   │  ← Your single point of contact
    │  Conductor  │     Natural language. Plain English.
    └──────┬──────┘
           │  Apollo briefs the right specialist
           │
     ┌─────┼──────┐
     ▼     ▼      ▼
  [CMO]  [Scout] [Ops]
 content  leads  tasks
```

Moirai is for businesses that:
- Know AI could help but don't know where to start
- Want more than a single assistant but aren't ready for a £2,500+ Pantheon build
- Need an expert to map their workflows, spot opportunities, and deploy real agents

Moirai is the mid-tier of Cognito's three-tier AI stack:

> **Apollo (£29.99/mo) → Moirai (£750) → Pantheon (£2,500+)**
>
> *"Start with knowledge. Add wisdom. Build your temple."*

## What's Included

### 1. Full Workflow Review
A structured audit of the client's operations. We spend time with the client mapping:
- What they do every day / week / month
- Where time is lost to repetitive admin
- Where humans are doing work a well-configured agent could do
- Where data is flowing manually between systems

### 2. AI Opportunity Map
A written document the client keeps, covering:
- Every workflow where AI could add value
- Ranked by impact vs. effort
- Concrete tools and approaches for each
- What's feasible this quarter vs. next year

### 3. Implementation Plan
A practical, phased plan — not a fantasy roadmap. What to deploy in month 1, what to revisit in month 3, what to budget for if they want to scale to a full Pantheon build later.

### 4. 2–3 Configured Specialist Agents (Apollo-Conducted)
The part that makes Moirai different from a generic consultancy engagement. We don't just write a document — we **deploy working agents** for 2–3 of the highest-value workflows identified in the audit.

These agents run underneath Apollo — you never interact with them directly. You instruct Apollo; Apollo assigns the work to the right specialist and reports results back to you in plain English. Example use cases:

- **Proposal Drafter** — reads a job listing, drafts a full proposal in the client's brand voice
- **Receipt Scanner** — inbox-monitoring agent that extracts expense data and logs to accounts
- **Outreach Agent** — pulls leads from a source, drafts personalised first-touch messages
- **Meeting Summariser** — listens to transcripts, extracts action items, emails them out
- **Content Repurposer** — takes a long-form video, produces LinkedIn, Instagram, and Twitter variants

### 5. 60-Minute Debrief
Live session to walk through the audit, the agents, the implementation plan, and answer questions. Recording provided.

## Delivery Timeline

| Week | What happens |
|------|-------------|
| 1 | Kick-off call, workflow interviews, access to relevant systems |
| 2 | Audit write-up, opportunity map drafting |
| 3 | Agent configuration and deployment |
| 4 | Debrief call, handover document, 7 days of post-delivery support |

## Tech Stack

Moirai agents are typically built on the same stack Cognito uses internally:

- **Orchestration**: Claude API (Sonnet 4) + skill routing
- **Integration**: MCP tools for Gmail, Drive, Calendar, Stripe, HTTP APIs
- **Hosting**: Client's existing infrastructure or a Cognito-hosted container (client's choice)
- **Handover**: Full source access — the client owns what's built

## Design Learnings

> **Note:** Moirai launched as a live demo in May 2026. These reflections are drawn from building and refining the product — not from paying client engagements, which are still to come.

### What Worked Well

**A £750 fixed fee removes the barrier.** Businesses that would balk at a £2,500 Pantheon build can commit to a £750 Moirai engagement. It's small enough to feel safe, large enough to do real work, and a genuine stepping stone to the full platform.

**The audit on its own justifies the fee.** Even without the agents, a well-run workflow review gives businesses the clearest picture they've ever had of their own operation. The agents are the kicker.

**2–3 is the right number.** One agent feels like a trial. Four or more bloats scope and risks missed deadlines. Two to three hits the sweet spot — enough to prove AI can pay for itself, few enough to ship in a month.

**Moirai is the natural Pantheon stepping stone.** The architecture is designed so the agents deployed in Moirai migrate straight into the Pantheon stack when a business is ready to scale up.

### What We'd Do Differently

**Scope the agents before signing.** Scope drift happens when "we'll pick the agents after the audit" means candidates keep getting added. The right approach: scope 2–3 agent slots at kick-off and lock them by end of week 1.

**Charge more for complex integrations.** £750 assumes agents integrate with common systems (Gmail, Stripe, standard CRMs). Projects needing a custom API bridge or legacy-system connector should be priced higher.

**Ship a starter pack of known-good agent templates.** Starting from proven templates and tuning to the client cuts estimated delivery time by a week compared to designing each agent from scratch.

---

*Part of the Cognito AI stack: [Apollo](../apollo) → [Moirai](./) → [Pantheon](../pantheon)*

*Built by [Cognito Coding](https://cognitocoding.com)*
