# 👨‍💻 Projects

A collection of the projects, courses, challenges and experiments I've built while learning and working as a developer — covering **web back-end, mobile, data analysis, game development, DevOps and problem solving**.

Each folder is a self-contained project (or a group of related ones). Open the folder to find its own code and, in many cases, its own README with run instructions.

---

## 🧰 Tech at a glance

| Area | Technologies |
|---|---|
| **Languages** | Python, PHP, C, Kotlin, Dart, JavaScript / TypeScript, SQL, HTML / CSS |
| **Back-end** | Django, Django REST Framework, Flask, FastAPI, Laravel, Slim (PHP) |
| **Mobile** | Kotlin (Android), Flutter |
| **Front-end** | HTML / CSS / JS, PWA, Angular |
| **Data** | Pandas, NumPy, Matplotlib, Jupyter, Power BI, Excel, Tableau, MySQL / SQLite |
| **Games / 3D** | Unity, Pygame, Flame (Flutter), Blender (`bpy`) |
| **DevOps** | Docker, Docker Compose, Nginx, Kubernetes basics, GitHub Actions |

---

## 📑 Table of contents

- [Live demos](#-live-demos)
- [Web back-end](#-web-back-end)
- [Mobile apps](#-mobile-apps)
- [Progressive Web Apps](#-progressive-web-apps-pwa)
- [Games & creative](#-games--creative)
- [Data & analytics](#-data--analytics)
- [Problem solving & interviews](#-problem-solving--interviews)
- [Courses & practice](#-courses--practice)
- [Tools & utilities](#-tools--utilities)
- [Repository structure](#-repository-structure)
- [About me](#-about-me)

---

## 🌐 Live demos

| Project | Link |
|---|---|
| Speculum Animae — browser game (Global Game Jam 2026) | [Play in browser](https://abdallaheldaly.github.io/Projects/Global%20Game%20Jam/2026/index.html) · [itch.io](https://abdallaheldaly.itch.io/the-mirror-within-a-journey-of-self) |
| Countdown Timer Pro (PWA) | [Open](https://abdallaheldaly.github.io/Projects/PWA/Counter/index.html) |
| Gym Pro — gym management (PWA) | [Open](https://abdallaheldaly.github.io/Projects/PWA/Gym/index.html) |
| Auto Parts Store Management System (PWA) | [Open](https://abdallaheldaly.github.io/Projects/PWA/SparePartsManagementSystem/%D9%86%D8%B8%D8%A7%D9%85_%D8%A7%D8%AF%D8%A7%D8%B1%D8%A9_%D9%82%D8%B7%D8%B9_%D8%A7%D9%84%D8%BA%D9%8A%D8%A7%D8%B1.html) |

---

## 🖥️ Web back-end

### [Flock Follow](./flock-follow) — Django REST + Flutter
Live location sharing for groups travelling together. One person creates a "flock" with a password, others nearby join, and everyone sees each other on a shared map, a member list and a chat until the trip ends.
- `backend/` — Django REST Framework API (users, flocks, members, messages)
- `mobileapp/` — Flutter app for Android & iOS

### [Text to MP3 (TTS)](./TTS/tts-project) — Python / Flask
Converts English or Arabic (Fusha or Egyptian) text — up to roughly 35,000 words — into a single MP3 file, with an HTML interface launched from the terminal and a CLI mode.

### [Django](./Django)
| Project | Description |
|---|---|
| [`project-0`](./Django/project-0) | REST API with Django REST Framework: customers, professions and data sheets (many-to-many and one-to-one relations, serializers). |
| [`project-1`](./Django/project-1) | Django site starter (portfolio-style app with project/testsite structure and image uploads). |

### [Flask](./Flask)
| Project | Description |
|---|---|
| [`project-0`](./Flask/project-0) | REST API protected with **JWT token authentication**. |
| [`project-1`](./Flask/project-1) | Small Flask API exercise. |

### [FastAPI](./FastAPI/fast)
Four progressive mini-projects:
- `url_path_parameters` — path parameters
- `query_parameters` — query parameters
- `crud_application` — CRUD for blog posts with Pydantic models
- `fast_api` — FastAPI + SQLAlchemy + SQLite with an HTML template

### [Laravel](./laravel) — 7 projects
| Project | What it covers |
|---|---|
| [`project-0`](./laravel/project-0) | Controllers, models and routing (students / users). |
| [`project_1`](./laravel/project_1) | Models and migrations (owner / boss / customer / student). |
| [`project_2`](./laravel/project_2) | Products CRUD with `ProductController`. |
| [`project_3`](./laravel/project_3) | Authentication scaffolding + user profiles. |
| [`project_4`](./laravel/project_4) | API authentication (`AuthController`). |
| [`project_5`](./laravel/project_5) | Passport-based API auth + Posts API. |
| [`project_6`](./laravel/project_6) | API-ready Laravel base setup. |

### [Restful API with Slim](./Restful_API_Slim) — PHP
Slim framework examples: route arguments, optional parameters, JSON responses, multiple HTTP methods, and PUT / DELETE handling.

### [Query Builder](./query/query_builder)
Jupyter notebook for filtering and querying an employees dataset.

---

## 📱 Mobile apps

### [Kotlin projects](./Kotlin_projects) — Android (5 apps)
| Project | Focus |
|---|---|
| `project-0` | Views, `EditText` and `Button` handling. |
| `project-1` | Reading user input and displaying results in `TextView`s. |
| `project-2` | Navigating between activities with `Intent`. |
| `project-3` | Passing an object (employee data) between activities. |
| `project-4` | `ListView` with item-click events and `Toast` messages. |

### [Djambi (improved)](./djambi-improved) — Flutter + Flame
An improved version of an open-source Flutter implementation of **Djambi**, the 1975 four-player strategy board game on a shared 9×9 board. Includes docs and an architecture diagram. Original project: [mabdelaal86/djambi](https://github.com/mabdelaal86/djambi).

### Flock Follow (mobile client)
See [Flock Follow](#flock-follow--django-rest--flutter) above.

---

## 📲 Progressive Web Apps (PWA)

Offline-capable apps built with plain HTML, CSS and JavaScript — no frameworks and no backend.

| Project | Description |
|---|---|
| [Countdown Timer Pro](./PWA/Counter) | Accurate countdown timer for Android, Mac and browsers that keeps running in the background. |
| [Gym Pro](./PWA/Gym) | Manage gym memberships, subscription end dates, attendance, payments and training schedules. |
| [Auto Parts Store Management](./PWA/SparePartsManagementSystem) | Offline-first inventory system for auto parts stores (Arabic interface). |

---

## 🎮 Games & creative

| Project | Description |
|---|---|
| [Global Game Jam 2026 — *Speculum Animae*](./Global%20Game%20Jam/2026) | A 15-stage philosophical, introspective browser experience inspired by Carl Jung. |
| [Global Game Jam 2020 — *Doors*](./Global%20Game%20Jam/2020) | Unity game built with Jam Squad around the theme "Doors"; showcased at ITI. |
| [Pygame](./pygame/project-0) | First 2D game built with Pygame. |
| [Blender — Door](./blender/door) | Procedural 3D door generated with a Python (`bpy`) script. |

---

## 📊 Data & analytics

| Project | Description |
|---|---|
| [Power BI Diploma](./Power_Bi_Diploma) | Material from a diploma funded by **Creativa Innovation Hubs (ITIDA)**: Excel, SQL, Python (NumPy / Pandas), statistics, Power BI — plus a **graduation project** analysing a data-analyst jobs / salaries dataset (notebooks, SQL and a Tableau workbook). Includes a Dockerfile to run the notebooks in Jupyter. |
| [Data Science](./Data_Science) | NumPy, Matplotlib 2D plotting and linear-algebra notebooks, plus Python fundamentals course tasks (types, strings, lists, tuples, conditions, loops, functions). |
| [Kaggle — Tech Support Conversations](./kaggle/Tech%20Support%20Conversations%20Dataset) | Exploratory analysis of a tech-support conversations dataset. |
| [Query Builder](./query/query_builder) | Pandas-style querying on an employees dataset. |

---

## 🧠 Problem solving & interviews

| Folder | Description |
|---|---|
| [problem_solving_and_algorithms](./problem_solving_and_algorithms) | **150+ LeetCode solutions in Python**, exercises from *Data Structures and Algorithms Using Python*, and Python practice. I also help others with problem solving on my YouTube channel. |
| [code_interview](./code_interview) | Solutions to real company assessments: a Microsoft Egypt software interview task (Sept 2024), a data deduplication / matching / analysis assessment, and PHP / JavaScript coding tasks. |
| ↳ [Task Manager](./code_interview/php/php_native/CRUD_Operations) | CRUD task app in native PHP with Nginx + Docker, storing data in JSON. |
| ↳ [Secure File Attacher](./code_interview/php/php_native/Secure_File_Attacher) | File upload / list / delete app with image validation (JPG, PNG, GIF), running on Docker + Nginx + PHP. |

---

## 📚 Courses & practice

### [CS50x 2022](./CS50/CS50x_2022)
Problem sets from Harvard's CS50x:

| Week | Topic | Solutions |
|---|---|---|
| 1 | C basics | Hello, Mario (less / more), Cash, Credit |
| 2 | Arrays | Scrabble, Readability, Caesar, Substitution |
| 3 | Algorithms | Plurality, Runoff, Tideman, Sort |
| 4 | Memory | Volume, Filter (less / more), Recover |
| 5 | Data structures | Speller, Inheritance |
| 6 | Python | Mario, Cash, Credit, Readability, DNA, World Cup |
| 7 | SQL | Movies (13 queries), Songs, Houses |
| 9 | Flask | Finance, Birthdays |

### [Recap & rehearsal code](./recap_rehearsal_code)
Revision exercises across the stack:
- **Docker & Kubernetes** — Dockerfiles and Compose files
- **SQL 101** — MySQL queries with Docker Compose
- **Django e-commerce app** — back-end practice
- **FastAPI** — quick test API
- **Angular** — `car-store` and `definition-of-a-person` apps
- **Front-end basics** — HTML fundamentals
- **Python basics** — notebook

---

## 🛠️ Tools & utilities

| Project | Description |
|---|---|
| [Guest Price Converter](./work/BTE) | Single-page calculator that converts guest prices from USD to EGP. |

---

## 🗂️ Repository structure

```text
Projects/
├── CS50/                          # CS50x 2022 problem sets (C, Python, SQL, Flask)
├── Data_Science/                  # NumPy, Matplotlib, linear algebra notebooks
├── Django/                        # Django & DRF projects
├── FastAPI/                       # FastAPI mini-projects
├── Flask/                         # Flask APIs
├── Global Game Jam/               # 2020 (Unity) and 2026 (browser) game jam entries
├── Kotlin_projects/               # 5 Android apps
├── PWA/                           # Countdown, Gym Pro, Auto Parts management
├── Power_Bi_Diploma/              # Data analysis diploma + graduation project
├── Restful_API_Slim/              # PHP Slim REST API examples
├── TTS/                           # Text-to-MP3 (English / Arabic)
├── blender/                       # Procedural Blender scripts
├── code_interview/                # Company interview tasks
├── djambi-improved/               # Flutter + Flame board game
├── flock-follow/                  # Django API + Flutter live-location app
├── kaggle/                        # Kaggle dataset analysis
├── laravel/                       # 7 Laravel projects
├── problem_solving_and_algorithms/# LeetCode & DSA in Python
├── pygame/                        # Pygame game
├── query/                         # Query builder notebook
├── recap_rehearsal_code/          # Docker, SQL, Django, Angular, etc.
└── work/                          # Small work utilities
```

---

## ▶️ Running a project

Every project is independent. In general:

```bash
git clone https://github.com/abdallaheldaly/Projects.git
cd Projects/<project-folder>
```

Then follow the project's own README or use the usual commands for its stack:

| Stack | Typical commands |
|---|---|
| Python (Flask / FastAPI / Django) | `python -m venv venv && source venv/bin/activate` → `pip install -r requirements.txt` → `python app.py` / `uvicorn main:app --reload` / `python manage.py runserver` |
| Laravel / PHP | `composer install` → `php artisan serve` |
| Docker projects | `docker-compose up -d` |
| Flutter | `flutter pub get` → `flutter run` |
| Android (Kotlin) | Open the project in Android Studio and run |
| PWA / HTML | Open `index.html` in a browser, or use the live demo links above |

---

## 🙋 About me

**Abdallah Eldaly** — software developer who enjoys building across the stack, from APIs and mobile apps to data analysis and games.

- GitHub: [@abdallaheldaly](https://github.com/abdallaheldaly)
- YouTube: [Problem-solving channel](https://www.youtube.com/channel/UCWI8Y-otDYNJc7iYapNm-jQ)

⭐ If you find something useful here, feel free to star the repo.
