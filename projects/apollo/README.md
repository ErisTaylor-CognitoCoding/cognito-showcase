# Apollo

> **AI Executive Assistant — per-client, private, trained on your business.**
>
> *"Start with knowledge."*

**Price**: £29.99/month (entry tier of the Cognito AI stack)

## Status

🟢 **[Live demo at apollo.cognitocoding.app](https://apollo.cognitocoding.app)** — the product is built and reachable. Click through and see Apollo in action. No paying clients yet — per-client Docker deployments happen at customer onboarding.

## Overview

Apollo is a personal AI executive assistant deployed per-client in an isolated Docker container. Unlike shared chatbot products, Apollo is **configured and trained on your business** — not a generic LLM bolted onto a template.

Clients interact with Apollo through **Telegram as the primary interface**, with a clean IDE-style web UI for managing skills, knowledge base, connections, and settings.

Apollo is the entry tier of Cognito's three-tier AI stack:

> **Apollo (£29.99/mo) → Moirai (£750) → Pantheon (£2,500+)**
>
> *"Start with knowledge. Add wisdom. Build your temple."*

## Architecture

```
┌──────────────────────────────────────────────────┐
│            Telegram Bot (Client)             │
│    DMs, voice notes, forwarded emails        │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│       Apollo Web UI (IDE-style)              │
│  Chat │ Skills │ Knowledge │ Connections │ ⚙️ │
└──────────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────────┐
│        Claude Code (Orchestration)           │
│  Tool routing, skill execution, reasoning    │
└──────────────────────────────────────────────────┘
                       │
       ┌───────────────┴───────────────┐
       ▼                               ▼
┌──────────────┐              ┌────────────────┐
│  Ollama LLM  │              │  SQLite (per   │
│ (conversat.) │              │  client DB)    │
└──────────────┘              └────────────────┘
```

**Per-client isolation**: each Apollo deployment gets its own Docker container, its own SQLite database, its own skill set, its own Telegram bot token. No shared state between clients.

## Tech Stack

- **Orchestration**: Claude Code (skill routing, reasoning, tool calls)
- **Conversational LLM**: Ollama (open-source models — Llama, Qwen, Mistral depending on use case)
- **Database**: SQLite (per-client, local to container)
- **Primary interface**: Telegram Bot API
- **Web UI**: Flask + HTMX (IDE-style — no framework bloat)
- **Deployment**: Docker Compose (containerised, per-client)

## Key Features

### 1. Email, Calendar, and Task Management
- Reads email through a connected Gmail/Outlook account
- Reads/writes calendar
- Maintains a task list scoped to the client's business

### 2. Research
- Browse the web, summarise articles, cross-reference sources
- Pull facts into the knowledge base for later retrieval

### 3. Knowledge Base
- Client-specific long-term memory (SOPs, contacts, brand voice, product catalogue)
- Embedded for semantic search
- Accessed by the LLM during reasoning

### 4. Custom Skills — the Killer Feature
Clients can **add custom skills** to their Apollo instance. A skill is a Markdown playbook the LLM loads on demand — e.g.
- "Draft a proposal using our pricing tiers"
- "Scan this receipt and log it to the ledger"
- "Generate a social post from this article in our brand voice"

Skills are plain Markdown. No code required. The client (or Cognito) writes them as they identify repetitive workflows.

### 5. Clean IDE-Style Web UI
Four panels, no bloat:
- **Chat** — conversation history with Apollo
- **Skills** — add / edit / disable skills
- **Knowledge Base** — view / edit stored facts and documents
- **Connections** — Gmail, calendar, Telegram, custom APIs
- **Settings** — model choice, persona tweaks, branding

## Design Learnings

> **Note:** Apollo is live at apollo.cognitocoding.app. These learnings come from building and running the product — not from paying client engagements, which are still to come.

### What Worked Well

**Telegram beat every other primary interface.** Users already have Telegram. Push notifications are free, instant, and work on desktop and mobile. Voice notes transcribe automatically. No new app to install.

**Claude Code + Ollama hybrid keeps costs down.** Claude Code handles the expensive reasoning and tool orchestration. Ollama handles the chatty back-and-forth. Result: per-client API spend stays low enough to make £29.99/mo a healthy margin.

**Per-client SQLite is the right choice for this tier.** No multi-tenant complexity, no query scoping bugs, no privacy worries. Each client literally has their own database file in their own container. If you want a backup, you copy the file.

**Custom skills turn Apollo into the client's own assistant.** Without the skill system, Apollo is a generic chatbot. With it, Apollo knows exactly how your business drafts proposals, scans receipts, and runs outreach.

### What We'd Do Differently

**Skill discovery is hard.** Users don't know what skills to add until they've lived with Apollo for a week. Every Apollo should ship with a starter pack of 10 common skills, plus suggestions based on observed patterns.

**Ollama model choice matters more than expected.** Qwen for fast chat, Llama for reasoning, Mistral for code. The right approach is to tune per-deployment rather than picking one model for everything.

**Voice note transcription needs a ceiling.** A long voice note from a user with a dictation habit will spend significant inference time. Capping at 5 minutes per note and summarising rather than transcribing verbatim is the right design.

---

*Part of the Cognito AI stack: [Apollo](./) → [Moirai](../moirai) → [Pantheon](../pantheon)*

*Built by [Cognito Coding](https://cognitocoding.com)*
