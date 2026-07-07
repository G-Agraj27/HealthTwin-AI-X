# Entity Relationship Design (ERD)

# HealthTwin AI X

Version: 1.0

---

# Core Entities

## User

- id
- first_name
- last_name
- email
- password_hash
- role
- date_of_birth
- gender
- phone
- created_at
- updated_at

---

## MedicalReport

- id
- user_id
- title
- file_url
- report_type
- uploaded_at
- ai_summary
- status

---

## Medication

- id
- user_id
- medicine_name
- dosage
- frequency
- start_date
- end_date

---

## HealthMetric

- id
- user_id
- heart_rate
- blood_pressure
- weight
- height
- blood_glucose
- sleep_hours
- recorded_at

---

## Appointment

- id
- patient_id
- doctor_id
- appointment_date
- status
- notes

---

## Notification

- id
- user_id
- title
- message
- is_read
- created_at

---

# Relationships

User
 ├── MedicalReport (1:N)
 ├── Medication (1:N)
 ├── HealthMetric (1:N)
 ├── Notification (1:N)
 └── Appointment (1:N)

Doctor
 └── Appointment (1:N)