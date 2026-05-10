# Session Pay

> Session-based payment tracking and professional invoicing — inside EducationDashDeck.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Price](https://img.shields.io/badge/price-%C2%A39.99%2Fmo-orange)
![Part of](https://img.shields.io/badge/part%20of-EducationDashDeck-blue)

## Overview

Session Pay closes the loop between teaching and getting paid. Sessions logged in Lesson Logs automatically appear in Session Pay's billing queue. Generate invoices, track payments, and produce a clean monthly income summary — without a separate spreadsheet, without double-entry, without chasing missing hours at the end of the month.

**Who it's for:** Tutoring agencies who invoice parents or commissioners per session and need to track which invoices have been paid, which are overdue, and what the month's income looks like across all tutors.

## Features

- **Auto Session Pull** — Billable sessions flow in from Lesson Logs automatically. No double-entry.
- **Flexible Billing** — Bill per session, per hour, or set a flat monthly rate per student.
- **Invoice Generation** — Professional PDF invoices branded to the agency or tutor. One click per client.
- **Payment Tracking** — Mark invoices as paid, part-paid, or overdue. Automatic chaser reminders for overdue invoices.
- **Income Summary** — Monthly income breakdown by student, tutor, and subject. Export to CSV for accountants or HMRC.
- **DashDeck Integration** — Full billing history visible from each student's profile. Session count and income in one view.

## Pricing

**£9.99/month** as a DashDeck add-on (Basic tier).  
Included in EducationDashDeck Small (1 Basic module free in base price).

## Status

🟡 **In Development** — Available at [cognitocoding.com](https://cognitocoding.com)

## Part of Education DashDeck

Session Pay is one module in the [EducationDashDeck ecosystem](../).  
It is the billing layer — fed automatically by **Lesson Logs**, visible from the student profile in the DashDeck command centre.

See the [full ecosystem overview](..) for pricing and architecture.

## Architecture Notes

```
Lesson Logs (session records)
        │
        ▼
  Session Pay billing queue
        │
        ├── Rate: £X per session / per hour / flat monthly
        ├── Invoice (PDF) ──▶ Parent / Commissioner
        ├── Payment status: Paid / Part-paid / Overdue
        └── Monthly income report (CSV)
```

All sessions become billable events automatically. The agency never manually enters session data into an invoicing spreadsheet.

## Tech Stack

- Module-based architecture inside EducationDashDeck
- PDF invoice generation (ReportLab)
- Shared session data from Lesson Logs
- CSV export for accountants / HMRC returns
- PostgreSQL multi-tenant data store
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](..) — built by [Cognito Coding](https://cognitocoding.com)*
