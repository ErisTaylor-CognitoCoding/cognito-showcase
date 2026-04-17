# Cognito Coding — Portfolio & Showcase

**Production code patterns, AI agent examples, and project showcases from Cognito Coding.**

This repository demonstrates the technical foundations behind Cognito's products — multi-tenant architecture, AI orchestration, OAuth flows, and Docker infrastructure.

## 🎯 What We Build

Cognito Coding builds AI-powered business automation and educational platforms:

- **Pantheon** — Custom AI-powered business command centres (CRM, agents, automation)
- **Apollo** — AI executive assistants deployed per-client in isolated Docker containers
- **DashDeck** — Education platform command centre (tutoring agencies, SEND providers)
- **Small Business Apps** — Niche tools for trades (dog walkers, tutors, etc.) at £9.99/month

## 📂 Repository Structure

```
cognito-showcase/
├── projects/           # Project showcases (sanitised)
│   ├── nova/          # AI Co-founder & Discord bot
│   ├── pantheon/      # Business command centre
│   └── award-tracker/ # AQA Unit Award SaaS
├── patterns/          # Production code patterns (coming soon)
├── prompts/           # AI agent persona examples (coming soon)
└── tutorials/         # How-to guides (coming soon)
```

## 🚀 Featured Projects

### [Nova](./projects/nova) — AI Co-founder & Executive Assistant
AI Discord bot with memory, agent delegation, and real-world execution power. Nova handles daily operations, coordinates specialist agents, and delivers morning briefings. Built on Claude API + PostgreSQL + MCP tools.

**Tech**: Python, discord.py, Claude API, PostgreSQL, MCP, Docker

---

### [Pantheon](./projects/pantheon) — AI-Powered Business Command Centre
Custom operating system for businesses — CRM, invoicing, accounts, Kanban, proposals, plus an AI agent team (Nova, CMO, CFO, Scout, CTO, Arthur). Deployed per-client with isolated infrastructure. Cognito itself runs on Pantheon.

**Tech**: Python/Flask, PostgreSQL (multi-tenant), Claude API, Paperclip (agent engine), Docker

---

### [Award Tracker](./projects/award-tracker) — AQA Unit Award SaaS
Multi-tenant web app for managing the AQA Unit Award Scheme (SEND/alternative provision). Evidence collection, portfolio generation, certificate printing. Live with paying clients at £24.99/month.

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
- Internal processes or pricing

## 📜 License

© 2026 Cognito Coding. All rights reserved.

---

**Built by a tutor who still teaches every day. We know the problems because we live them.**
