# 💧 AI Water Intake Tracker

An AI-powered hydration tracking system that allows users to log daily water intake, store data in a database, visualize trends, and receive intelligent feedback using an AI agent.

---

## 📌 Problem Statement

Many people struggle to consistently track their daily water consumption. Without proper tracking:

- Hydration goals are unclear
- Long-term intake patterns go unnoticed
- There is no feedback on whether intake is sufficient

This project solves that problem by providing:

- A structured water intake logging system
- AI-based feedback analysis
- Historical tracking with visual dashboards
- A backend API for structured data handling

---

## 🚀 Features

- ✅ Log daily water intake (in ml)
- ✅ AI-generated hydration feedback
- ✅ Store intake data in SQLite database
- ✅ View intake history
- ✅ Data visualization using charts
- ✅ REST API built with FastAPI
- ✅ Interactive dashboard using Streamlit

---

## 🏗️ Tech Stack & Skills Used

### 🔹 Backend
- FastAPI
- REST API Design
- Pydantic (Data Validation)
- Async Endpoints

### 🔹 Frontend
- Streamlit
- Interactive UI Design
- Data Visualization

### 🔹 Database
- SQLite
- SQL Queries
- CRUD Operations

### 🔹 AI & Logic
- Agent-based architecture
- Hydration analysis logic
- Modular backend design

### 🔹 Core Python Skills
- Object-Oriented Programming (OOP)
- Modular project structure
- Logging system
- Session management
- Error handling

---

## 📂 Project Structure

```
Daily-Water-Intake-Tracker/
│
├── src/
│   ├── api.py              # FastAPI backend
│   ├── aggent.py           # Water Intake AI Agent
│   ├── database.py         # SQLite operations
│   ├── logger.py           # Logging configuration
│
├── dashboard.py                  # Streamlit frontend
├── water_tracker.db        # SQLite database
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sagarsinghchauhan/Daily-Water-Intake-Tracker.git
cd Daily-Water-Intake-Tracker
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv water-tracker
```

Activate it:

**Windows**
```bash
water-tracker\Scripts\activate
```

**Mac/Linux**
```bash
source water-tracker/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How To Run The Project

## Step 1: Start FastAPI Backend (Run First)

```bash
uvicorn src.api:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

API documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## Step 2: Start Streamlit Frontend (Run Second)

Open a new terminal (keep FastAPI running) and run:

```bash
streamlit run dashboard.py
```

Streamlit dashboard will open automatically in your browser.

---

## 📊 API Endpoints

### 🔹 Log Water Intake

```
POST /log-intake
```

Example JSON body:

```json
{
  "user_id": "user_123",
  "intake_ml": 500
}
```

---

### 🔹 Get User Intake History

```
GET /history/{user_id}
```

---

## 🔮 Future Improvements

- Daily hydration goal tracking
- Weekly/monthly analytics
- User authentication
- AI-based personalized recommendations
- Cloud deployment (Render / Railway)
- Mobile-friendly interface

---

## 🎯 What This Project Demonstrates

- Full-stack integration (Frontend + Backend)
- AI-driven application architecture
- Database handling & persistence
- REST API development
- Real-world health tracking solution

---

## 👨‍💻 Author

Sagar Singh Chauhan |
ML Enginner@FoundersCart
