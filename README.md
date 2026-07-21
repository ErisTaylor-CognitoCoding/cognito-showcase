# Cognito Coding — Showcase

> **Learn To Code By Building Real Things.**  
> No fluff. No theory dumps. Just real builds.

I'm a coder and a teacher. For a while those two pulled in different directions — proposals, clients, chasing the agency — and the bit I actually love got buried.

So Cognito Coding pivoted. It's now about sharing what I know: my solutions, my methodology, the why behind the code.

**[YouTube Channel →](https://www.youtube.com/@CognitoCoding01)** · **[Website →](https://cognitocoding.com)**

---

## 🎮 I Taught an AI to Farm — The Farmer Was Replaced Series

Playing through [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) — a game where you write real Python to automate a drone farmer. Every Wednesday on the channel.

### [/series](./series) — Long-form Episode Code

One folder per episode. Each contains the **end-state Python code** from that episode plus a plain README explaining what was covered and why.

| Episode | Topic | Video |
|---------|-------|-------|
| [ep-01-first-program](./series/ep-01-first-program) | `harvest()`, `while True`, `if can_harvest()`, `move(North)` | [▶ Watch](https://youtu.be/maTaBrkHh1o) |
| [ep-02-operators](./series/ep-02-operators) | Comparison operators, position sensing, full 3×3 | [▶ Watch](https://youtu.be/qB2nKoU1dkI) |
| [ep-03-functions](./series/ep-03-functions) | `def`, parameters, DRY principle | [▶ Watch](https://youtu.be/FMUXw4UKyLI) |
| [ep-04-pumpkins](./series/ep-04-pumpkins) | Variables, `if/elif`, reading tile state | [▶ Watch](https://youtu.be/X92lWWj8HbY) |
| [ep-05-sunflowers](./series/ep-05-sunflowers) | Running maximum, `measure()`, double sweep | [▶ Watch](https://youtu.be/rchPKYdB3AE) |
| [ep-06-cactus](./series/ep-06-cactus) | Patience — `while not ready`, only act when growth is complete | [▶ Watch](https://youtu.be/iuiQK3me25M) |
| [ep-07-fertilizers](./series/ep-07-fertilizers) | Resource management — combining items to boost crop yields | [▶ Watch](https://youtu.be/fI1fF9-VIo8) |

### [/concepts-a-z](./concepts-a-z) — Saturday Shorts Library

One folder per concept. 30-second bite-sized videos with a working code snippet and a plain explanation. Same game, same concepts — zoomed in.

| Concept | What it teaches |
|---------|----------------|
| [harvest](./concepts-a-z/harvest) | `while True` — your first infinite loop |
| [if-check](./concepts-a-z/if-check) | `if` statements — guard before you act |
| [grass-strip](./concepts-a-z/grass-strip) | `for` loops — cover a full row |
| [snake-pattern](./concepts-a-z/snake-pattern) | Nested loops — cover every tile |
| [pumpkins](./concepts-a-z/pumpkins) | Reading entity state before planting |
| [sunflowers](./concepts-a-z/sunflowers) | Running maximum with a variable |
| [dead-crops](./concepts-a-z/dead-crops) | Clearing failure states before replanting |
| [trees](./concepts-a-z/trees) | `if/elif` — multi-resource harvest |
| [cactus](./concepts-a-z/cactus) | Patience — only act when growth is complete |
| [trade](./concepts-a-z/trade) | Arithmetic — converting harvest into gold |
| [upgrade](./concepts-a-z/upgrade) | Conditional buying — check balance first |
| [full-farm](./concepts-a-z/full-farm) | Combining everything into one automated farm |

*New episode every Wednesday. New Short every Saturday. [Subscribe →](https://www.youtube.com/@CognitoCoding01)*

---

## 📖 Learn to Code

### [Cognito Coding A–Z](https://github.com/ErisTaylor-CognitoCoding/cognito-coding-a-z)

Companion repo to the **One Concept, One Board** YouTube Shorts series. Every coding concept gets its own folder — an analogy, a classroom explanation, and a working Python example you can run right now. No experience needed. Start at the top, work down.

→ [Browse the repo](https://github.com/ErisTaylor-CognitoCoding/cognito-coding-a-z)

---

## 🗂️ Repository Structure

```
cognito-showcase/
├── series/            # I Taught an AI to Farm — episode end-state code
│   ├── ep-01-first-program/
│   ├── ep-02-operators/
│   ├── ep-03-functions/
│   ├── ep-04-pumpkins/
│   ├── ep-05-sunflowers/
│   ├── ep-06-cactus/
│   └── ep-07-fertilizers/
├── concepts-a-z/      # Sat Farmer Shorts — one concept, one snippet
│   ├── harvest/
│   ├── if-check/
│   ├── grass-strip/
│   └── ... (12 concepts total)
└── projects/          # App showcases (sanitised)
    ├── apollo/
    ├── moirai/
    ├── pantheon/
    ├── nova/
    ├── wagtracker/
    ├── solo-tutor-lite/
    └── education-dashdeck/
```

---

## 🚀 What I've Built

### [Apollo](./projects/apollo) — AI Executive Assistant
Per-client AI assistant deployed in an isolated Docker container. Claude Code orchestration + Ollama + SQLite + Telegram as the primary interface.

**Tech**: Claude Code, Ollama, SQLite, Telegram Bot API, Docker  
🟢 **Live demo**: [apollo.cognitocoding.app](https://apollo.cognitocoding.app)

---

### [Moirai](./projects/moirai) — Apollo-Conducted Multi-Agent Team
A coordinated agent team under one conductor. Apollo sits on top as the single point of contact — you instruct Apollo, Apollo briefs the specialists. You never manage the stack.

🟢 **Live demo**: [athena.cognitocoding.app](https://athena.cognitocoding.app)

---

### [Pantheon](./projects/pantheon) — AI Business Command Centre
A full private dashboard — CRM, invoicing, Kanban, agent orchestration, secrets vault, and more. Cognito Coding itself runs on Pantheon every day.

**Tech**: Python/Flask, PostgreSQL, Claude API, Docker  
🟢 **Live demo**: [pantheon.cognitocoding.app](https://pantheon.cognitocoding.app)

---

### [Nova](./projects/nova) — Cognito's AI Partner
Runs Cognito's daily operations — coordinates the internal agent team, handles communications, and executes real-world actions via MCP tools. Nova is the model for what Apollo is in client deployments.

**Tech**: TypeScript / Node.js, React + Vite, Drizzle ORM + PostgreSQL, MCP tools, Docker

---

### [WagTracker](./projects/wagtracker) — Dog Walker Business Manager
Schedule walks, manage clients and dogs, track cancellations, invoice — all from a phone. Replaces the notebook, the spreadsheet, and the WhatsApp thread.

🟢 **Live** · [30s Short](https://youtube.com/shorts/Mh781szagRk?si=ROCSSqw97z2NPRJ4) · [Walkthrough](https://youtu.be/b8F5Y0cV8U8?si=L9JrDmd7pVNm_cJn)

---

### [SoloTutorLite](./projects/solo-tutor-lite) — Independent Tutor All-in-One
Lesson planning, interactive whiteboard, one-click video sessions, AI-generated reports, and invoicing — all in one app. No more juggling five tools. Built by a tutor who still teaches every day.

🟢 **Live** · [30s Short](https://youtube.com/shorts/jm2Bs0u7p2k)

---

### EducationDashDeck — Modular Education Platform

Ecosystem for tutoring agencies and SEND providers. Six modules: Award Tracker, Revision Bites, Lesson Logs, Target Tracker, Session Pay, Meet & Teach. Paused — built, not in active development.

**[→ Full Ecosystem Overview](./projects/education-dashdeck)**

---

## 🛡️ What's NOT Here

- Client names or data
- API keys, credentials, secrets
- Full application codebases
- Internal processes

---

## 🔗 Links

- **Website**: [cognitocoding.com](https://cognitocoding.com)
- **YouTube**: [@CognitoCoding01](https://youtube.com/@CognitoCoding01)
- **Email**: info@cognitocoding.com
- **LinkedIn**: [Eris Taylor](https://linkedin.com/in/eris-taylor-cognito-coding)

---

**Built by a tutor who still teaches every day.**

© 2026 Cognito Coding
