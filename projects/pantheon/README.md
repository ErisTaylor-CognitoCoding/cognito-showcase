# Pantheon

> **Your own AI-powered business command centre — Apollo orchestrates a bespoke specialist team built around your operation.**
>
> *"Build your temple."*

**Price**: £2,500+ fixed fee (flagship tier of the Cognito AI stack)

## Overview

Pantheon is a custom private instance of the full Cognito stack, configured for your business. Not a template, not a shared platform — **your data, your database, your branding, your infrastructure**. Cognito deploys and maintains; you own the workflow.

**Apollo orchestrates a bespoke specialist team built around your business.** Same conductor model as Athena, scaled up: you instruct Apollo in natural language, Apollo briefs the specialist agents underneath. You never manage the stack — you manage Apollo.

Pantheon is the flagship tier of Cognito's three-tier AI stack:

> **Apollo (£29.99/mo) → Athena (£750/mo) → Pantheon (£2,500+)**
>
> *"Start with knowledge. Add wisdom. Build your temple."*

Pantheon was built from three earlier systems — a business dashboard, Apollo's AI executive assistant, and an agent execution engine — unified into a single platform in April 2026. **Cognito Coding itself runs on Pantheon every day.** Nova, CMO, CFO, Scout, CTO and the rest of the agent roster all live in production on the same stack we deploy for clients.

## What You Get

### 1. Your Own Dashboard
One place to run the business:
- **CRM** — client lifecycle, contacts, last-contact tracking
- **Invoicing** — drafts, send-ready PDFs, payment status
- **Accounts ledger** — income, expenses, Stripe sync, Gmail receipt scanning, UK tax-year filtering
- **Kanban** — task board: backlog → todo → in progress → in review → done
- **Proposals** — Scout-drafted, Apollo-reviewed, status tracking
- **Newsletter** — draft, preview, scheduled send
- **Company doc** — single source of truth for products, pricing, brand voice
- **Skills library** — reusable Markdown playbooks agents read at runtime
- **Routines** — cron-scheduled agent jobs
- **Secrets vault** — encrypted storage for API keys

### 2. Your Own Apollo — The Conductor
An AI executive assistant embedded in Discord / Slack / Telegram. This is your single point of contact into the entire Pantheon stack:

- Reads your inbox and surfaces what matters
- Manages your calendar
- Runs morning briefings with overnight activity summary
- Conducts outreach and chases leads
- **Briefs the specialist team and reports results back to you**

You instruct Apollo in plain English. Apollo decides which specialist to brief, coordinates across the team, and keeps you informed. You never open an agent panel or write a prompt — you talk to Apollo.

### 3. Your Specialist Agent Team — Conducted by Apollo
Apollo orchestrates this team on your behalf. Each agent is a real employee-style persona with a custom system prompt, default skill set, and cron schedule. You never interact with individual agents directly — Apollo does that.

| Agent | What They Do |
|-------|-------------|
| **CTO** | Technical execution, infrastructure monitoring, code reviews |
| **CMO** | Content creation, social scheduling, proposal writing, lead nurturing |
| **CFO** | Stripe sync, receipt scanning, expense tracking, weekly P&L |
| **Scout** | Upwork and LinkedIn prospecting, outreach drafting |
| **Engineer** | Code changes, shell-level automation, integrations |

Agents are **not chatbots**. They run on cron schedules (routines), execute autonomously, report to Apollo, and log every action (`agent_runs` table) for audit.

### 4. Configured for Your Business
Personas, brand voice, pricing, workflows — all tuned to your operation, not a generic chatbot bolted onto a template.

### 5. Claude Max Under the Hood
All agent execution runs on Claude Max subscription billing, not per-token API billing. No surprise spend. No bill shock. Predictable monthly infrastructure cost.

### 6. Fully Private and Audited
- Every agent action logged
- Secrets encrypted at rest
- Destructive operations require confirmation
- Per-client database isolation — your data never mixes with anyone else's

## Tech Stack

