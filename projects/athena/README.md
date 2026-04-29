# Athena

> **AI Consultancy & Multi-Agent Deployment — the bridge between Apollo and Pantheon.**
>
> *"Add wisdom."*

**Price**: £750/month

## Overview

Athena is Cognito's mid-tier AI engagement: a **full business audit** to identify where AI adds value, plus **2–3 configured agents** deployed for specific workflows in your business. It bridges the gap between Apollo (the entry-level assistant) and Pantheon (the full custom build).

**Apollo sits on top as your single point of contact.** You instruct Apollo in plain English. Apollo briefs the right specialist underneath — CMO for content, Scout for leads, Ops for tasks. You never manage the stack. You manage Apollo.

Athena is for businesses that:
- Know AI could help but don't know where to start
- Want more than a single assistant but aren't ready for a £2,500+ Pantheon build
- Need an expert to map their workflows, spot opportunities, and deploy real agents

Athena is the mid-tier of Cognito's three-tier AI stack:

> **Apollo (£29.99/mo) → Athena (£750/mo) → Pantheon (£2,500+)**
>
> *"Start with knowledge. Add wisdom. Build your temple."*

## The Apollo-Conductor Architecture

```
         YOU
          │
          ▼
    ┌─────────────┐
    │   APOLLO    │  ← Your single point of contact
    │ (Telegram)  │     Natural language. Plain English.
    └──────┬──────┘
           │  Apollo briefs the right specialist
           │
     ┌─────┼──────┐
     ▼     ▼      ▼
  [CMO]  [Scout] [Ops]
 content  leads  tasks
```

You instruct Apollo. Apollo runs the team. You never manage the stack — **you manage Apollo**.

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

### 4. 2–3 Configured Agents (Apollo-Conducted)
The part that makes Athena different from a generic consultancy engagement. We don't just write a document — we **deploy working agents** for 2–3 of the highest-value workflows identified in the audit, with Apollo as the interface over them. Examples from past engagements:

- **Proposal Drafter** — reads a job listing, drafts a full proposal in the client's brand voice
- **Receipt Scanner** — inbox-monitoring agent that extracts expense data and logs to accounts
- **Outreach Agent** — pulls leads from a source, drafts personalised first-touch messages
- **Meeting Summariser** — listens to transcripts, extracts action items, emails them out
- **Content Repurposer** — takes a long-form video, produces LinkedIn, Instagram, and Twitter variants

### 5. 60-Minute Debrief
Live session to walk through the audit, the agents, the implementation plan, and answer questions. Recording provided.

## Delivery Timeline

| Week | What happens |
|------|--------------|
| 1 | Kick-off call, workflow interviews, access to relevant systems |
| 2 | Audit write-up, opportunity map drafting |
| 3 | Agent configuration and deployment |
| 4 | Debrief call, handover document, 7 days of post-delivery support |

## Tech Stack

Athena agents are typically built on the same stack Cognito uses internally:

- **Orchestration**: Claude API (Sonnet 4) + skill routing
- **Integration**: MCP tools for Gmail, Drive, Calendar, Stripe, HTTP APIs
- **Hosting**: Client's existing infrastructure or a Cognito-hosted container (client's choice)
- **Handover**: Full source access — the client owns what's built

## Lessons Learned

### What Worked Well

**A £750/month fee removes every objection.** Clients who balk at a £2,500 Pantheon build say yes to a £750/month Athena engagement. It's small enough to feel safe, large enough for us to do real work, and profitable enough to be worth building for.

**The audit on its own justifies the fee.** Even without the agents, clients tell us the workflow review is the clearest picture they've ever had of their own operation. The agents are the kicker.

**2–3 is the right number.** One agent feels like a trial. Four or more bloats the scope and missed deadlines. Two to three hits the sweet spot — enough to prove AI can pay for itself, few enough to ship in a month.

**Athena is the natural Pantheon upsell.** Roughly half of Athena clients want a full Pantheon build after seeing two agents running for 30 days. The agents deployed in Athena migrate straight into the Pantheon stack when they upgrade.

### What We'd Do Differently

**Scope the agents before signing.** Early Athena engagements drifted because "we'll pick the agents after the audit" meant clients kept adding candidates. We now scope 2–3 agent slots at kick-off and lock them by end of week 1.

**Charge more for complex integrations.** The monthly fee assumes the agents integrate with common systems (Gmail, Stripe, standard CRMs). When a client needs a custom API bridge or legacy-system connector, that's extra.

**Ship a starter pack of "known-good" agent templates.** Instead of designing each agent from scratch, we now start from proven templates and tune them to the client. Cuts delivery time by a week.

---

*Part of the Cognito AI stack: [Apollo](../apollo) → [Athena](./) → [Pantheon](../pantheon)*

*Built by [Cognito Coding](https://cognitocoding.com)*
