# Flock Follow

![Django](https://img.shields.io/badge/Django-3.1-green)
![Flutter](https://img.shields.io/badge/Flutter-2.x-blue)

Flock Follow lets a group of people travelling together — a "flock" — share
their live location with each other until they reach their destination.
One person creates a flock and sets a password, others nearby join with
that password, and everyone in the flock can see each other on a shared
map, view the member list, and chat until the trip is over.

It's made up of two projects:

- **`backend/`** — a Django REST Framework API that stores users, flocks,
  members, and messages.
- **`mobileapp/`** — a Flutter app (Android & iOS) that registers a user,
  finds or creates nearby flocks, and shows everyone's live position on a
  map.

> Looking for a list of recent bug fixes and security hardening? See
> [`CHANGES.md`](./CHANGES.md).

## How it works

1. On first launch, the app asks for location permission and registers a
   new user (name + phone) with the backend.
2. From the home screen, the user sees nearby flocks (within roughly 5km)
   that haven't finished yet, and can join one with its password, or
   create a new flock of their own (which also sets a password).
3. Once in a flock, the map screen shows every member's live position,
   updating as each member's location changes. The flock leader can start
   the trip and later mark it finished; any other member can leave at any
   time.
4. A simple chat lets members in the same flock send each other messages
   while the flock is active.

## Project structure

```
backend/                  Django REST Framework API
  core/                   models, serializers, views for users/flocks/messages
  flock_follow/           project settings, URL routing
  manage.py
mobileapp/                Flutter app
  lib/
    data/                 API client + data models (User, Flock, Message, ...)
    *.dart                screens (register, home, map, members, messages, settings)
idea/                     early planning notes, schema diagrams, similar-app research
```

## Backend setup

Requirements: Python 3.8+ (the project is pinned to Django 3.1; newer
Python 3.12+ environments may need a newer Django/DRF pin — see
`requirements.txt`).

```bash
cd backend
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` (or otherwise export the variables it lists)
before running the server:

```bash
cp .env.example .env
```

At minimum, set a real `DJANGO_SECRET_KEY`. You can generate one with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

For local development, also set:

```bash
export DJANGO_DEBUG=true
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,10.0.2.2   # 10.0.2.2 = Android emulator's host
```

Then run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

The Django admin is available at `/admin/` (create a superuser first with
`python manage.py createsuperuser`).

> **Note:** every API endpoint is currently open to anonymous access — no
> authentication is enforced yet, even though the auth-related packages are
> installed. See `CHANGES.md` for details before deploying this publicly.

### API overview

All endpoints are under `/api/v1/` and exchange JSON.

| Method | Path                                          | Description                          |
|--------|------------------------------------------------|---------------------------------------|
| POST   | `/users/`                                       | Register a new user                   |
| GET    | `/users/<id>/`                                  | Get a user                             |
| PUT    | `/users/<id>/`                                  | Update a user (e.g. location)          |
| GET    | `/flocks/?lat=&lng=`                            | List nearby, not-yet-finished flocks   |
| POST   | `/flocks/`                                      | Create a flock (password required)     |
| GET    | `/flocks/<id>/`                                 | Get a flock                            |
| PUT    | `/flocks/<id>/`                                 | Update a flock (status, location, ...) |
| GET    | `/flocks/<id>/members/`                         | List a flock's members                 |
| POST   | `/flocks/<id>/members/<user_id>/`               | Join a flock (send `{"password": ...}`)|
| DELETE | `/flocks/<id>/members/<user_id>/`               | Leave a flock                          |
| GET    | `/flocks/<id>/messages/`                        | List a flock's chat messages           |
| POST   | `/flocks/<id>/messages/`                        | Post a chat message                    |

A flock's `password` is write-only — it's accepted when creating a flock
but never included in any API response, so it can't be read back by
listing or fetching flocks.

## Mobile app setup

Requirements: [Flutter SDK](https://flutter.dev) compatible with Dart
`>=2.7.0 <3.0.0` (this project predates Dart's null-safety migration, so
use an older stable Flutter release — roughly the 1.22–2.x line).

```bash
cd mobileapp
flutter pub get
```

The app talks to the backend at `flock-follow.live` over HTTPS
(`lib/data/backend.dart`). To point it at a local backend instead, change
the host passed to `Uri.https(...)` in that file (and make sure that host
is included in `DJANGO_ALLOWED_HOSTS` on the backend side).

Run on a connected device or emulator:

```bash
flutter run
```

Google Maps is used for the map screen — you'll need to add your own Maps
API key for Android (already has a placeholder in
`android/app/src/main/AndroidManifest.xml`) and for iOS (add a
`GMSServices.provideAPIKey("YOUR_KEY")` call in
`ios/Runner/AppDelegate.swift`, before `GeneratedPluginRegistrant.register`)
before the map will render. See the
[`google_maps_flutter` setup guide](https://pub.dev/packages/google_maps_flutter)
for details.

## Tech stack

- **Backend:** Django, Django REST Framework, SQLite (default; swap
  `DATABASES` in `flock_follow/settings.py` for production).
- **Mobile:** Flutter, Google Maps Flutter, `location` (GPS), `http`,
  `shared_preferences` (local user id), `loader_overlay`, `flutter_phoenix`
  (in-app restart after state-changing actions).

## Contributing

This is a small, evolving side project — issues and pull requests are
welcome. If you're picking up an area to improve, `CHANGES.md` lists known
gaps (auth, a couple of unused model fields) that are good starting points.
