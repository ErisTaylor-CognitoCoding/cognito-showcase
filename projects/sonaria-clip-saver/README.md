# Sonaria Clip Saver

A background screen recorder that automatically saves the last ~30 seconds of gameplay whenever a **KILL CONFIRMED** banner appears on screen. Built for Sonaria mains who are tired of missing highlight clips.

No reflexes required. Open the app once, share your game window, calibrate the banner, and play.

---

## Features

- **Rolling buffer** — your screen is continuously recorded into a 30-second loop in memory (configurable). Nothing is written to disk until something interesting happens.
- **Auto-detect KILL CONFIRMED** — a pixel scanner watches a calibrated region of the frame for the banner's signature colors (yellow, red, black, off-white) all co-occurring in the same window. When it fires, the buffer plus a short tail is saved as `.webm`.
- **Calibration** — press **F10** while the banner is on screen to lock the detector to its exact colors *and* position. After calibration the detector ignores the rest of the screen, which kills false positives from minimap dragons, blood splatters, and other HUD noise.
- **Manual save hotkey** — **F9** dumps the current buffer immediately. Use it for anything that isn't a kill banner.
- **Trigger-frame snapshot** — every auto-saved clip ships with a `.jpg` of the exact frame that fired the detector, so you can verify what triggered it.
- **Configurable post-detect delay** — choose how much footage to keep *after* the banner fires (default 1.5s). Useful for catching aftermath.
- **Dark, neon-green streamer aesthetic** — no emojis, no clutter.

---

## How it works

1. **Capture** — `getDisplayMedia` streams your selected window/screen into a `MediaRecorder` configured as a circular buffer (last N seconds, default 30).
2. **Detect** — every frame is sampled into an offscreen canvas. The pixels in the calibrated banner region are classified into yellow / red / black / off-white buckets, summed via an integral image, and scored with a sliding window. The score is `min(yellow, red, black, offwhite)` — all four must co-occur for the window to count.
3. **Confirm** — two consecutive hits (~200 ms) above the calibrated trigger threshold are required before saving. This rejects single-frame noise.
4. **Save** — on a confirmed hit, the rolling buffer plus the configured tail are flushed to disk as `.webm`, with the trigger frame written next to it as `.jpg`.

---

## Hotkeys

| Key | Action |
|---|---|
| **F9** | Save the current buffer to disk immediately |
| **F10** | Calibrate the KILL CONFIRMED banner (color + position) — do this while a real banner is on screen |

---

## Getting started

1. Open the app in a Chromium-based browser (Chrome, Edge, Brave). `getDisplayMedia` and `MediaRecorder` are required.
2. Click **Start** and pick the window or screen showing Sonaria.
3. Wait for a real KILL CONFIRMED banner. Press **F10** to calibrate.
4. Play. Clips will save automatically every time the banner fires.

Clips and trigger-frame JPGs land in the folder you pick when you grant file-system access (or in the browser's download folder as a fallback).

---

## Settings

Open the Settings panel from the main screen to adjust:

- **Buffer length** (seconds before the trigger to keep)
- **Post-detect delay** (milliseconds after the trigger to keep)
- **Detector sensitivity** (trigger threshold — lower means more sensitive, more false positives)
- **Calibrated banner box** (set by F10; can be cleared to fall back to the default search region)

---

## Tuning notes

- **Always calibrate.** Uncalibrated detection scans a tight upper-middle band of the frame as a safe default, but a calibrated run is far more reliable because the search is locked to the exact banner box. One press of F10 on a real banner is all it takes.
- **False positives** are dominated by HUD elements that share the banner's color palette — minimap creatures, blood splatters, environmental highlights. Calibration suppresses these geometrically; the detector simply doesn't look outside the calibrated box.
- **Missed kills** at default settings usually mean either the buffer is too short for what you wanted, or the banner appeared in an unusual position (different aspect ratio, UI scale). Recalibrate.

---

## Tech

- React + Vite + TypeScript
- Native Web APIs: `getDisplayMedia`, `MediaRecorder`, `OffscreenCanvas`, File System Access
- No backend, no telemetry, no accounts. Everything runs in your browser, clips stay on your machine.

---

## Status

Built as a single-user tool. Pull requests, issues, and tuning notes for other games with similar event banners welcome.
