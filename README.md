# Cognito Coding — Portfolio & Showcase

**Production code patterns, AI agent examples, and project showcases from Cognito Coding.**

This repository demonstrates the technical foundations behind Cognito's products — multi-tenant architecture, AI orchestration, OAuth flows, and Docker infrastructure.

## 🎯 What We Build

Cognito Coding builds AI-powered business automation and educational platforms. Our AI tier is structured in three levels:

> **Start with knowledge. Add wisdom. Build your temple.**

| Tier | Product | Price |
|------|---------|-------|
| 🟠 Entry | **[Apollo](./projects/apollo)** — Per-client AI executive assistant | Build from £99 · Hosting £29/mo · [🟢 Live demo](https://apollo.cognitocoding.app) |
| 🟡 Mid | **[Moirai](./projects/moirai)** — Apollo-conducted multi-agent team | Build from £249 · Hosting £750/mo · [🟢 Live demo](https://athena.cognitocoding.app) |
| 🔵 Flagship | **[Pantheon](./projects/pantheon)** — Full custom AI business command centre | Build from £599 · Hosting £2,500+/mo · [🟢 Live demo](https://pantheon.cognitocoding.app) |

Plus:

- **Small Business Apps** — Niche tools for trades and professionals at £9.99/month ([WagTracker](./projects/wagtracker), [SoloTutorLite](./projects/solo-tutor-lite), and more)
- **Education Platform** — [EducationDashDeck](./projects/education-dashdeck) — modular ecosystem for tutoring agencies and SEND providers
- **Gaming Tools** — Browser-based utilities for gamers ([Sonaria Clip Saver](./projects/sonaria-clip-saver))

## 📂 Repository Structure

```
cognito-showcase/
├── projects/                     # Project showcases (sanitised)
│   ├── apollo/                   # AI executive assistant
│   ├── moirai/                   # Apollo-conducted multi-agent team
│   ├── pantheon/                 # Full AI business command centre
│   ├── nova/                     # AI Co-founder & Discord bot
│   ├── wagtracker/               # Dog walker business manager (£9.99/mo)
│   ├── solo-tutor-lite/          # Independent tutor all-in-one (£9.99/mo)
│   ├── sonaria-clip-saver/       # Background game clip recorder (browser)
│   └── education-dashdeck/       # Education ecosystem
│       ├── award-tracker/        #   AQA Unit Award Scheme
│       ├── revision-bites/       #   Personalised revision schedules
│       ├── lesson-logs/          #   Auto session logging
│       ├── target-tracker/       #   Half-termly targets + PDF reports
│       ├── session-pay/          #   Payment tracking + invoicing
│       └── meet-and-teach/       #   Video tutoring with IWB
├── marketing/                    # Positioning docs and market research
├── sales-assets/                 # Sales collateral and pitch materials
├── seo-outreach/                 # SEO and outreach materials
└── memory/                       # Reference and context files
```

## 🚀 Featured Projects

### [Apollo](./projects/apollo) — AI Executive Assistant
Per-client AI executive assistant deployed in an isolated Docker container. Claude Code orchestration + Ollama for conversational inference + SQLite per client + Telegram as the primary interface. Clients can add custom skills to extend their agent. Clean IDE-style web UI: chat, skills panel, knowledge base, connections, settings.

**Status**: 🟢 [Live demo](https://apollo.cognitocoding.app) — built and reachable. No paying clients yet.

**Tech**: Claude Code, Ollama, SQLite, Telegram Bot API, Docker

**Pricing**: Build from £99 (one-off, client owns the container) · Hosting £29/month fixed

**Tagline**: *"Start with knowledge."*

---

### [Moirai](./projects/moirai) — Apollo-Conducted Multi-Agent Team
Bespoke fixed-fee build + a coordinated agent team under one conductor. A full workflow review, AI opportunity map, implementation plan, and 2–3 configured specialist agents deployed for your highest-value workflows. **Apollo sits on top as your single point of contact: you instruct Apollo, Apollo briefs the specialists underneath. You never manage the stack — you manage Apollo.** The bridge between Apollo (entry) and Pantheon (full build).

**Status**: 🟢 [Live demo](https://athena.cognitocoding.app) — Social Media vertical live, seeded with PeakForm demo. No paying clients yet.

**Deliverables**: Audit report, AI opportunity map, 2–3 deployed agents (Apollo-conducted), 60-min debrief

**Pricing**: Build from £249 (one-off, client owns the container) · Hosting £750/month fixed

**Tagline**: *"Add wisdom."*

---

### [Pantheon](./projects/pantheon) — AI Business Command Centre
A custom private instance of the full Cognito stack, configured for your business. **Apollo orchestrates a bespoke specialist team built around your operation — you talk to Apollo in plain English, Apollo briefs the specialists underneath. You never manage the stack — you manage Apollo.** Includes your own private dashboard (CRM, invoicing, accounts, Kanban, proposals, newsletter, skills, routines, secrets vault) and Claude Max under the hood — no per-token API billing. Cognito Coding itself runs on Pantheon every day.

**Status**: 🟢 [Live demo](https://pantheon.cognitocoding.app) — multi-vertical build, running at Cognito HQ daily. No external paying clients yet.

**Tech**: Python/Flask, PostgreSQL (multi-tenant), Claude API (Max), Docker, per-client isolation

**Pricing**: Build from £599 (one-off, client owns the container + code) · Hosting £2,500+/month fixed

**Tagline**: *"Build your temple."*

---

### [Nova](./projects/nova) — AI Co-founder & Executive Assistant
AI Co-founder running Cognito's daily operations — coordinates the internal agent team, handles communications, delivers morning briefings, and executes real-world actions via MCP tools. Nova is the model for what Apollo is in client deployments.

**Tech**: TypeScript / Node.js, React + Vite, Drizzle ORM + PostgreSQL, MCP tools, Docker

---

## 🎓 EducationDashDeck

> The modular command centre for tutoring agencies, AP/SEND providers, and alternative provision settings. Every module works standalone but plugs into the EducationDashDeck command centre via SSO and a shared data layer.

**[→ Full Ecosystem Overview](./projects/education-dashdeck)**

### Architecture

```
EducationDashDeck — Command Centre
        │
        └── SSO & Shared Student Data Layer
                │
                ├── Lesson Logs        ← auto-logs from Meet & Teach
                │       ├──▶ Target Tracker   (progress data)
                │       ├──▶ Session Pay      (billable sessions)
                │       └──▶ Award Tracker    (evidence timestamps)
                │
                ├── Meet & Teach       ← video + IWB + scientific calculator + auto-log
                ├── Target Tracker     ← half-termly targets + PDF reports
                ├── Session Pay        ← invoicing + payment tracking
                ├── Award Tracker      ← AQA Unit Award portfolios + certificates
                └── Revision Bites     ← personalised weekly revision schedules
```

### Modules

| Module | What it does | Status | Price |
|--------|-------------|--------|-------|
| **[Award Tracker](./projects/education-dashdeck/award-tracker)** | AQA Unit Award Scheme — evidence, portfolios, certificates | 🟢 Live | TBC |
| **[Revision Bites](./projects/education-dashdeck/revision-bites)** | Personalised weekly revision schedules, curriculum-aligned topics | 🟡 In Development | TBC |
| **[Lesson Logs](./projects/education-dashdeck/lesson-logs)** | Auto session logging, learner voice, progress notes | 🟡 In Development | TBC |
| **[Target Tracker](./projects/education-dashdeck/target-tracker)** | Half-termly targets + auto PDF reports | 🟡 In Development | TBC |
| **[Session Pay](./projects/education-dashdeck/session-pay)** | Session-based payment tracking + invoicing | 🟡 In Development | TBC |
| **[Meet & Teach](./projects/education-dashdeck/meet-and-teach)** | Integrated video tutoring with IWB — auto-logs into Lesson Logs | 🟡 In Development | TBC |

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

## 🎮 Gaming Tools

Browser-based utilities for gamers — no install, no accounts, no backend.

### [Sonaria Clip Saver](./projects/sonaria-clip-saver) — Auto Clip Recorder for Creatures of Sonaria
A background screen recorder that automatically saves the last ~30 seconds of gameplay whenever a **KILL CONFIRMED** banner appears on screen. Built for Sonaria mains who are tired of missing highlight clips.

No reflexes required. Open the app in Chrome/Edge, share your game window, press F10 on a real banner to calibrate, and play. Clips save automatically to disk as `.webm` with a trigger-frame `.jpg` alongside each one.

**Tech**: React + Vite + TypeScript, `getDisplayMedia`, `MediaRecorder`, `OffscreenCanvas`, File System Access API — runs entirely in the browser. No telemetry, no accounts, clips stay on your machine.

🔵 **Built** · [→ Full Details](./projects/sonaria-clip-saver)

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
