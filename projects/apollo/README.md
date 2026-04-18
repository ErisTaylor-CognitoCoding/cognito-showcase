# Apollo

> **AI Executive Assistant — per-client, private, trained on your business.**
>
> *"Start with knowledge."*

**Price**: £29.99/month (entry tier of the Cognito AI stack)

## Overview

Apollo is a personal AI executive assistant deployed per-client in an isolated Docker container. Unlike shared chatbot products, Apollo is **configured and trained on your business** — not a generic LLM bolted onto a template.

Clients interact with Apollo through **Telegram as the primary interface**, with a clean IDE-style web UI for managing skills, knowledge base, connections, and settings.

Apollo is the entry tier of Cognito's three-tier AI stack:

> **Apollo (£29.99/mo) → Athena (£750) → Pantheon (£2,500+)**
>
> *"Start with knowledge. Add wisdom. Build your temple."*

## Architecture

```
┌──────────────────────────────────────────────┐
│            Telegram Bot (Client)             │
│    DMs, voice notes, forwarded emails        │
└──────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────┐
│       Apollo Web UI (IDE-style)              │
│  Chat │ Skills │ Knowledge │ Connections │ ⚙️ │
└──────────────────────────────────────────────┘
                       │
┌──────────────────────────────────────────────┐
│        Claude Code (Orchestration)           │
│  Tool routing, skill execution, reasoning    │
└──────────────────────────────────────────────┘
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

## Lessons Learned

### What Worked Well

**Telegram beat every other primary interface.** Clients already have Telegram. Push notifications are free, instant, and work on desktop and mobile. Voice notes transcribe automatically. No new app to install.

**Claude Code + Ollama hybrid keeps costs down.** Claude Code handles the expensive reasoning and tool orchestration. Ollama handles the chatty back-and-forth. Result: per-client API spend stays low enough to make £29.99/mo a healthy margin.

**Per-client SQLite is the right choice for this tier.** No multi-tenant complexity, no query scoping bugs, no privacy worries. Each client literally has their own database file in their own container. If you want a backup, you copy the file.

**Custom skills turn Apollo into the client's own assistant.** Without the skill system, Apollo is a generic chatbot. With it, Apollo knows exactly how your business drafts proposals, scans receipts, and runs outreach.

### What We'd Do Differently

**Skill discovery is hard.** Clients don't know what skills to add until they've lived with Apollo for a week. We now ship every Apollo with a starter pack of 10 common skills and suggest new ones based on observed patterns.

**Ollama model choice matters more than we expected.** Qwen for fast chat, Llama for reasoning, Mistral for code. We had to tune per-deployment instead of picking one.

**Voice note transcription needed a ceiling.** A 20-minute voice note from a client with dictation as a habit will happily spend an hour of inference time. We cap at 5 minutes per note now, and summarise rather than transcribe verbatim.

---

*Part of the Cognito AI stack: [Apollo](./) → [Athena](../athena) → [Pantheon](../pantheon)*

*Built by [Cognito Coding](https://cognitocoding.com)*
