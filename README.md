# 📦 Webhook Flask App

A lightweight Flask application that receives GitHub webhook events (`push`, `pull_request`, and simulated `merge`) and stores them in a MongoDB database. The frontend updates every 15 seconds to display the latest activity.

---

## 🚀 Live Demo

Hosted on: [https://techstax-webhook-repo.onrender.com/](https://techstax-webhook-repo.onrender.com/)

> Replace with your actual Render/hosted URL

---

## 🧰 Features

- ✅ Listens to GitHub Webhooks (`push`, `pull_request`, `merge`)
- ✅ Parses payload and stores structured entries in MongoDB
- ✅ Frontend auto-refreshes every 15 seconds with latest activity
- ✅ Displays:
  - Author
  - Branches
  - Action type
  - Commit/PR request ID
  - Timestamp (formatted in IST)

---

## 📁 Project Structure
├── app.py # Flask backend with webhook receiver
├── templates/
│ └── index.html # Auto-refresh frontend
├── requirements.txt # Python dependencies
├── .env # MongoDB connection string
└── README.md # This file

