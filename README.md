# Healthcare Backend System  
Backend Developer Intern Assignment – WhatBytes  

## 📖 Overview

This project is a healthcare backend system built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.

The system allows users to:

- Register and log in using JWT authentication
- Manage patients
- Manage doctors
- Assign doctors to patients
- Secure all endpoints using authentication

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- PostgreSQL
- djangorestframework-simplejwt (JWT Authentication)
- python-dotenv (Environment Variables)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KhushneetSingh/WhatByte_Backend.git
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE healthcare_db;
```

---

### 5️⃣ Create `.env` File

Create a `.env` file in the root directory and add:

```
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 6️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

This project uses **JWT Authentication**.

### Register User
```
POST /api/auth/register/
```

### Login
```
POST /api/auth/login/
```

Response:
```
{
  "refresh": "...",
  "access": "..."
}
```

Use access token in headers:

```
Authorization: Bearer <access_token>
```

---

## 👤 Patient APIs

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/patients/ | Create patient |
| GET | /api/patients/ | Get all patients of logged-in user |
| GET | /api/patients/<id>/ | Get patient details |
| PUT | /api/patients/<id>/ | Update patient |
| DELETE | /api/patients/<id>/ | Delete patient |

---

## 👨‍⚕️ Doctor APIs

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/doctors/ | Create doctor |
| GET | /api/doctors/ | Get all doctors |
| GET | /api/doctors/<id>/ | Get doctor details |
| PUT | /api/doctors/<id>/ | Update doctor |
| DELETE | /api/doctors/<id>/ | Delete doctor |

---

## 🔗 Patient-Doctor Mapping APIs

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/mappings/ | Assign doctor to patient |
| GET | /api/mappings/ | Get all mappings |
| GET | /api/mappings/patient/<patient_id>/ | Get doctors assigned to patient |
| DELETE | /api/mappings/<id>/ | Remove doctor from patient |

---

## 🔒 Security Features

- JWT-based authentication
- Authenticated access to patient endpoints
- User-specific patient filtering
- Environment variable usage for sensitive credentials
- Duplicate mapping prevention
- PostgreSQL relational database

---

## ✅ Assignment Requirements Covered

- Django Framework
- Django REST Framework APIs
- PostgreSQL Database
- JWT Authentication
- Secure endpoints
- RESTful API design
- Environment variables for configuration
- ORM-based modeling