# 🐦 Django Tweet App

A microblogging platform (like a mini Twitter clone) built with **Django** and **Django REST Framework**, allowing users to register, log in, post tweets, upload images, and interact with a RESTful API.

---

## 🚀 Features

- 🔐 User Registration & Authentication
- ✍️ Create, Edit, and Delete Tweets
- 🖼️ Tweet with Images (media upload)
- 🧠 Token-based Authentication (via DRF)
- 📬 API Access via Postman or cURL
- 🗂️ Admin panel to manage tweets and users

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates (HTML/CSS)
- **Database**: SQLite (default)
- **Authentication**: Session-based + Token (DRF)
- **Tools**: Postman, cURL, Git, GitHub

---

## 📸 Screenshots

> *(Add screenshots of tweet list, tweet form, API test if available)*

---

## 📦 API Endpoints

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/tweet/tweets/`        | List all tweets          |
| POST   | `/tweet/tweets/`        | Create a new tweet       |
| GET    | `/tweet/tweets/<id>/`   | Retrieve a tweet         |
| PUT    | `/tweet/tweets/<id>/`   | Update a tweet           |
| DELETE | `/tweet/tweets/<id>/`   | Delete a tweet           |
| POST   | `/tweet/api-token-auth/`| Get Auth Token           |

🔐 Use `Authorization: Token <your_token>` in headers for authenticated requests.

---

## 🧪 Testing with cURL

```bash
# Authenticate
curl -X POST http://127.0.0.1:8000/tweet/api-token-auth/ \
  -d "username=yourusername&password=yourpassword"

# Create a tweet
curl -X POST http://127.0.0.1:8000/tweet/tweets/ \
  -H "Authorization: Token your_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from cURL!"}'


🧰 Setup Instructions

# Clone the repo
git clone https://github.com/Anshika0804/Django-tweet-app.git
cd Django-tweet-app

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
