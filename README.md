# Django Starter – Production‑Ready Boilerplate

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.15-red.svg)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-✓-2496ED.svg)](https://docker.com)
[![Celery](https://img.shields.io/badge/Celery-5.4-37814A.svg)](https://docs.celeryq.dev/)
![Nginx](https://img.shields.io/badge/Server-Nginx-009639?logo=nginx&logoColor=white)
![Redis](https://img.shields.io/badge/Broker-Redis-DC382D?logo=redis&logoColor=white)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Elasticsearch](https://img.shields.io/badge/Search-Elasticsearch-005571?logo=elasticsearch&logoColor=white)



A **complete, production‑ready Django starter project** with everything you need to build scalable web applications and REST APIs.  
**Zero boilerplate** – focus on your business logic, not on repetitive setup.



## ✨ Features

- ✅ **Modern Django 5.2** + **Django REST Framework 3.15**
- ✅ **Custom User Model** with email as username, roles (`admin`, `moderator`, `user`), and profile extension
- ✅ **JWT Authentication** (via `djoser` + `simplejwt`) – login, register, email verification, password reset
- ✅ **Full‑featured Notifications App** – email & SMS, templates, broadcasts, user preferences, database‑driven SMTP
- ✅ **Dockerized** – PostgreSQL, Redis, Celery, Flower, Nginx, Elasticsearch (ready for production)
- ✅ **Celery** – async task queue with Flower monitoring
- ✅ **Comprehensive Makefile** – one‑command dev workflow
- ✅ **Dynamic Project Renamer** – rename your project instantly (bidirectional)
- ✅ **Postman Collection** – complete, ready‑to‑import API documentation
- ✅ **Environment‑aware settings** (`base.py`, `dev.py`, `prod.py`)
- ✅ **Logging** – structured JSON‑ready logging with `CustomLogger`
- ✅ **CORS / Security Headers** – production‑hardened
- ✅ **Cloudflare R2 / S3 Storage** – pluggable
- ✅ **Code Quality** – Black, isort, flake8, pytest with coverage
- ✅ **OpenAPI Schema** – auto‑generated via `drf-spectacular`


## 📦 Quick Start (5 Minutes)

### Prerequisites
- Docker & Docker Compose
- Git

### 1. Clone & Enter
```bash
git clone https://github.com/miclemabasie/django-docker-starter.git my-new-project
cd my-new-project
```

### 2. Rename Your Project
After creating a virtual environment
```bash
make rename
# Enter your new project name (e.g., `myawesomeapi`)
```

### 3. Configure Environment
```bash
cp app/.env.example app/.env
# Edit app/.env – add your database passwords, email credentials, etc.
```

### 4. Build & Run
```bash
make build
make up
make migrate
make createsuperuser
make email-setup   # creates default email templates
```

### 5. Open Your Browser
- API Root: [http://localhost/api/v1/](http://localhost/api/v1/)
- Admin: [http://localhost/admin/](http://localhost/admin/)
- Flower (Celery monitor): [http://localhost:5557](http://localhost:5557)

---

## 📚 Project Structure

```
django-docker-starter/
├── app/                      # Django project root
│   ├── djangostarter/        # Main project folder (renamed to your project name)
│   │   ├── settings/         # Environment‑aware settings
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   └── celery.py
│   ├── apps/                # All Django apps
│   │   ├── core/           # Common utilities, base models, logging
│   │   ├── users/          # Custom user, profile, roles, JWT
│   │   └── notifications/  # Email/SMS, templates, broadcasts, user prefs
│   ├── manage.py
│   └── .env.example
├── docker/                  # Docker configuration
│   └── local/
│       ├── django/
│       └── nginx/
├── docker-compose.yml       # Main compose file
├── Makefile                 # Swiss army knife – everything via make
├── postman/                 # Postman collection & environment
│   ├── DjangoStarter.postman_collection.json
│   └── DjangoStarter.postman_environment.json
└── README.md
```

---

## 🔧 Configuration – Environment Variables

All configuration is driven by environment variables (`.env`).  
**Mandatory variables** are marked with 🔴.

```ini
# Django
SECRET_KEY=your-secret-key-here           # 🔴 Change this!
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (PostgreSQL)
POSTGRES_DB=myproject                    # 🔴 Set to your project name
POSTGRES_USER=postgresadmin
POSTGRES_PASSWORD=postgrespass
PG_HOST=postgres-db
PG_PORT=5432

# Redis / Celery
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

# Email (SMTP – used as fallback)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@example.com

# Twilio (for SMS) – optional
SMS_BACKEND=console                     # or 'twilio'
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=

# Cloudflare R2 (optional)
CLOUDFLARE_R2_BUCKET=
CLOUDFLARE_R2_BUCKET_ENDPOINT=
CLOUDFLARE_R2_ACCESS_KEY=
CLOUDFLARE_R2_SECRET_KEY=
CLOUDFLARE_R2_TOKEN=

# CORS (development)
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
```

---

## 🛠️ Development Workflow – The Makefile

**The one‑stop shop for all commands.**  
Just run `make help` to see everything.

| Command                | Description |
|------------------------|-------------|
| `make up`              | Start all containers |
| `make down`            | Stop containers |
| `make logs`            | Tail all logs |
| `make api-logs`        | Tail Django logs |
| `make shell`           | Django shell_plus |
| `make migrate`         | Run migrations |
| `make makemigrations`  | Create migrations |
| `make test`            | Run pytest with coverage |
| `make lint`            | Run flake8 + black + isort |
| `make format`          | Auto‑format code |
| `make rename`          | Rename the entire project |
| `make email-setup`     | Create default email templates |
| `make dump-db`         | Backup database |
| `make psql`            | Open PostgreSQL CLI |

**Pro tip:** `make watch` automatically re‑runs linters/tests when you save a Python file – ideal for TDD.

---

## 👥 User Management & Authentication

### 🔐 JWT Authentication (djoser + simplejwt)

| Endpoint                                 | Method | Description                  |
|------------------------------------------|--------|------------------------------|
| `/api/v1/auth/users/`                   | POST   | Register new user           |
| `/api/v1/auth/users/activation/`        | POST   | Activate account            |
| `/api/v1/auth/jwt/create/`              | POST   | Login → get tokens          |
| `/api/v1/auth/jwt/refresh/`             | POST   | Refresh access token        |
| `/api/v1/auth/users/reset_password/`    | POST   | Request password reset      |
| `/api/v1/auth/users/reset_password_confirm/` | POST | Confirm reset |

After registration, the user is **inactive** until they verify their email – secure by default.

### 👤 Custom User API (ViewSet)

| Endpoint                          | Method | Description                          |
|-----------------------------------|--------|--------------------------------------|
| `/api/v1/users/me/`              | GET    | Get current user profile           |
| `/api/v1/users/update_me/`       | PATCH  | Update own profile                 |
| `/api/v1/users/delete_me/`       | DELETE | Deactivate own account            |
| `/api/v1/users/`                | GET    | List all users (admin only)        |
| `/api/v1/users/{id}/`           | GET    | Retrieve user (owner/admin)        |
| `/api/v1/users/assign_role/`    | POST   | Change user role (admin only)      |

**Roles:** `admin`, `moderator`, `user`.  
Permissions are fully enforced – users can only access their own data unless they are staff.

---

## 📬 Notifications System

A complete, database‑driven notification engine.

### 📧 Email Configuration (Database)

Instead of hardcoding SMTP in settings, you can **store multiple email configurations in the database** and switch between them on the fly.

**API Endpoints (admin only):**
- `GET|POST /api/v1/notifications/email-configs/`
- `GET|PUT|PATCH|DELETE /api/v1/notifications/email-configs/{id}/`

Only one config can be active at a time. If no active config exists, the system falls back to `settings.EMAIL_*`.

### 📄 Templates

Create reusable email/SMS templates with **Django Template Language** syntax.  
Variables like `{{ user.first_name }}`, `{{ site_name }}`, `{{ year }}` are auto‑injected.

**API Endpoints:**
- CRUD on `/api/v1/notifications/templates/`

### 📨 Broadcasts

Send a template to a **segment of users** defined by a JSON filter (e.g., `{"is_active": true, "role": "user"}`).  
Broadcasts are processed asynchronously via Celery.

**API Endpoints:**
- CRUD on `/api/v1/notifications/broadcasts/`
- `POST /api/v1/notifications/broadcasts/{id}/send/` – start sending

### 🔔 User Notification Settings

Every user can control their notification preferences:

```json
{
  "email_enabled": true,
  "sms_enabled": false,
  "receive_marketing_emails": false,
  "receive_security_emails": true
}
```

**API Endpoints:**
- `GET|PATCH /api/v1/notifications/settings/`

---

## 📡 API Documentation & Postman

We provide a **complete, ready‑to‑import Postman collection** with:

- ✅ Every endpoint (auth, users, notifications, email configs, broadcasts)
- ✅ Environment variables (`base_url`, `access_token`, etc.)
- ✅ Example payloads for each request
- ✅ Pre‑request scripts to automatically save tokens

**Files are located in `/postman/`.**  
Import both `DjangoStarter.postman_collection.json` and `DjangoStarter.postman_environment.json` into Postman.

For OpenAPI/Swagger, generate the schema:
```bash
make schema-yaml   # creates schema.yaml
make schema-json   # creates schema.json
```

---

## 🧪 Testing

We use **pytest** with coverage reporting.

```bash
make test          # run tests with terminal coverage
make test-html     # run tests + HTML coverage report (opens in browser)
```

Tests are located inside each app’s `tests/` directory.  
**We already include tests for:**
- User registration & activation
- Profile retrieval & update
- Permission checks (owner vs admin)
- Notification sending

Add more tests as your business logic grows.

---

## 🐳 Docker & Production

### Production‑Ready Features
- **Nginx** – serves static/media, reverse proxy
- **PostgreSQL** – persistent volume
- **Redis** – Celery broker
- **Celery** – background tasks
- **Flower** – Celery monitoring (port 5557)
- **Elasticsearch** – ready for search (optional)

### Deploy to Production
1. Set `DEBUG=False` and a strong `SECRET_KEY` in `.env`.
2. Configure `ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS`.
3. Use a production email backend (e.g., SendGrid, Amazon SES).
4. (Optional) Enable Cloudflare R2 for media storage.
5. Run:
   ```bash
   docker compose -f docker-compose.yml up -d --build
   ```

**Recommended:** Use a reverse proxy (Traefik, Caddy) for automatic SSL.

---

## 🎯 Project Renaming – One Command to Rule Them All

**Never manually edit file names again.**  
Our custom management command renames your entire project – **bidirectional** and **idempotent**.

```bash
# Rename from 'djangostarter' to 'myproject'
python manage.py rename_project myproject

# Rename back to 'djangostarter'
python manage.py rename_project djangostarter --current-name myproject
```

It updates:
- ✅ Project directory
- ✅ All Python imports (`from djangostarter...` → `from myproject...`)
- ✅ Django settings (`ROOT_URLCONF`, `WSGI_APPLICATION`, etc.)
- ✅ Docker volumes, networks, container names
- ✅ `.env` and `.env.example`
- ✅ `docker-compose.yml`
- ✅ `Makefile`
- ✅ `README.md`

**Zero manual effort.** This is the foundation for starting dozens of projects without repetitive work.

---

## 🧰 Development Tools

### Code Formatting & Linting

We enforce strict code quality with:
- **Black** – uncompromising formatter
- **isort** – import sorter
- **flake8** – linter

```bash
make format   # runs black + isort
make lint     # runs flake8 + black-check + isort-check
```

### Pre‑commit Hooks (Recommended)

Install pre‑commit hooks to automatically format/lint before each commit:

```bash
pip install pre-commit
pre-commit install
```

Then create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing`).
5. Open a Pull Request.

**Please ensure your code passes `make lint` and `make test` before submitting.**

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

Built with the best tools in the Python ecosystem.  
Special thanks to the Django, DRF, Celery, and Docker communities.

---

**Now go build something amazing!** 
```