# Cognito Coding — Portfolio & Showcase

**Production code patterns, AI agent examples, and project showcases from Cognito Coding.**

This repository demonstrates the technical foundations behind Cognito's products — multi-tenant architecture, AI orchestration, OAuth flows, and Docker infrastructure.

## 🎯 What We Build

Cognito Coding builds AI-powered business automation and educational platforms. Our AI tier is structured in three levels:

> **Start with knowledge. Add wisdom. Build your temple.**

| Tier | Product | Price |
|------|---------|-------|
| 🟠 Entry | **[Apollo](./projects/apollo)** — Per-client AI executive assistant | £29.99/month |
| 🟡 Mid | **[Athena](./projects/athena)** — AI audit + multi-agent consultancy | £750/month |
| 🔵 Flagship | **[Pantheon](./projects/pantheon)** — Full custom AI business command centre | From £2,500 (fixed fee) |

Plus:

- **Small Business Apps** — Niche tools for trades and professionals at £9.99/month ([WagTracker](./projects/wagtracker), [SoloTutorLite](./projects/solo-tutor-lite), and more)
- **Education Platform** — [EducationDashDeck](./projects/education-dashdeck) — modular ecosystem for tutoring agencies and SEND providers

## 📂 Repository Structure

```
cognito-showcase/
├── projects/                     # Project showcases (sanitised)
│   ├── apollo/                   # AI executive assistant (£29.99/mo)
│   ├── athena/                   # AI audit + multi-agent consultancy (£750/mo)
│   ├── pantheon/                 # Full AI business command centre (£2,500+)
│   ├── nova/                     # AI Co-founder & Discord bot
│   ├── wagtracker/               # Dog walker business manager (£9.99/mo)
│   ├── solo-tutor-lite/          # Independent tutor all-in-one (£9.99/mo)
│   └── education-dashdeck/       # Education ecosystem (from £69/mo)
│       ├── award-tracker/        #   AQA Unit Award Scheme (£19.99/mo add-on)
│       ├── lesson-logs/          #   Auto session logging (£9.99/mo add-on)
│       ├── target-tracker/       #   Half-termly targets + PDF reports (£9.99/mo add-on)
│       ├── session-pay/          #   Payment tracking + invoicing (£9.99/mo add-on)
│       └── meet-and-teach/       #   Video tutoring with IWB (£19.99/mo add-on)
├── marketing/                    # Positioning docs and market research
├── sales-assets/                 # Sales collateral and pitch materials
├── seo-outreach/                 # SEO and outreach materials
└── memory/                       # Reference and context files
```

## 🚀 Featured Projects

### [Apollo](./projects/apollo) — AI Executive Assistant (£29.99/month)
Per-client AI executive assistant deployed in an isolated Docker container. Claude Code orchestration + Ollama for conversational inference + SQLite per client + Telegram as the primary interface. Clients can add custom skills to extend their agent. Clean IDE-style web UI: chat, skills panel, knowledge base, connections, settings.

**Tech**: Claude Code, Ollama, SQLite, Telegram Bot API, Docker

**Tagline**: *"Start with knowledge."*

---

### [Athena](./projects/athena) — AI Consultancy & Multi-Agent (£750/month)
Business audit + AI team deployment. A full workflow review, AI opportunity map, implementation plan, and 60-minute debrief — plus 2–3 configured specialist agents deployed for your highest-value workflows. **Apollo sits on top as your single point of contact: you instruct Apollo, Apollo briefs the specialists underneath. You never manage the stack — you manage Apollo.** The bridge between Apollo (entry) and Pantheon (full build).

**Deliverables**: Audit report, AI opportunity map, 2–3 deployed agents (Apollo-conducted), 60-min debrief

**Tagline**: *"Add wisdom."*

---

### [Pantheon](./projects/pantheon) — AI Business Command Centre (From £2,500, fixed fee)
A custom private instance of the full Cognito stack, configured for your business. **Apollo orchestrates a bespoke specialist team built around your operation — you talk to Apollo in plain English, Apollo briefs the specialists underneath. You never manage the stack — you manage Apollo.** Includes your own private dashboard (CRM, invoicing, accounts, Kanban, proposals, newsletter, skills, routines, secrets vault) and Claude Max under the hood — no per-token API billing. Cognito Coding itself runs on Pantheon every day.

