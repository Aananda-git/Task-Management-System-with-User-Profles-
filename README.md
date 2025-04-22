# Task-Management-System-with-User-Profles

A full-stack Task Management System built with **Django REST Framework** for the backend and **Vue 3 with TypeScript** for the frontend. The system allows users to manage user profiles and tasks with authentication and real-time interaction.

---

## 🔗 Project URLs

- **Backend API Docs (Swagger):** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Django Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Frontend Vue App:** [http://localhost:5173/](http://localhost:5173/)

> **Login Credentials**  
> - **Username:** `Test`  
> - **Password:** `Test@123`

---

## ⚙️ Setup Instructions

### 📦 Backend (Django Rest Framework)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aananda-git/Task-Management-System-with-User-Profles-.git
   cd backend 

2. **Create a virtual environment & install dependencies**
    ```bash
    python -m venv env
    source env\Scripts\activate

3. **Apply migrations**
    ```bash
    python manage.py migrate
    
4. **Run the development server**
    ```bash
    python manage.py runserver

5. **Access**
  
    - Admin Panel: http://127.0.0.1:8000/admin/

    - API Docs: http://127.0.0.1:8000/swagger/


### 🌐 Frontend - Vue 3 + TypeScript

1. **Navigate, install dependencies and runserver**
    ```bash
    cd frontend
    npm install
    npm run dev

2. **Access**

    vue-app: http://localhost:5173/

3. **Login Credentials**
    ```
    username: Test
    Password: Test@123