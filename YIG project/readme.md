WELCOME TO THE YIG PROJECT


```markdown
# 🎬 YouTube Video Information Getter

A responsive, asynchronous Flask web application that extracts and displays YouTube video metadata (thumbnails, statistics, channel info, and descriptions) featuring a real-time ChatGPT-style typewriter text effect and adaptive UI transitions.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![YouTube API](https://img.shields.io/badge/YouTube_Data_API-v3-FF0000?style=for-the-badge&logo=youtube&logoColor=white)

---

## 📌 Milestone & Learning Note

> **Developer Note:** I built this project on my **6th day of learning Flask**. It serves as a practical milestone showcasing rapid hands-on execution with backend API integration, asynchronous frontend requests, and UI streaming.
>
> 🚀 **Roadmap:** This is v1.0 of the project. As I advance my backend development skill set (database integrations, caching, authentication, and architectural design patterns), I will continuously refine, refactor, and expand this application in upcoming versions.

---

## 🌟 Key Features

* **Multi-Format URL Parsing:** Supports standard watch URLs (`watch?v=`), shortened links (`youtu.be/`), and YouTube Shorts (`/shorts/`).
* **Dynamic Media Rendering:** Displays high-resolution video thumbnails with custom rounded corners and subtle shadow elevations.
* **Typing Stream Effect:** Simulates a ChatGPT-like character-by-character output stream for enhanced visual engagement.
* **Auto-Scrolling Card:** Dynamic result container with auto-scrolling capabilities and tailored webkit scrollbars for detailed descriptions.
* **Debounced Input & Animations:** Smooth CSS keyframes and JavaScript timing triggers that manage element fading and state updates.

---

## 🛠️ Tech Stack & Architecture

* **Backend:** Python, Flask, `google-api-python-client` (YouTube Data API v3), `python-dotenv`
* **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3 (CSS Variables, Flexbox, Custom Webkit Scrollbars)
* **Configuration:** Environment variable isolation for API security

---

## 📂 Project Structure

```text
youtube-info-getter/
│
├── static/
│   ├── css/
│   │   └── index.css          # Custom styling, animations, and scrollbars
│   └── js/
│       └── index.js           # Async API fetching, DOM stream effect, UI state logic
│
├── templates/
│   ├── base.html              # HTML5 base layout structure
│   └── index.html             # Application viewport and card containers
│
├── .env.example               # Template for environment key isolation
├── .gitignore                 # Excluded environments and sensitive data
├── app.py                     # Flask backend routing & YouTube API endpoint
├── README.md                  # Comprehensive project documentation
└── requirements.txt           # Python dependency declarations

```

---

## 🚦 Getting Started

### Prerequisites

* **Python 3.10+** installed on your machine.
* A valid **YouTube Data API v3 Key** obtained from the [Google Cloud Console](https://console.cloud.google.com/).

### Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/youtube-info-getter.git](https://github.com/your-username/youtube-info-getter.git)
cd youtube-info-getter

```


2. **Create and activate a virtual environment:**
* **Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


* **Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate

```




3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Environment Variables:**
Create a `.env` file in the project root directory by copying `.env.example`:
```bash
cp .env.example .env

```


Add your YouTube API Key inside `.env`:
```env
YOUTUBE_API_KEY=your_actual_youtube_api_key_here

```


5. **Run the Flask application:**
```bash
python app.py

```


6. **Open in browser:**
Navigate to `http://127.0.0.1:5000` to interact with the application.

---

## 🔑 API Security Notice

This repository strictly enforces API key safety using environment variables via `python-dotenv`. Production deployments must always pass runtime environment values rather than hardcoding credentials into source code.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

```

<FollowUp label="Loyiha kelajakda (v2.0 da) qanday yangi xususiyatlar bilan boyitilishi mumkinligi bo'yicha g'oyalar xohlaysizmi?" query="Ushbu loyihani v2.0 va v3.0 versiyalarida rivojlantirish uchun qanday texnik va funksional g'oyalar bersa bo'ladi?"/>

```
