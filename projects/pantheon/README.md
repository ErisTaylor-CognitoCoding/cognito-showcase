# Pantheon

> **The internal command centre Cognito Coding runs on — agents, tasks, content production, invoicing and secrets in one private Flask app.**

## Status

🔒 **Internal. Not a product, not for sale, not deployed for anyone else.**

Pantheon is the system the business actually runs on, every day. It was originally built as a sellable platform; that direction was dropped in June 2026 when Cognito Coding moved to a YouTube-and-apps model. What remains is a real production tool with a single user — and, as a showcase, an honest look at what running your own agent platform involves.

Everything below describes the live system, not a plan.

## What it does

One Flask app, one Postgres database, one browser tab that stays open all day.

| Area | What it holds |
|---|---|
| **Agents** | Roster, per-agent run history, failure triage, health stats |
| **Grind** | Fortnightly sprint board — tasks under per-category targets |
| **Routines** | Cron-scheduled agent jobs, with a watchdog for missed fires |
| **Skills** | Markdown playbooks agents read at runtime |
| **Video Docs** | Structured production records per YouTube episode — script, hook, thumbnail prompt, code links, publish status |
| **Challenges** | Coding challenges tracked from attempted through solved |
| **Tutoring** | Students, timetables, lessons, EHCP files, AQA outcomes, monthly invoicing |
| **Accounts** | Income and expenses, Stripe sync, Gmail receipt scanning, UK tax-year filtering |
| **Invoices** | Line items, PDF generation, send and mark-paid |
| **Newsletter** | Subscribers, drafts, live preview, scheduled send |
| **Company doc** | Single source of truth for products, schedule and brand voice |
| **Vault** | AES-256-GCM encrypted secrets |

Current live state: **4 agents** (3 AI, 1 human), **34 enabled routines**, **73 skills**, and **1,830 agent runs** logged for audit.

## Tech

- **Backend**: Python 3.11, Flask, SQLAlchemy, Gunicorn (gthread, 2 workers × 4 threads)
- **Frontend**: Jinja2 + HTMX + Alpine.js — server-rendered, no SPA build step
- **Database**: PostgreSQL 16
- **AI**: Claude, executed through the Claude CLI on a Max subscription — *not* the per-token API
- **Deployment**: Docker, single container plus its database

Designed dyslexia-friendly throughout: Atkinson Hyperlegible for body text, high contrast, icon-and-colour navigation, and a per-page scoped CSS system so one page's styling can never leak into another.

## The agent runtime

Agents are not chatbots. They are rows in a table with a Markdown persona, a model, a skill list and a schedule. A routine fires on cron, the runner assembles the prompt from the agent's persona plus its skills, executes it through the Claude CLI, and writes the result to `agent_runs` — every action auditable after the fact.

The roster is deliberately small. It was a wider set of narrow specialists — content, finance, prospecting, engineering, design — and is now three: **Nova**, the partner Zero actually talks to, who owns content and finance; **host-shell**, which handles infrastructure; and **git**, which maintains the repositories. Consolidating cut prompt bloat and made ownership obvious.

```
   Zero  ──talks to──▶  Nova  (Discord DM · web chat widget)
                          │
                          ├── reads/writes Pantheon via the bridge API
                          │
   cron ──fires──▶  Routines ──▶  agent runner ──▶ Claude CLI (Max sub)
                                        │
                                        ▼
                                   agent_runs  (full audit trail)
```

Nova reaches Pantheon over an internal bridge (`/api/nova/*`, shared-key auth) rather than touching the database, so every agent action goes through the same validation the UI does.

## Design learnings

Real ones, from running it rather than selling it.

### What worked

**Agents as scheduled jobs, not conversations.** The useful part was never the chat. It was a cron entry that reconciles Stripe at 07:00 without being asked.

**A skills library stops drift.** Reusable Markdown playbooks mean a thumbnail generated in November matches one from June. Prompts live in the database and are edited in the browser, not redeployed.

**Postgres is enough.** No Redis, no queue broker, no NoSQL. Postgres with sensible indexes and a few JSONB columns carries agent logs, conversation history and every domain table comfortably.

**Server-rendered beats an SPA here.** HTMX and Alpine cover every interaction this app needs. There is no build step, no bundle, no hydration bug — a page is a template.

**Subscription billing removed the anxiety.** All background execution runs through the Claude CLI on a Max subscription rather than per-token API billing. The failure mode of an agent looping is wasted time, not an unbounded invoice.

**Delta-only reporting.** Routines that sweep for changes keep a persistent ledger row and only notify when something actually changed. Without that, a daily sweep becomes noise you learn to ignore.

### What we'd do differently

**Retire features properly the first time.** Dropping a feature means removing its tools, its enum values, its skill mappings and its documentation — not just the page. Half-removed features leave tools that are advertised and then denied, which reads to an agent as a broken tool rather than a retired one.

**Enumerations belong in one place.** The same list of video lanes ended up copied into five files and drifted apart. One of them was missing a lane that had live records, so the agent could not create records on it at all.

**Surface agent failures louder.** Failures were logged from the start but not always surfaced. A routine that triages failed runs and comments on stuck tasks should exist from day one, not after the first silent week.

**Watch the drift between disk and git.** Code reaching the box outside version control means the running app can be correct while the repository is ten commits behind. Fetch before assuming, and check both directions.

---

*Built and run by [Cognito Coding](https://cognitocoding.com).*
