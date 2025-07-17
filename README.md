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
- **Search Tweets by Username or Content**

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
| Database     | PostgreSQL                      |
| Auth         | Django Sessions & DRF Tokens    |
| Tools        | Git, GitHub, Postman, cURL      |

---

## 📦 API Endpoints

### 🔁 Tweets
| Method | Endpoint                             | Description                           |
|--------|--------------------------------------|---------------------------------------|
| GET    | `/tweet/tweets/`                     | List all tweets                       |
| POST   | `/tweet/tweets/`                     | Create a tweet                        |
| GET    | `/tweet/tweets/<id>/`                | Get tweet details                     |
| PUT    | `/tweet/tweets/<id>/`                | Update a tweet                        |
| DELETE | `/tweet/tweets/<id>/`                | Delete a tweet                        |
| GET    | `/tweet/tweets/search/?q=<keyword>`  | Search tweets by username or content  |

### 🔐 Authentication
| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| POST   | `/tweet/api-token-auth/`  | Get auth token (DRF)               |

### 💬 Comments
| Method | Endpoint                             | Description                    |
|--------|--------------------------------------|--------------------------------|
| POST   | `/tweet/tweets/<id>/comments/`       | Add comment to a tweet         |
| GET    | `/tweet/tweets/<id>/comments/`       | Get all comments on a tweet    |
| PUT    | `/tweet/comments/<comment_id>/`      | Edit a comment                 |
| DELETE | `/tweet/comments/<comment_id>/`      | Delete a comment               |

### 👤 User Profiles
| Method | Endpoint                        | Description                    |
|--------|---------------------------------|--------------------------------|
| GET    | `/profile/<username>/`          | View a user's profile          |
| PUT    | `/profile/edit/`                | Edit logged-in user's profile  |

---
