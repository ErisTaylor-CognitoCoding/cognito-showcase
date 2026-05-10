# Education DashDeck

> The modular command centre for tutoring agencies, AP/SEND providers, and alternative provision settings.

![Status](https://img.shields.io/badge/status-live-brightgreen)
![Price](https://img.shields.io/badge/price-from%20%C2%A369%2Fmo-orange)

## Overview

EducationDashDeck is an end-to-end, teacher-led modular ecosystem that reduces teacher workload. Every module works standalone but plugs into the DashDeck command centre via SSO and a shared data layer — so learner progress, session history, payments, and award evidence are always in sync across your whole team.

Built by a tutor and Deputy Headteacher who lived the admin problem for 25 years.

**Who it's for:**

- **Tutoring agencies (15–200 tutors)** — reduce admin, track progress across tutors, handle invoicing centrally, stay compliant
- **AP / SEND providers** — manage AQA Unit Award evidence, half-termly progress reports, EHCP tracking, and session records
- **Solo tutors** — see [SoloTutorLite](../solo-tutor-lite) — a standalone solution built for one-person operations

## The Modules

Each module solves a real problem and plugs into the DashDeck command centre via SSO. Add only what you need. Remove what you don't.

| Module | What it does | Tier | Price |
|--------|-------------|------|-------|
| **[Award Tracker](./award-tracker)** | AQA Unit Award Scheme — evidence, portfolios, certificates | Premium | £19.99/mo add-on |
| **[Lesson Logs](./lesson-logs)** | Auto session logging, learner voice, progress notes | Basic | £9.99/mo add-on |
| **[Target Tracker](./target-tracker)** | Half-termly targets + auto PDF reports | Basic | £9.99/mo add-on |
| **[Session Pay](./session-pay)** | Session-based payment tracking + invoicing | Basic | £9.99/mo add-on |
| **[Meet & Teach](./meet-and-teach)** | Integrated video tutoring with IWB — auto-logs into Lesson Logs | Premium | £19.99/mo add-on |

## Pricing

| Plan | Price | Includes |
|------|-------|---------|
| EducationDashDeck Small | **£69/month** | Up to 50 users + 1 Basic module |
| Extra Basic module | **£9.99/month** | Lesson Logs, Target Tracker, or Session Pay |
| Extra Premium module | **£19.99/month** | Award Tracker or Meet & Teach |

No setup fee. No lock-in. Add modules as your provision grows.

## How the Data Flows

The power of DashDeck is the shared data layer. Modules don't exist in silos — session data, progress records, evidence, and billing all speak to each other.

```
EducationDashDeck — Command Centre
        │
        └── SSO & Shared Student Data Layer
                │
                ├── Lesson Logs        ← auto-logs from Meet & Teach
                │       │
                │       ├──▶ Target Tracker   (progress data)
                │       ├──▶ Session Pay      (billable sessions)
                │       └──▶ Award Tracker    (evidence timestamps)
                │
                ├── Meet & Teach       ← video + IWB + auto-log
                ├── Target Tracker     ← half-termly targets + PDF reports
                ├── Session Pay        ← invoicing + payment tracking
                └── Award Tracker      ← AQA Unit Award portfolios + certificates
```

A session taught in **Meet & Teach** auto-creates a record in **Lesson Logs**, which automatically feeds **Target Tracker** (progress), **Session Pay** (billing), and **Award Tracker** (evidence). One session — four systems updated.

## Architecture

Single-instance SaaS with multi-tenant data isolation per client organisation. Row-level PostgreSQL security ensures no cross-tenant data access. The SSO layer means a teacher logs in once and sees all their modules in one dashboard.

Key patterns:
- **Shared data layer** — student records, session data, and progress data are shared across modules via a common schema, not duplicated per module
- **Event-based integration** — a session close event triggers downstream updates (Lesson Logs, then Target Tracker, Session Pay, Award Tracker) via internal event handlers, not API calls between modules
- **Multi-tenant isolation** — each client organisation is a tenant. Evidence files stored in isolated, encrypted per-client buckets
- **Role-based access** — admin / teacher / viewer roles per tenant. Tutor can see their own students only; admin sees all

## Status

🟢 **Award Tracker live** with paying clients.  
🟡 Remaining modules in active development.

## Links

- 🌐 [cognitocoding.com](https://cognitocoding.com)
- 📧 [info@cognitocoding.com](mailto:info@cognitocoding.com)

---

*Built by [Cognito Coding](https://cognitocoding.com) — practitioners who built this because we needed it ourselves.*
