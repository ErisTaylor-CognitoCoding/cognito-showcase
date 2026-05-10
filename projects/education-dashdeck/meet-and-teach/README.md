# Meet & Teach

> Integrated video tutoring with interactive whiteboard, scientific calculator, and screen sharing — inside EducationDashDeck.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Price](https://img.shields.io/badge/price-%C2%A319.99%2Fmo-orange)
![Part of](https://img.shields.io/badge/part%20of-EducationDashDeck-blue)

## Overview

Meet & Teach replaces Lessonspace — and the Zoom + Bitpaper workaround. Video call, interactive whiteboard, scientific calculator, and screen sharing in a single browser tab. No downloads for students. No third-party subscriptions.

The key difference: when the session ends, it auto-logs into Lesson Logs. Duration, tutor, student, subject — captured automatically. Zero admin.

**Who it's for:** Tutoring agencies delivering online sessions who are paying for Lessonspace, or cobbling together Zoom + an IWB app, and want everything in one place that also updates their session records automatically.

## Features

- **Video Call** — Peer-to-peer WebRTC video. Browser-native. No Zoom subscription. No download required for students.
- **Interactive Whiteboard** — Freehand draw, shapes, document upload (PDF, images), multiple background types: plain, lined, graph paper, dot grid.
- **Scientific Calculator** — Embedded scientific calculator accessible during the session without switching tabs.
- **Screen Sharing** — One-click screen share without leaving the session window.
- **Auto Session Logging** — When the session ends, a Lesson Log entry is created automatically: tutor, student, duration, subject, date, and session notes. No admin.
- **In-Session Notes** — Tutor notes panel during the session that convert to the session log on close.
- **Session Replay** *(roadmap)* — Whiteboard session replay for student review after the session.

## Pricing

**£19.99/month** as a DashDeck add-on (Premium tier).

## Status

🟡 **In Development** — Available at [cognitocoding.com](https://cognitocoding.com)

## Part of Education DashDeck

Meet & Teach is one module in the [EducationDashDeck ecosystem](../).  
It is the only DashDeck module that auto-creates entries in **Lesson Logs** — making it the fastest path to a complete session record.

See the [full ecosystem overview](..) for pricing and architecture.

## Architecture Notes

```
Meet & Teach session
        │
        ├── WebRTC video (peer-to-peer, browser-native)
        ├── Canvas whiteboard (server-side canvas API)
        ├── Screen share (browser MediaStream API)
        └── On session close:
                │
                ▼
          Lesson Logs (auto-entry)
                │
                ├──▶ Target Tracker (progress data)
                ├──▶ Session Pay (billable session)
                └──▶ Award Tracker (evidence timestamp)
```

A Meet & Teach session creates data that flows through the entire DashDeck ecosystem — Lesson Logs, Target Tracker, Session Pay, and Award Tracker all updated from one event.

## Tech Stack

- WebRTC peer-to-peer video (no third-party video platform)
- HTML5 Canvas interactive whiteboard
- Browser MediaStream API (screen sharing)
- DashDeck SSO integration
- Auto-integration with Lesson Logs on session close
- PostgreSQL multi-tenant data store
- Hosted by Cognito Coding — no installation required

---

*Part of the [EducationDashDeck ecosystem](..) — built by [Cognito Coding](https://cognitocoding.com)*
