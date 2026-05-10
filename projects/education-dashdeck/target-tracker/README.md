# Target Tracker

> Half-termly targets and auto-generated PDF progress reports — inside EducationDashDeck.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Price](https://img.shields.io/badge/price-%C2%A39.99%2Fmo-orange)
![Part of](https://img.shields.io/badge/part%20of-EducationDashDeck-blue)

## Overview

Target Tracker removes the half-term reporting crunch. Set targets once per student. Progress is tracked automatically as session data flows in from Lesson Logs. When reports are due, generate professional PDFs in one click — no copy-pasting from spreadsheets, no chasing tutors for notes.

**Who it's for:** Tutoring agencies and AP/SEND providers who report progress to parents, commissioners, or local authorities each half-term and need a consistent, auditable paper trail across all their tutors.

## Features

- **Half-Termly Targets** — Set SMART targets per student per subject. Track against them across the term.
- **Auto PDF Reports** — Professional progress reports pre-populated from session data. One click per student.
- **Progress RAG** — Red/Amber/Green status per target, updated automatically as Lesson Log data arrives.
- **Tutor Notes** — Free-text commentary per target for the report narrative. Visible to the student's assigned tutor only.
- **Agency Dashboard** — All students, all targets, all RAG statuses at a glance. Spot who's behind before it becomes a problem.
- **DashDeck Integration** — Pulls session data from Lesson Logs automatically. Pushes summaries into Award Tracker evidence records.
- **Export** — Reports as PDF. Data export as CSV for commissioners or LA returns.

## Pricing

**£9.99/month** as a DashDeck add-on (Basic tier).  
Included in EducationDashDeck Small (1 Basic module free in base price).

## Status

🟡 **In Development** — Available at [cognitocoding.com](https://cognitocoding.com)

## Part of Education DashDeck

Target Tracker is one module in the [EducationDashDeck ecosystem](../).  
It reads from **Lesson Logs** and writes summaries into **Award Tracker** — the reporting layer that ties the ecosystem together.

See the [full ecosystem overview](..) for pricing and architecture.

## Architecture Notes

```
Lesson Logs (session data)
        │
        ▼
  Target Tracker
        │
        ├── Target: Y9 Functional Skills Maths ──▶ RAG: Amber
        ├── Target: Communication Level 1     ──▶ RAG: Green
        └── Target: Independent Living Skills ──▶ RAG: Red
        │
        ▼
  PDF Report (one click)
  Award Tracker evidence summary (auto-push)
```

Progress reports are generated server-side from live data — no spreadsheet intermediary.

## Tech Stack

- Module-based architecture inside EducationDashDeck
- PDF report generation (ReportLab)
- Shared data layer with Lesson Logs and Award Tracker
- PostgreSQL multi-tenant data store
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](..) — built by [Cognito Coding](https://cognitocoding.com)*
