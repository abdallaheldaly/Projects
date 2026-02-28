# Countdown Timer Pro

A beautiful, accurate, and feature-rich countdown timer that works seamlessly across Android, Mac, and all modern browsers. Runs perfectly in the background even when the app is closed or your screen is locked.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Android%20%7C%20Mac%20%7C%20Web-green.svg)
![PWA](https://img.shields.io/badge/PWA-Ready-orange.svg)

---

## 🎯 Live Demo

**Try it now:** [https://yourusername.github.io/countdown-timer](https://yourusername.github.io/countdown-timer)

*No installation required - works instantly in your browser!*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Highly Accurate** | Uses system time synchronization to maintain precision even in background |
| 📱 **Cross-Platform** | Works on Android, Mac, Windows, iOS, and any modern browser |
| 🌙 **Background Mode** | Timer continues running even if you close the app or switch tabs |
| 🔔 **Smart Notifications** | Alerts you when time is up, even if the app is closed |
| 🎨 **4 Beautiful Themes** | Neon, Classic Dark, Light Modern, and Warm |
| ⚡ **Progressive Web App** | Install it like a native app, works offline |
| 🔒 **Wake Lock** | Prevents screen from sleeping while timer is running |
| 📊 **Visual Progress** | Progress bar shows remaining time at a glance |
| ⚡ **Quick Presets** | 1m, 5m, 10m, 25m, 30m, 1h shortcuts |
| 📳 **Vibration Alerts** | Haptic feedback when timer completes (on supported devices) |

---

## 🚀 Quick Start

### Option 1: Try Online (Instant)
👉 **[Open Live Demo](https://yourusername.github.io/countdown-timer)**

### Option 2: Direct Use (Offline)
1. Save the `index.html` file
2. Open it in any modern browser (Chrome, Safari, Firefox, Edge)
3. Start using immediately!

### Option 3: Install as App (Recommended)

**Android:**
1. Open the file in Chrome
2. Tap menu (⋮) → **"Add to Home screen"** or **"Install app"**
3. Launch from your home screen like any native app

**Mac (Safari):**
1. Open the file in Safari
2. Click **Share** → **"Add to Dock"**

**Mac/Windows (Chrome):**
1. Open the file in Chrome
2. Click the install icon (➕) in the address bar, or go to menu → **"Install"**

---

## 🎨 Themes

Click the theme buttons in the top-right corner to switch between:

| Theme | Description | Best For |
|-------|-------------|----------|
| **Neon** | Cyan glow on dark background | Night use, modern look |
| **Classic Dark** | Purple accents on dark gray | Eye comfort, professional |
| **Light** | Clean white with blue accents | Day use, bright environments |
| **Warm** | Orange tones on brown | Relaxed, cozy atmosphere |

Your theme preference is automatically saved.

---

## 📖 How to Use

### Setting the Timer
1. Enter hours, minutes, and seconds in the input fields
2. Or click a **preset button** (1m, 5m, 10m, etc.) for quick setup
3. Click **Start** to begin countdown

### Controls
- **Start** - Begin countdown
- **Pause** - Pause timer (click Resume to continue)
- **Reset** - Stop and clear timer

### Background Operation
- Feel free to switch apps, lock your screen, or close the browser
- The timer uses system time calculation to stay accurate
- You'll receive a notification when time is up
- Progress is saved in browser storage

---

## 🔧 Technical Details

### How It Works
- **Time Calculation**: Uses `Date.now()` and end-time comparison instead of simple interval counting
- **Background Sync**: Saves end timestamp to `localStorage` and syncs on visibility change
- **Wake Lock**: Uses Screen Wake Lock API to prevent device sleep (with fallback for iOS)
- **Service Worker**: Enables offline functionality and background processing
- **Web Audio API**: Generates alert sounds without external files

### Browser Compatibility

| Feature | Chrome | Safari | Firefox | Edge |
|---------|--------|--------|---------|------|
| Basic Timer | ✅ | ✅ | ✅ | ✅ |
| Background Mode | ✅ | ✅ | ✅ | ✅ |
| Notifications | ✅ | ✅ | ✅ | ✅ |
| Wake Lock | ✅ | ✅ | ❌ | ✅ |
| Install as App | ✅ | ✅ | ❌ | ✅ |

---

## 🛠️ Development

### File Structure