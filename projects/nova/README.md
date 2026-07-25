# Nova

> Cognito Coding's AI partner — Discord bot + embedded web widget, with memory, orchestration, and agent delegation

## Overview

Nova is Cognito Coding's AI partner — a Discord bot and website chat widget, powered by Claude, that acts as coding partner, content coordinator, and agent orchestrator. Nova owns the content pipeline (video docs, social posts, thumbnails, descriptions), handles the finance surfaces (Stripe reconciliation, monthly P&L), coordinates the other specialist agents, and delivers the daily briefing plus the weekly YouTube review and coding-challenge hunt.

Unlike typical chatbots, Nova has:
- **Long-term memory** via PostgreSQL conversation storage
- **Agent delegation** through the Pantheon agent runtime
- **Real execution power** with MCP tools for Gmail, Calendar, GitHub, Drive
- **Personality and context** — Nova is "he/him", part of the team, speaks in first person

Nova demonstrates how AI can be embedded into a business as a true operational partner, not just a Q&A tool. Nova is the model for what Apollo is in client deployments — the single point of contact that conducts the specialist team.

## Tech Stack

- **Language**: TypeScript / Node.js
- **Framework**: Express (rest-express) + discord.js
- **Web**: React + Vite standalone app; the chat panel embedded in Pantheon is vanilla JS
- **AI**: Anthropic Claude (Opus 5)
- **Database**: PostgreSQL via Drizzle ORM (conversation history, context, memory)
- **Orchestration**: Pantheon agent runtime (cron-scheduled agents, MCP tool execution)
- **Tools**: MCP (Model Context Protocol) for Gmail, Calendar, GitHub, Drive, YouTube
- **Deployment**: Docker container

## Architecture

```
Discord user / web widget
    ↓
Nova service (Node/TS — discord.js + Express)
    ↓
Claude (conversation + tools)
    ↓
┌────────────────────────────────┐
│ MCP Tools:                     │
│ - Gmail (read/send)            │
│ - Calendar (read events)       │
│ - GitHub (repos, files)        │
│ - Drive (upload/download)      │
│ - YouTube (upload videos)      │
│ - Pantheon (trigger agents)    │
└────────────────────────────────┘
    ↓
PostgreSQL (conversation history)
```

## Key Features

### 1. **Conversational Memory**
Every conversation stored in PostgreSQL with full context. Nova remembers past discussions, decisions, and preferences across sessions.

### 2. **Agent Delegation**
Nova works within a deliberately lean agent team, coordinating via the Pantheon agent runtime:
- **host-shell** — infrastructure / CTO: the Elysium host, Docker container health, the Pantheon and Nova codebases, database migrations, and security posture
- **git** — autonomous GitHub agent: repo maintenance across the product repos, README currency, and tag/release management

Content and finance were once separate agents; those roles were folded into Nova, who now owns all content work, the finance surfaces, and the weekly reviews himself.

### 3. **Tool Integration**
Real-world execution via MCP:
- Read and send emails (Gmail)
- Check calendar appointments
- Create GitHub repos and commit files
- Upload files to Google Drive
- Publish videos to YouTube
- Trigger Pantheon agent routines for complex workflows

### 4. **Morning Briefings**
Daily summary delivered to Discord:
- Calendar for the day
- Recent emails (inbox scan)
- Pending tasks from Grind Tracker
- Agent status (any errors or warnings)

### 5. **Content Review**
Nova reviews content drafts and acts as the brand-voice gate before anything ships to the channel.

## Lessons Learned

### What Worked Well

**Personality matters**: Giving Nova a consistent voice, pronouns (he/him), and partner status made interactions feel collaborative rather than transactional. Zero talks to Nova like a partner, not a tool.

**Memory is critical**: Storing full conversation history in PostgreSQL means Nova can reference past decisions. "Remember when we talked about X?" works — this is a game-changer for long-term projects.

**MCP is the right abstraction**: Model Context Protocol cleanly separates "AI reasoning" from "real-world actions". Nova calls tools, tools execute, results feed back into context. No fragile function chaining.

**A lean team beats a big org chart**: Nova doesn't need a roster of narrow agents — he owns content and finance directly and leans on host-shell for infrastructure and git for repo work. Fewer agents, less prompt bloat, clearer ownership.

### What We'd Do Differently

**Conversation pruning**: Early versions stored *everything* forever, causing context bloat. Now we prune old messages and summarise long threads. Still learning the right balance.

**Tool error handling**: When an MCP tool fails (e.g. Gmail API rate limit), Nova needs better retry logic and user-facing error messages. Currently too raw.

**Multi-channel support**: Nova runs in Discord and the website widget. Apollo (the client-facing equivalent) extends this to Slack and Telegram using the same conductor model — one interface, specialist team underneath.

---

*Built by [Cognito Coding](https://cognitocoding.com)*
