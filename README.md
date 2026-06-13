# Django User Authentication System

A Django User Authentication System built using Django's built-in authentication framework. This project demonstrates user registration, login, logout, profile management, password reset, forgot password functionality, profile updates, session handling, and route protection using Django Authentication.

---

## Features

- User Registration
- User Login
- User Logout
- User Profile Page
- Edit Profile
- Reset Password
- Forgot Password
- Session Authentication
- Django Messages Framework
- Protected Routes using Login Required Decorator
- Responsive UI Design
- Professional About Page

---

## Technologies Used

- Python 3
- Django 5
- SQLite3
- HTML5
- CSS3

---

## Project Structure

```text
myproject/
│
├── authuser/
│   ├── migrations/
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── reset_pasw.html
│   │   ├── forget_pasw.html
│   │   ├── update.html
│   │   └── about.html
│   │
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── main.html
│   └── nav.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Authentication Flow

### Registration

Users can create a new account using:

- First Name
- Last Name
- Email
- Username
- Password

**Validation**

- Username must be unique
- Password is securely hashed before storing

---

### Login

Users can login using:

- Username
- Password

Django Authentication validates credentials before creating a session.

---

### Profile

After login, users can view:

- Username
- First Name
- Last Name
- Email

---

### Edit Profile

Users can update:

- First Name
- Last Name
- Email

Username remains visible and cannot be modified.

---

### Password Reset

#### Step 1

Verify Old Password

#### Step 2

Enter New Password

#### Step 3

Confirm New Password

**Validation**

- Old password must be correct
- New password and confirm password must match
- New password cannot be the same as old password

---

### Forgot Password

#### Step 1

Verify Username

#### Step 2

Enter New Password

#### Step 3

Confirm New Password

**Validation**

- Username must exist
- New password and confirm password must match
- Password is securely hashed before saving

---

### Logout

Logout destroys the active user session and redirects users to the login page.

---

## About Page

The application includes a professional About Page featuring:

- Project Overview
- Task Management Features
- Technology Stack
- Statistics Cards
- Developer Information

---

## Concepts Covered

- Django Authentication
- User Sessions
- Login Required Decorator
- Password Hashing
- Password Validation
- Forgot Password Workflow
- Profile Update Functionality
- Django Messages Framework
- Template Inheritance
- URL Routing
- Static Files Handling

---

## Database

This project uses SQLite3 as the default database.

### Important Tables

- auth_user
- django_session
- django_admin_log
- django_content_type
- django_migrations

---

## Installation

### Clone Repository

```bash
git clone https://github.com/nikunjhadiya/django-user-authentication.git
```

### Move Into Project Directory

```bash
cd django-user-authentication
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Virtual Environment

**Windows**

```bash
myenv\Scripts\activate
```

**Linux / Mac**

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

### Open Browser

```text
http://127.0.0.1:8000/
```

---

## Future Enhancements

- Upload Profile Picture
- Email Verification
- Forgot Password via Email OTP
- Todo CRUD Operations
- Admin Dashboard
- User Roles and Permissions
- Account Activation via Email

---

## Repository Topics

```text
django
python
authentication
login-system
user-management
django-authentication
sqlite
web-development
todo-app
```

---

## Author

### Nikunj Hadiya

**Python Developer | Django Developer**

Portfolio:
https://nikunjhadiya.netlify.app/

LinkedIn:
https://www.linkedin.com/in/nikunjhadiya/

GitHub:
https://github.com/nikunjhadiya/

---

⭐ If you found this project useful, consider giving it a star on GitHub.
