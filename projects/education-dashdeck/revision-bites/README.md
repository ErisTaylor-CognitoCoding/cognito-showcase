# Revision Bites

> Personalised weekly revision schedules with curriculum-aligned topics and progress tracking — inside EducationDashDeck.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Price](https://img.shields.io/badge/price-TBC-orange)
![Part of](https://img.shields.io/badge/part%20of-EducationDashDeck-blue)

## Overview

Revision Bites generates personalised weekly revision schedules for learners, aligned to their curriculum topics and adjusted week-by-week based on progress. Teachers and tutors set the subjects, topics, and exam timeline once — Revision Bites does the rest, delivering a structured revision plan the student can follow without constant hand-holding.

**Who it's for:** Tutoring agencies, AP/SEND providers, and solo tutors who spend time manually building revision plans for each student — or whose students arrive underprepared because no structured revision plan existed.

## Features

- **Curriculum-Aligned Topics** — Map subjects and topics to the student's exam syllabus. Supports GCSE, A-Level, and bespoke alternative-provision curricula.
- **Personalised Weekly Schedules** — Auto-generated revision timetable per student, balanced across subjects and weighted by upcoming assessments.
- **Progress Tracking** — Students mark topics as revised. Track completion rates across the cohort at a glance.
- **Adaptive Scheduling** — Topics marked weak or incomplete are automatically re-queued in subsequent weeks.
- **Exam Countdown** — Schedule anchored to real exam dates. As dates approach, weighting shifts to high-priority topics.
- **EducationDashDeck Integration** — Revision progress data feeds into Target Tracker. Lesson Logs session notes surface relevant revision topics for the next session.
- **Student-Facing View** — Clean weekly checklist students access directly — no login friction.

## Pricing

**TBC** — pricing being confirmed under the EducationDashDeck reshape.

## Status

🟡 **In Development**

## Part of EducationDashDeck

Revision Bites is one module in the [EducationDashDeck ecosystem](../).  
Progress data syncs with **Target Tracker** half-termly reports. Lesson Logs session records surface topic coverage gaps to surface in future revision schedules.

See the [full ecosystem overview](..) for pricing and architecture.

## Architecture Notes

```
Curriculum Map (subjects + topics + exam dates)
        │
        ▼
  Revision Bites
        │
        ├── Personalised weekly schedule per student
        ├── Progress logged (topic marked revised)
        │              ──▶ Target Tracker (progress summary)
        │              ──▶ Lesson Logs (topic surface on next session)
        ├── Adaptive re-queue (weak topics resurface)
        └── Exam-anchored weighting (countdown logic)
```

Multi-tenant isolation: each client's learner data is stored in a dedicated, isolated environment. No cross-tenant data access.

## Tech Stack

- Multi-tenant web app with EducationDashDeck SSO
- Dynamic schedule generation engine (Python)
- PostgreSQL (multi-tenant, row-level security)
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](..) — built by [Cognito Coding](https://cognitocoding.com)*
