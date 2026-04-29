# Nova

> AI Co-founder and Executive Assistant — Discord bot with memory, orchestration, and agent delegation

## Overview

Nova is Cognito Coding's AI Co-founder — a Discord bot powered by Claude API that acts as an executive assistant, content coordinator, and agent orchestrator. Nova handles daily operations, manages outreach campaigns, coordinates other specialist agents, and delivers morning briefings.

Unlike typical chatbots, Nova has:
- **Long-term memory** via PostgreSQL conversation storage
- **Agent delegation** through the Pantheon agent runtime
- **Real execution power** with MCP tools for Gmail, Calendar, GitHub, Drive
- **Personality and context** — Nova is "he/him", part of the founding team, speaks in first person

Nova demonstrates how AI can be embedded into a business as a true operational partner, not just a Q&A tool. Nova is the model for what Apollo is in client deployments — the single point of contact that conducts the specialist team.

## Tech Stack

- **Language**: Python 3.11
- **Framework**: discord.py + Flask
- **AI**: Anthropic Claude API (Sonnet 4)
- **Database**: PostgreSQL (conversation history, context, memory)
- **Orchestration**: Pantheon agent runtime (cron-scheduled agents, MCP tool execution)
- **Tools**: MCP (Model Context Protocol) for Gmail, Calendar, GitHub, Drive, YouTube
- **Deployment**: Docker container

## Architecture

```
Discord User
    ↓
Nova Bot (discord.py)
    ↓
Claude API (conversation + tools)
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
Nova coordinates specialist agents via the Pantheon agent runtime:
- **CMO** — Marketing, content creation, video production
- **CFO** — Finance, expense scanning, Stripe sync
- **Scout** — Job hunting, proposal drafting
- **CTO** — Technical execution, infrastructure
- **Arthur** — Code-level shell execution

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

### 5. **Proposal & Content Review**
Nova reviews drafts from other agents before sending to clients. Acts as quality gate and brand voice enforcer.

## Lessons Learned

### What Worked Well

**Personality matters**: Giving Nova a consistent voice, pronouns (he/him), and "co-founder" status made interactions feel collaborative rather than transactional. Zero talks to Nova like a business partner, not a tool.

**Memory is critical**: Storing full conversation history in PostgreSQL means Nova can reference past decisions. "Remember when we talked about X?" works — this is a game-changer for long-term projects.

**MCP is the right abstraction**: Model Context Protocol cleanly separates "AI reasoning" from "real-world actions". Nova calls tools, tools execute, results feed back into context. No fragile function chaining.

**Agent delegation scales**: Nova doesn't do everything himself — he delegates to specialist agents (CMO for content, Scout for proposals). This mirrors real team structures and prevents prompt bloat.

### What We'd Do Differently

**Conversation pruning**: Early versions stored *everything* forever, causing context bloat. Now we prune old messages and summarise long threads. Still learning the right balance.

**Tool error handling**: When an MCP tool fails (e.g. Gmail API rate limit), Nova needs better retry logic and user-facing error messages. Currently too raw.

**Multi-channel support**: Nova runs in Discord. Apollo (the client-facing equivalent) extends this to Slack and Telegram using the same conductor model — one interface, specialist team underneath.

---

*Built by [Cognito Coding](https://cognitocoding.com)*
