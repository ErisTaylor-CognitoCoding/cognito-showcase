# Moirai

> **Apollo-conducted multi-agent platform.**
>
> *"Add wisdom."*

## Status

🟢 **[Live demo at athena.cognitocoding.app](https://athena.cognitocoding.app)** — Social Media vertical, seeded with the PeakForm demo. Apollo conductor + three specialists (Content Creator, Scheduler, Engagement). Built May–June 2026.

---

## What It Does

Moirai deploys 2–3 specialist agents for a business's highest-value workflows. **Apollo sits on top as the single point of contact — you instruct Apollo in plain English, Apollo briefs the specialists underneath. You never manage the stack — you manage Apollo.**

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

---

## Conductor Branding

The conductor can be named anything — the architecture underneath doesn't change:

| Use case | Name |
|----------|------|
| Lead-gen / sourcing / outbound | Scout |
| Marketing / social / content / ads | Herald |
| Anything else or mixed | Apollo |
| Custom | Client-named |

---

## What Specialist Agents Can Do

Examples of agents deployed under the conductor:

- **Proposal Drafter** — reads a brief, drafts a full proposal in the client's brand voice
- **Receipt Scanner** — monitors inbox, extracts expense data, logs to accounts
- **Outreach Agent** — pulls leads from a source, drafts personalised first-touch messages
- **Meeting Summariser** — extracts action items from transcripts, emails them out
- **Content Repurposer** — takes a long-form video, produces LinkedIn/IG/Twitter variants

---

## Design Learnings

Reflections from building and refining the product.

**Lock agent scope early.** "We'll pick the agents after the audit" leads to scope drift. Lock 2–3 agent slots at kick-off and freeze them by end of week 1.

**2–3 is the right number.** One agent feels like a trial. Four or more bloats scope. Two to three is enough to prove the model without overengineering.

**Templates beat blank-slate builds.** Starting from proven agent templates and tuning to the use case is significantly faster than designing each agent from scratch.

**The conductor pattern scales cleanly.** The same architecture that works in Moirai — one conductor, N specialists — scales directly to a larger agent roster. You just add specialists underneath without changing how the client interacts with the system.

**Complex integrations need extra time.** Agents integrating with common systems (Gmail, Stripe, standard CRMs) are fast to ship. Custom API bridges or legacy-system connectors need explicit scoping upfront.

---

## Tech Stack

- **Orchestration**: Claude API (Sonnet 4) + skill routing
- **Integration**: MCP tools for Gmail, Drive, Calendar, Stripe, HTTP APIs
- **Database**: PostgreSQL
- **Server**: Python / Flask
- **Deployment**: Docker (containerised per environment)

---

*Part of the Cognito build portfolio: [Apollo](../apollo) → [Moirai](./) → [Pantheon](../pantheon)*

*Built by [Cognito Coding](https://cognitocoding.com)*
