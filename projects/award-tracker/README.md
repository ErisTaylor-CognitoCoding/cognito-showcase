# Award Tracker

> AQA Unit Award Scheme progress tracking, evidence portfolios, and certificate printing.

![Status](https://img.shields.io/badge/status-live-brightgreen)
![Price](https://img.shields.io/badge/price-%C2%A319.99%2Fmo-orange)
![Ecosystem](https://img.shields.io/badge/ecosystem-EducationDashDeck-blue)

## Overview

Award Tracker digitalises the AQA Unit Award Scheme for SEND schools, alternative provision settings, and tutoring agencies. Evidence collection, portfolio generation, and certificate printing in one app — with no paper trail, no lost folders, and a clean digital record that passes an Ofsted inspection.

Live with paying clients.

**Who it's for:** AP and SEND providers running the AQA Unit Award Scheme who spend hours managing paper evidence folders, chasing staff for certificate paperwork, and manually assembling student portfolios.

## Features

- **Unit Award Management** — Browse and select AQA units from the full catalogue. Assign units to individual learners or whole cohorts.
- **Evidence Collection** — Upload photos, videos, and documents as evidence per unit. Timestamped and securely stored per student.
- **Progress Tracking** — Dashboard view of each student's unit completions across all enrolled units. RAG status at a glance.
- **Portfolio Generation** — Auto-generate a printable student portfolio (PDF) showing all completed units and evidence references. Ready for review meetings.
- **Certificate Printing** — AQA-formatted completion certificates per unit. No manual template work.
- **Multi-User Access** — Staff roles: admin, teacher, viewer. Assign learners to specific staff members.
- **DashDeck Integration** — Evidence timestamps sync with Lesson Logs session records. Progress summaries feed into Target Tracker reports.

## Pricing

**£19.99/month** as a DashDeck add-on (Premium tier).

## Status

🟢 **Live** — in production with paying clients.

## Part of Education DashDeck

Award Tracker is a Premium module in the [EducationDashDeck ecosystem](../education-dashdeck/).  
Full ecosystem overview — including Lesson Logs, Target Tracker, Session Pay, and Meet & Teach — is in the [education-dashdeck folder](../education-dashdeck/).

## Tech Stack

- Multi-tenant web app with DashDeck SSO
- PDF generation — portfolio and certificate printing (ReportLab)
- Evidence file storage (secure, per-client isolation)
- PostgreSQL (multi-tenant, row-level security)
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](../education-dashdeck/) — built by [Cognito Coding](https://cognitocoding.com)*
