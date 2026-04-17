# Pantheon

> AI-powered business command centre — CRM, agents, invoicing, proposals, and automation in one private instance

## Overview

Pantheon is a custom AI-powered business operating system. It combines a web dashboard (CRM, invoicing, accounts, Kanban, proposals) with an AI agent team (Nova, CMO, CFO, Scout, CTO, Arthur) that runs the business alongside the founder.

Unlike SaaS platforms, Pantheon is **deployed per-client** with isolated infrastructure. Each client gets:
- Their own database (PostgreSQL)
- Their own AI agents (configured for their business)
- Their own branding and workflows
- Their own Discord/Slack/Telegram bot (Nova)

Cognito Coding itself runs on Pantheon. This is the tool we built for our own business, and we deploy the same stack for other companies.

## Tech Stack

- **Backend**: Python 3.11 + Flask
- **Database**: PostgreSQL (multi-tenant, per-client isolation)
- **AI**: Anthropic Claude API (Sonnet 4)
- **Agent Engine**: Paperclip (custom orchestration layer)
- **Frontend**: HTML/CSS/JS (server-rendered, no framework bloat)
- **Deployment**: Docker Compose (containerised services)
- **Auth**: Session-based with bcrypt

## Architecture

```
┌──────────────────────────────────────┐
│         DashDeck (Web UI)            │
│  CRM | Invoices | Accounts | Kanban  │
│  Proposals | Newsletter | Skills     │
└──────────────────────────────────────┘
                  ↓
┌──────────────────────────────────────┐
│       Paperclip (Agent Engine)       │
│  Nova | CMO | CFO | Scout | CTO      │
│  Arthur | Skills | Routines          │
└──────────────────────────────────────┘
                  ↓
┌──────────────────────────────────────┐
│  PostgreSQL (Multi-Tenant Database)  │
│  clients | contacts | proposals      │
│  accounts | tasks | agent_runs       │
└──────────────────────────────────────┘
```

## Key Features

### 1. **CRM Pipeline**
- Client lifecycle tracking (prospect → client → paused → churned)
- Contact management with email/phone
- Last contact timestamp (synced from outreach channels)
- Notes and history per client

### 2. **Proposal Builder**
- Draft proposals with AI assistance (Scout agent)
- Store job listings, client details, pricing
- Track status (draft → submitted → won → lost)
- Review queue for Nova

### 3. **Accounts Ledger**
- Income and expense tracking
- Stripe sync (auto-import charges)
- Gmail receipt scanning (CFO agent extracts invoice data from emails)
- Category tagging, client attribution
- Tax-year filtering (UK tax year: 6 Apr → 5 Apr)

### 4. **Grind Tracker (Kanban)**
- Task board: backlog → todo → in progress → in review → done
- Assign to agents or humans
- Priority levels (low/normal/high)
- Comments and history

### 5. **Agent Team**
Each agent is a Claude instance with a custom persona and toolset:

- **Nova** — CEO, morning briefings, email management, calendar, outreach coordination
- **CMO** — Marketing, content creation, video production, social media
- **CFO** — Finance, expense scanning, Stripe sync, P&L reports
- **Scout** — Job hunting (Upwork, LinkedIn), proposal drafting
- **CTO** — Technical execution, infrastructure monitoring
- **Arthur** — Code-level engineering, shell execution, Docker logs

Agents are **not chatbots**. They:
- Run on cron schedules (routines)
- Execute tasks autonomously
- Report results to Discord
- Have memory (agent_runs table logs every execution)

### 6. **Skills Library**
Reusable workflow playbooks (Markdown templates). Examples:
- How to draft a proposal
- How to generate a thumbnail
- How to scan a receipt and extract invoice data
- How to sync Stripe charges

Agents read skills during execution to follow consistent processes.

### 7. **Routines (Cron Scheduling)**
Agents run recurring jobs:
- **Nova**: Morning briefing (weekdays 9am)
- **CFO**: Stripe sync (daily), receipt scan (daily)
- **Scout**: Job board scrape (weekdays 10am)
- **CMO**: Social media scheduling checks

### 8. **Secrets Vault**
Encrypted storage for API keys:
- Stripe API key
- Gmail OAuth tokens
- Gemini API key (image generation)
- ElevenLabs API key (TTS)
- Veo3Gen API key (video generation)

Agents fetch secrets at runtime via Paperclip.

## Multi-Tenancy

Pantheon supports per-client database isolation. Each deployment can serve:
- **One business** (Cognito's own instance)
- **Multiple clients** (SaaS mode with tenant-scoped data)

Current implementation uses **per-client PostgreSQL databases** (Award Tracker, DashDeck Education clients).

## Lessons Learned

### What Worked Well

**Agents as employees, not chatbots**: Treating agents like team members (with roles, personas, routines) made them feel part of the operation. Zero doesn't "use a tool" — he works with Nova, CMO, Scout.

**Skills library prevents drift**: Reusable playbooks keep processes consistent. When CMO generates a thumbnail, the skill ensures the same template and brand style every time.

**Cron routines are killer**: Morning briefings, Stripe sync, receipt scanning happen automatically. Zero wakes up to a Discord message with the day's overview. This is the "magic moment" clients pay for.

**PostgreSQL handles everything**: No need for Redis, caching layers, or NoSQL. Postgres + proper indexes + JSONB columns handle agent logs, conversation history, and CRM data beautifully.

**Docker isolates cleanly**: Each service (DashDeck, Paperclip, Nova) in its own container. Rebuild one without touching the others. Logs stay separate.

### What We'd Do Differently

**UI polish comes last**: We built the backend and agents first, UI second. The dashboard works but looks utilitarian. For client deployments, we'd invest in frontend design earlier.

**Agent error handling**: When an agent fails (API timeout, malformed response), the error gets logged but not always surfaced to the user. Need better alerting and retry logic.

**Secrets management**: Current vault works but is custom-built. Would consider HashiCorp Vault or AWS Secrets Manager for enterprise clients.

**Cost monitoring**: Claude API usage can spike. We'd add per-agent token tracking and budget alerts before deploying for clients with tight margins.

---

*Built by [Cognito Coding](https://cognitocoding.com)*
