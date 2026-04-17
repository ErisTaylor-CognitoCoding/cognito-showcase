# Award Tracker

> AQA Unit Award Scheme portfolio management — multi-tenant SaaS for alternative provision and SEND centres

## Overview

Award Tracker is a web application for managing the **AQA Unit Award Scheme** — a qualification framework for learners who struggle with traditional exams (SEND, alternative provision, vocational training).

The system helps centres:
- Track student progress across AQA units
- Collect and organise evidence (photos, documents, observations)
- Generate portfolios for AQA moderation
- Print certificates when units are completed

Award Tracker is Cognito's first **paying SaaS product**, live with Tutor Doctor Peterborough at £24.99/month.

## The Problem

The AQA Unit Award Scheme has no official tracking software. Centres use:
- Spreadsheets (error-prone, no collaboration)
- Paper folders (lost evidence, moderation nightmares)
- Generic project management tools (not built for AQA's structure)

We built Award Tracker because Zero (founder) tutors SEND learners and needed something better.

## Tech Stack

- **Backend**: Python 3.11 + Flask
- **Database**: PostgreSQL (multi-tenant architecture)
- **Frontend**: HTML/CSS/JS (server-rendered, minimal framework bloat)
- **Auth**: DashDeck SSO (organisation-level single sign-on)
- **PDF Generation**: ReportLab (certificates, portfolios)
- **File Storage**: Local filesystem (per-organisation directories)
- **Deployment**: Docker

## Architecture

```
┌────────────────────────────────────┐
│      DashDeck (Auth Hub)           │
│  Handles login, org selection      │
└────────────────────────────────────┘
              ↓ SSO
┌────────────────────────────────────┐
│     Award Tracker (Flask App)      │
│  Students | Units | Evidence       │
│  Portfolio Builder | Certificates  │
└────────────────────────────────────┘
              ↓
┌────────────────────────────────────┐
│  PostgreSQL (Multi-Tenant)         │
│  org_12345 schema → students, units│
│  org_67890 schema → students, units│
└────────────────────────────────────┘
```

### Multi-Tenancy Design

Each organisation (tutoring centre, school) gets:
- **Isolated database schema** (e.g. `org_12345`)
- **Own student/unit/evidence tables**
- **File storage directory** (`/uploads/org_12345/`)
- **No cross-contamination** — Organisation A cannot see Organisation B's data

This architecture allows one codebase to serve multiple paying clients securely.

## Key Features

### 1. **Student Management**
- Add students with basic details (name, DoB, entry date)
- Track which units each student is working on
- View progress dashboard per student

### 2. **Unit Library**
- AQA Unit Award Scheme catalogue (all official units)
- Search by subject area (Maths, English, Science, Life Skills, etc.)
- Assign units to students

### 3. **Evidence Collection**
- Upload photos, PDFs, documents
- Add observations (teacher notes)
- Tag evidence to specific AQA criteria
- Date-stamped and attributed to staff member

### 4. **Portfolio Builder**
- Auto-generate PDF portfolio per unit
- Includes student details, evidence, assessor sign-offs
- Formatted for AQA moderation submission
- Watermarked with organisation branding

### 5. **Certificate Printing**
- Generate official-looking certificates when unit completed
- Includes AQA branding, student name, unit title, date
- PDF download for printing

### 6. **Progress Tracking**
- Visual indicators: Not Started | In Progress | Completed
- Overview dashboard shows all students and their units
- Alerts for overdue or stalled units

## Lessons Learned

### What Worked Well

**Multi-tenancy from day one**: Building with isolated schemas from the start meant adding a second client (when that happens) requires zero code changes. Just provision a new schema.

**DashDeck SSO integration**: Authenticating via DashDeck means clients get one login for all Cognito apps. Award Tracker, Lesson Logs, Target Tracker all share auth. Huge UX win.

**PDF generation**: ReportLab is ugly but reliable. Portfolios render consistently, which is critical for regulatory compliance (AQA moderation).

**Filesystem storage over cloud**: For a small SaaS, local filesystem (organised per-org) is simpler and cheaper than S3/GCS. Backups via Docker volume snapshots work fine.

### What We'd Do Differently

**Evidence search**: Currently no way to filter evidence by date, type, or criteria. Users have to scroll through long lists. Need better filtering and search.

**Mobile upload**: Evidence collection happens in the classroom — staff want to snap photos on their phone and upload immediately. Current UI is desktop-first. Next version needs mobile-optimised upload flow.

**Moderation export**: AQA moderators want evidence in specific formats (ZIP archives with folder structure). Current PDF portfolio works but isn't ideal. Need export presets.

**Automated reminders**: Students stall on units. System should notify staff when a unit has been "In Progress" for X weeks with no new evidence.

**User roles**: Currently everyone in an organisation has full access. Need tutor vs admin roles (tutors can only see their own students).

## Revenue Model

- **£24.99/month per organisation** (unlimited students/users)
- Break-even at 16 customers (covers server + Zero's time)
- Current clients: 1 (Tutor Doctor Peterborough)
- Target: 20-50 UK alternative provision centres

## Why It's Defensible

- **Niche expertise**: Zero tutors SEND learners daily. Knows the pain points competitors don't.
- **AQA integration**: Bespoke to UK qualifications framework. Hard to replicate without domain knowledge.
- **Multi-tenant architecture**: Can scale to hundreds of clients without re-architecting.
- **DashDeck ecosystem**: Award Tracker is one app in a suite. Clients who adopt DashDeck get all apps under one roof.

---

*Built by [Cognito Coding](https://cognitocoding.com)*
