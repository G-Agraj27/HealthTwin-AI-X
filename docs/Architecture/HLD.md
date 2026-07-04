# High Level Design (HLD)

# HealthTwin AI X

Version: 1.0

---

# 1. System Overview

HealthTwin AI X is a modular AI-powered healthcare platform.

The system consists of:

- Landing Website
- Patient Portal
- Doctor Portal
- Admin Portal
- AI Services
- PostgreSQL Database
- File Storage
- Notification Service

---

# 2. Architecture

                    Internet
                        │
                Next.js Frontend
                        │
          ┌─────────────┴─────────────┐
          │                           │
     Authentication              FastAPI Backend
                                      │
        ┌──────────────┬──────────────┴─────────────┐
        │              │                            │
   PostgreSQL     AI Service                  File Storage
        │              │                            │
        └──────────────┴────────────────────────────┘

---

# 3. Frontend

Technology

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

Responsibilities

- Authentication
- Dashboard
- Medical Records
- Analytics
- Charts
- AI Chat

---

# 4. Backend

Technology

- FastAPI

Responsibilities

- REST APIs
- Authentication
- Business Logic
- Validation
- Notifications

---

# 5. AI Layer

Responsibilities

- Report Explanation
- AI Chat
- Health Insights
- Recommendation Engine

---

# 6. Database

Technology

- PostgreSQL

Stores

- Users
- Reports
- Medications
- Health Metrics
- Appointments
- Notifications

---

# 7. Security

- JWT Authentication
- Password Hashing
- HTTPS
- RBAC
- Input Validation

---

# 8. Deployment

Frontend → Vercel

Backend → Railway / Azure / AWS

Database → PostgreSQL

Storage → Cloud Storage

---

End of Document