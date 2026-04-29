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

- **Small Business Apps** — Niche tools for trades (dog walkers, tutors, etc.) at £9.99/month
- **Education Platform** — DashDeck and add-ons for tutoring agencies and SEND providers

## 📂 Repository Structure

```
cognito-showcase/
├── projects/              # Project showcases (sanitised)
│   ├── apollo/           # AI executive assistant (£29.99/mo)
│   ├── athena/           # AI audit + multi-agent consultancy (£750/mo)
│   ├── pantheon/         # Full AI business command centre (£2,500+)
│   ├── nova/             # AI Co-founder & Discord bot
│   └── award-tracker/    # AQA Unit Award SaaS
├── patterns/             # Production code patterns (coming soon)
├── prompts/              # AI agent persona examples (coming soon)
└── tutorials/            # How-to guides (coming soon)
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
AI Discord bot with memory, agent delegation, and real-world execution power. Nova handles daily operations, coordinates specialist agents, and delivers morning briefings. Built on Claude API + PostgreSQL + MCP tools. Nova is the model for what Apollo is in client deployments.

**Tech**: Python, discord.py, Claude API, PostgreSQL, MCP, Docker

---

### [Award Tracker](./projects/award-tracker) — AQA Unit Award SaaS
Multi-tenant web app for managing the AQA Unit Award Scheme (SEND/alternative provision). Evidence collection, portfolio generation, certificate printing. Live with paying clients at £19.99/month.

**Tech**: Python/Flask, PostgreSQL (multi-tenant), ReportLab (PDF), DashDeck SSO, Docker

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