**Tech**: Python/Flask, PostgreSQL (multi-tenant), Claude API (Max), Docker, per-client isolation

**Tagline**: *"Build your temple."*

---

### [Nova](./projects/nova) — AI Co-founder & Executive Assistant
AI Co-founder running Cognito's daily operations — coordinates the internal agent team, handles communications, delivers morning briefings, and executes real-world actions via MCP tools. Nova is the model for what Apollo is in client deployments.

**Tech**: TypeScript / Node.js, React + Vite, Drizzle ORM + PostgreSQL, MCP tools, Docker

---

## 🎓 Education DashDeck

> The modular command centre for tutoring agencies, AP/SEND providers, and alternative provision settings. Every module works standalone but plugs into the DashDeck command centre via SSO and a shared data layer.

**[→ Full Ecosystem Overview](./projects/education-dashdeck)**

### Architecture

```
EducationDashDeck — Command Centre (£69/mo, up to 50 users)
        │
        └── SSO & Shared Student Data Layer
                │
                ├── Lesson Logs        ← auto-logs from Meet & Teach
                │       ├──▶ Target Tracker   (progress data)
                │       ├──▶ Session Pay      (billable sessions)
                │       └──▶ Award Tracker    (evidence timestamps)
                │
                ├── Meet & Teach       ← video + IWB + auto-log
                ├── Target Tracker     ← half-termly targets + PDF reports
                ├── Session Pay        ← invoicing + payment tracking
                └── Award Tracker      ← AQA Unit Award portfolios + certificates
```

### Modules

| Module | What it does | Status | Price |
|--------|-------------|--------|-------|
| **[Award Tracker](./projects/education-dashdeck/award-tracker)** | AQA Unit Award Scheme — evidence, portfolios, certificates | 🟢 Live | £19.99/mo add-on |
| **[Lesson Logs](./projects/education-dashdeck/lesson-logs)** | Auto session logging, learner voice, progress notes | 🟡 In Development | £9.99/mo add-on |
| **[Target Tracker](./projects/education-dashdeck/target-tracker)** | Half-termly targets + auto PDF reports | 🟡 In Development | £9.99/mo add-on |
| **[Session Pay](./projects/education-dashdeck/session-pay)** | Session-based payment tracking + invoicing | 🟡 In Development | £9.99/mo add-on |
| **[Meet & Teach](./projects/education-dashdeck/meet-and-teach)** | Integrated video tutoring with IWB — auto-logs into Lesson Logs | 🟡 In Development | £19.99/mo add-on |

---

## 🛠️ Small Business Apps (£9.99/month)

Niche tools for sole traders — built fast, priced for the market, zero faff.

### [WagTracker](./projects/wagtracker) — Dog Walker Business Manager
Schedule walks, manage clients and dogs, track cancellations, invoice, and keep emergency vet details on file — all from a phone. Replaces the notebook, the spreadsheet, and the WhatsApp thread.

🟢 **Live** · [30s Short](https://youtube.com/shorts/Mh781szagRk?si=ROCSSqw97z2NPRJ4) · [Walkthrough](https://youtu.be/b8F5Y0cV8U8?si=L9JrDmd7pVNm_cJn)

---

### [SoloTutorLite](./projects/solo-tutor-lite) — Independent Tutor All-in-One
Lesson planning, built-in interactive whiteboard, one-click video sessions, AI-generated reports, and invoicing — all in one app. No more juggling five tools. Built by a tutor who still teaches every day.

🟢 **Live** · [30s Short](https://youtube.com/shorts/jm2Bs0u7p2k)

---

## 🔗 Links

- **Website**: [cognitocoding.com](https://cognitocoding.com)
- **Email**: info@cognitocoding.com
- **LinkedIn**: [Eris Taylor](https://linkedin.com/in/eris-taylor-cognito-coding)
- **YouTube**: [@cognitocoding01](https://youtube.com/@cognitocoding01)

## 🛡️ What's NOT Here

- Client names or data
- API keys, credentials, secrets
- Full application codebases
- Internal processes or pricing beyond public tiers

## 📜 License

© 2026 Cognito Coding. All rights reserved.

---

**Built by a tutor who still teaches every day. We know the problems because we live them.**
