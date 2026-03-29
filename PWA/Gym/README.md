# Gym Pro - Gym Management System

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://abdallaheldaly.github.io/Projects/PWA/Gym/index.html)
[![PWA](https://img.shields.io/badge/PWA-Ready-blue)](https://abdallaheldaly.github.io/Projects/PWA/Gym/index.html)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A progressive web application (PWA) for managing gym memberships, attendance tracking, and financial records. Built with vanilla JavaScript, HTML5, and CSS3 — no frameworks, no backend required.

**[Live Demo →](https://abdallaheldaly.github.io/Projects/PWA/Gym/index.html)**

---

## Features

### Membership Management
- Add new members with subscription details
- Track subscription duration and expiration dates
- Automatic end-date calculation based on subscription length
- Financial tracking (total amount, paid amount, remaining balance)
- Edit and delete member records

### Attendance System
- Daily attendance marking with timestamp
- Calendar view showing attendance history
- Attendance statistics per member
- Quick attendance from member list

### Dashboard & Analytics
- Real-time statistics (total members, active subscriptions, today's attendance)
- Revenue tracking (total revenue, monthly revenue)
- Expiration alerts (expired subscriptions, expiring within 7 days)
- Recent activity feed

### Data Portability
- **Export**: Download all data as JSON file
- **Import**: Restore data from JSON backup
- **Portable**: Move your data between devices easily
- No browser storage dependencies — data travels with your file


---

## Getting Started

### Option 1: Use Online (Recommended)
Simply visit the **[Live Demo](https://abdallaheldaly.github.io/Projects/PWA/Gym/index.html)** and start using immediately.

### Option 2: Run Locally
1. Download `index.html`
2. Open in any modern web browser
3. Start managing your gym data

### Option 3: Install as PWA
1. Visit the live demo in Chrome/Edge/Safari
2. Click "Add to Home Screen" or install prompt
3. Use as standalone app on desktop or mobile

---

## How to Use

### Adding a Member
1. Navigate to "Add Member" tab
2. Fill in phone number, name, start date, and subscription duration
3. Enter financial details (total amount, paid amount)
4. Click "Save" — the system auto-calculates end date and remaining balance

### Marking Attendance
1. Go to "Attendance" tab
2. Select member from dropdown
3. Click "Check-in Now" to record attendance with timestamp
4. View attendance calendar and history below

### Backup Your Data
&gt; **Important**: Since this app doesn't use browser storage for portability, you must manually export your data.

1. Go to "Dashboard" → Backup section
2. Click "Save Backup" to download `gym_backup_YYYY-MM-DD.json`
3. Store this file safely with your `index.html`

### Restore Data on New Device
1. Open `index.html` on new device/browser
2. Click "Restore Backup"
3. Select your previously saved `.json` file
4. All data is restored instantly

---

## Technical Details

### Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Storage**: In-memory with JSON file export/import
- **PWA**: Service Worker, Web App Manifest
- **Styling**: CSS Variables, Flexbox, Grid, Animations

### Browser Compatibility
- Chrome/Edge 80+
- Firefox 75+
- Safari 13+
- Opera 67+
- iOS Safari 13+
- Chrome Android 80+

### Data Structure
```json
{
  "members": [
    {
      "id": 1712345678901,
      "phone": "01234567890",
      "name": "John Doe",
      "startDate": "2024-01-01",
      "duration": 3,
      "endDate": "2024-04-01",
      "totalAmount": 1500,
      "paidAmount": 1000,
      "remainingAmount": 500,
      "createdAt": "2024-01-01T10:00:00.000Z"
    }
  ],
  "attendance": {
    "1712345678901": [
      {
        "date": "2024-01-15",
        "time": "06:30 PM",
        "timestamp": "2024-01-15T18:30:00.000Z"
      }
    ]
  },
  "exportDate": "2024-01-15T20:00:00.000Z",
  "version": "1.0"
}