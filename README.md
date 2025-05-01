
---

# 🏫 CORE — Django REST API for South African Schools Data

This is the **backend Django REST API** that powers the school data functionality for the [Admission Web App](https://github.com/Matidza/School-Front). It handles the **storage, retrieval, and management of South African school profiles**, which are created when a school signs up via the frontend hosted at [admission-schools.up.railway.app](https://admission-schools.up.railway.app/).

---

## 📌 What This API Does

- 🏫 **Stores School Profiles**  
  When a school creates an account, its profile (name, location, contact info, type, etc.) is saved here.

- 🌍 **Exposes School Data to Frontend**  
  Enables public or authenticated users to fetch school information via structured REST endpoints.

- 🔐 **Admin Access**  
  Admins can view, update, or delete school records if necessary.

---

## 🛠️ Tech Stack

- **Framework**: Django & Django REST Framework  
- **Database**: PostgreSQL or SQLite (for local dev)  
- **CORS**: Configured for React frontend access  
- **Hosted On**: Railway (or relevant backend hosting platform)

---

## 🔗 Frontend Link

This API is connected to the frontend repository:  
📦 [https://github.com/Matidza/School-Front](https://github.com/Matidza/School-Front)

And is used in production at:  
🌐 [https://admission-schools.up.railway.app](https://admission-schools.up.railway.app)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Matidza/CORE.git
cd CORE
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Migrate Database

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Start the Server

```bash
python manage.py runserver
```

API will be available at:  
`http://127.0.0.1:8000/api/`

---

## 📂 Example API Endpoints

| Endpoint               | Description                  |
|------------------------|------------------------------|
| `/api/schools/`        | List all registered schools  |
| `/api/schools/<id>/`   | Retrieve a specific school   |
| `/api/schools/create/` | Add a new school (POST)      |

> Authentication may be required for POST, PUT, DELETE actions (depending on your setup).

---

## ⚙️ Environment Setup

Create a `.env` file with the following (if using `django-environ`):

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_connection_string
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🔐 CORS Configuration

Make sure to allow requests from your frontend domain (e.g., `http://localhost:3000` or your Railway frontend URL).

---

## ✅ Deployment Tips

- Set `DEBUG=False` in production
- Use Gunicorn + Nginx for server setup
- Host PostgreSQL on a managed service (e.g., Railway or Supabase)

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for full details.

---
