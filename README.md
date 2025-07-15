# 🐦 Django Tweet App

A microblogging platform (mini Twitter clone) built with **Django** and **Django REST Framework**. Users can register, post tweets with images, comment on tweets, manage their profiles, and interact through RESTful APIs.

---

## 🚀 Features

### 🔐 Authentication
- User Registration & Login (Session-based)
- Token-based Authentication for APIs (DRF)

### 🐥 Tweets
- Create, Edit, Delete Tweets
- Upload images with tweets
- View all tweets
- See only your own tweets

### 💬 Comments
- Add, Edit, and Delete Comments on Tweets
- Comment management on a separate page to reduce clutter

### 🙋 User Profiles
- Each user has a profile (auto-created on signup)
- Fields: Full Name, Bio, Date of Birth, Profile Picture
- View Profile Page
- Edit Profile Page with file upload

### 📬 Admin Panel
- Full control over users, tweets, comments, and profiles

---

## 🛠️ Tech Stack

| Layer        | Tools/Frameworks                |
|--------------|---------------------------------|
| Backend      | Django, Django REST Framework   |
| Frontend     | Django Templates (HTML, CSS)    |
| Database     | SQLite (default)                |
| Auth         | Django Sessions & DRF Tokens    |
| Tools        | Git, GitHub, Postman, cURL      |

---

## 📦 API Endpoints

| Method | Endpoint                    | Description               |
|--------|-----------------------------|---------------------------|
| GET    | `/tweet/tweets/`            | List all tweets           |
| POST   | `/tweet/tweets/`            | Create a tweet            |
| GET    | `/tweet/tweets/<id>/`       | Get tweet details         |
| PUT    | `/tweet/tweets/<id>/`       | Update a tweet            |
| DELETE | `/tweet/tweets/<id>/`       | Delete a tweet            |
| POST   | `/tweet/api-token-auth/`    | Get auth token (DRF)      |

**🔐 Auth Note**: Use this header for API access:
```http
Authorization: Token your_token_here
