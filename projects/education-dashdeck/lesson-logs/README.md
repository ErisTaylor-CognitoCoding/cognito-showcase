# Lesson Logs

> Automatic session logging, learner voice capture, and progress notes — inside EducationDashDeck.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Price](https://img.shields.io/badge/price-%C2%A39.99%2Fmo-orange)
![Part of](https://img.shields.io/badge/part%20of-EducationDashDeck-blue)

## Overview

Lesson Logs replaces the end-of-session admin that eats into every teacher's evening. Sessions auto-log to each student's record. Learner voice is captured in-session. Progress notes are one tap, not a five-minute write-up.

Fully integrated with the EducationDashDeck SSO layer — student data flows automatically from your register into each log entry.

**Who it's for:** Tutoring agencies and AP/SEND providers who need consistent session records across multiple tutors without chasing paper logs.

## Features

- **Auto Session Logging** — Sessions start and end times are captured automatically. No manual entry.
- **Learner Voice** — In-session prompts capture the learner's own words. Meets Ofsted expectations for learner voice evidence.
- **Progress Notes** — Structured note templates per subject. Quick to fill, consistent across tutors.
- **Session History** — Full chronological session history per student, filterable by date, subject, and tutor.
- **DashDeck Integration** — Session data feeds directly into Target Tracker and Award Tracker. Write once, report everywhere.
- **Export** — Export session logs as PDF or CSV for compliance reporting.

## Pricing

**£9.99/month** as a DashDeck add-on (Basic tier).  
Included in EducationDashDeck Small (1 Basic module free in base price).

## Status

🟡 **In Development** — Available at [cognitocoding.com](https://cognitocoding.com)

## Part of Education DashDeck

Lesson Logs is one module in the [EducationDashDeck ecosystem](../).  
Sessions logged here automatically flow into **Target Tracker** (progress tracking) and **Session Pay** (invoicing) — no double-entry.

See the [full ecosystem overview](..) for pricing and architecture.

## Architecture Notes

```
EducationDashDeck SSO
        │
        ▼
  Lesson Logs module
        │
        ├──▶ Target Tracker (progress data)
        ├──▶ Session Pay (billable sessions)
        ├──▶ Award Tracker (evidence timestamps)
        └──▶ Meet & Teach (auto-log on session close)
```

Session records are shared across modules via the DashDeck data layer. A session logged here is immediately visible in billing, progress reports, and evidence portfolios — without copy-paste.

## Tech Stack

- Module-based architecture inside EducationDashDeck
- Shared SSO authentication layer
- PDF and CSV export (ReportLab)
- PostgreSQL multi-tenant data store
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](..) — built by [Cognito Coding](https://cognitocoding.com)*