- **Backend**: Python 3.11 + Flask
- **Database**: PostgreSQL (per-client isolated database)
- **AI**: Anthropic Claude (Sonnet 4 / Opus 4) via Claude Max
- **Agent runtime**: MCP tools + cron scheduler, unified Pantheon runtime
- **Frontend**: HTML/CSS/JS (server-rendered, no framework bloat)
- **Deployment**: Docker Compose (containerised, per-client)
- **Auth**: Session-based with bcrypt

## Architecture

```
              YOU
    (Discord / Slack / Telegram)
               │
               ▼
┌──────────────────────────────────────────────┐
│         Apollo — The Conductor               │
│   Single point of contact. Natural language. │
│   Briefs the right specialist. Reports back. │
└──────────────────────────────────────────────┘
               │
┌──────────────────────────────────────────────┐
│             Pantheon Web UI                  │
│  CRM │ Invoices │ Accounts │ Kanban          │
│  Proposals │ Newsletter │ Skills │ Routines  │
└──────────────────────────────────────────────┘
               │
┌──────────────────────────────────────────────┐
│          Pantheon Agent Runtime              │
│  CTO │ CMO │ CFO │ Scout │ Engineer          │
│  Skills library │ Routines │ Agent logs      │
└──────────────────────────────────────────────┘
               │
┌──────────────────────────────────────────────┐
│      PostgreSQL (Per-Client Isolation)       │
│  clients │ contacts │ proposals │ tasks      │
│  accounts │ agent_runs │ secrets │ skills    │
└──────────────────────────────────────────────┘
```

## Why It's Not Niche

Any business that deals with clients, leads, content, or ops can run on Pantheon. Law firms, dental practices, tradespeople, coaches, agencies, consultancies, service businesses.

If our education product DashDeck is *"the command centre for tutors"*, **Pantheon is the command centre for any business.**

## Proof It Works

Cognito Coding itself runs on Pantheon:

- **Apollo** runs our outreach and morning briefings
- **Scout** hunts job listings and drafts proposals every weekday
- **CMO** schedules social posts, drafts newsletters, produces YouTube videos
- **CFO** syncs Stripe and scans Gmail receipts into the accounts ledger
- **CTO** monitors infra and triages every agent failure
- The dashboard is the first thing Zero opens every morning

We didn't build this theoretically. We built it because we needed it, and now we deploy the same stack for other businesses.

## Lessons Learned

### What Worked Well

**Agents as employees, not chatbots.** Treating agents like team members (with roles, personas, routines) made them feel part of the operation. Zero doesn't "use a tool" — he works with Nova, CMO, Scout.

**Skills library prevents drift.** Reusable Markdown playbooks keep processes consistent. When CMO generates a thumbnail, the skill ensures the same template and brand style every time.

**Cron routines are killer.** Morning briefings, Stripe sync, receipt scanning happen automatically. Zero wakes up to a Discord message with the day's overview. This is the "magic moment" clients pay for.

**PostgreSQL handles everything.** No Redis, no caching layers, no NoSQL. Postgres + proper indexes + JSONB columns handle agent logs, conversation history, and CRM data beautifully.

**Docker isolates cleanly.** Each client gets their own container stack. Rebuild one without touching others. Logs stay separate.

**Claude Max beats per-token API billing.** Moving all background agent execution off per-token API billing onto Claude Max subscription removed the spend anxiety. Pantheon clients get predictable monthly infra, not a metered surprise.

### What We'd Do Differently

**UI polish comes last.** We built backend and agents first, UI second. The dashboard works but looks utilitarian. For client deployments, we now invest in frontend design earlier.

**Agent error handling.** When an agent fails (API timeout, malformed response), the error is logged but not always surfaced. We've since added a CTO routine that triages failed runs and comments on stuck tasks.

**Secrets management.** Current vault works but is custom-built. For larger client deployments we'd consider HashiCorp Vault or AWS Secrets Manager.

**Cost monitoring.** Even on Claude Max, some agents can burn hours of CLI time. Per-agent run tracking and alerting landed in the flagship build — we'd scaffold it in from day one next time.

---

*Part of the Cognito AI stack: [Apollo](../apollo) → [Athena](../athena) → [Pantheon](./)*

*Built by [Cognito Coding](https://cognitocoding.com)*
