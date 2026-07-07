# Software Requirements Specification (SRS)

# HealthTwin AI X

Version: 1.0

Author: Agraj Nethra

Date: July 2026

---

# 1. Introduction

## 1.1 Purpose

This document defines the software requirements for HealthTwin AI X. It serves as the technical reference for development, testing, deployment, and maintenance.

---

## 1.2 Scope

HealthTwin AI X is an AI-powered Digital Health Twin platform that enables users to securely manage health records, upload medical reports, monitor wellness metrics, and receive AI-assisted health insights.

The system is intended for informational purposes only and does not replace professional medical advice.

---

# 2. Product Overview

The platform consists of:

- Patient Portal
- Doctor Portal
- Admin Portal
- AI Services
- Analytics Engine
- Secure Medical Vault

---

# 3. User Classes

## Patient

Can:

- Register
- Login
- Upload reports
- View dashboard
- Track medications
- Chat with AI
- View analytics

---

## Doctor

Can:

- View shared patient data
- Review uploaded reports
- Add consultation notes

---

## Administrator

Can:

- Manage users
- Monitor platform activity
- Review system logs

---

# 4. Functional Requirements

## Authentication

FR-001 User Registration

FR-002 Login

FR-003 Logout

FR-004 Forgot Password

FR-005 Email Verification

---

## Profile

FR-006 Edit Profile

FR-007 Upload Profile Picture

FR-008 Update Health Information

---

## Medical Reports

FR-009 Upload PDF

FR-010 Upload Image

FR-011 OCR Processing

FR-012 AI Report Explanation

FR-013 Report History

---

## Dashboard

FR-014 Health Score

FR-015 Timeline

FR-016 Charts

FR-017 Recent Activity

---

## Medication

FR-018 Add Medication

FR-019 Edit Medication

FR-020 Delete Medication

FR-021 Reminder

---

## AI

FR-022 AI Health Copilot

FR-023 AI Report Analysis

FR-024 Health Recommendations

FR-025 Explainable AI Response

---

# 5. Non-Functional Requirements

Security

- JWT Authentication
- Password Hashing
- HTTPS
- Role-Based Access Control

Performance

- Dashboard < 2 seconds
- API < 500 ms (typical requests)

Availability

- 99% uptime target

Scalability

- Support future microservices

Accessibility

- WCAG 2.1 principles

---

# 6. External Interfaces

Frontend

- Next.js

Backend

- FastAPI

Database

- PostgreSQL

AI

- LLM API
- RAG

---

# 7. Database Requirements

Store:

- Users
- Reports
- Medications
- Appointments
- Health Metrics
- Notifications

---

# 8. Security Requirements

- Password hashing
- JWT
- Input validation
- SQL injection protection
- XSS protection
- CSRF protection where applicable
- File upload validation

---

# 9. Constraints

- Internet required for AI features
- AI responses are informational
- User consent required for data sharing

---

# 10. Acceptance Criteria

A release is acceptable when:

- Authentication works
- Reports upload successfully
- AI explanations are returned
- Dashboard loads correctly
- APIs pass tests
- Documentation is updated

---

End of Document