# 🧠 Fatigue Detection Web App

A Flask-based multimodal fatigue detection web application using **facial analysis**, **voice input**, and **behavioral data** to assess cognitive fatigue levels. Designed for healthcare monitoring, academic productivity, and mental well-being tracking.

---

## 🚀 Features

- 📸 Real-time **Eye Closure Detection** via webcam
- 🎤 **Voice Analysis** via microphone input
- 📊 **Behavioral Pattern Analysis** from uploaded CSV/TXT files
- 📈 Interactive **Trend Graph** and **Bar Chart**
- 🧾 **PDF/CSV Report Export**
- 🔐 **User Registration & Login** system with secure password hashing
- 🎨 Responsive **Bootstrap UI** for desktop and mobile

---

## 📁 Project Structure

📦 fatigue_project
├── 📂 model
│ ├── behavior_reader.py
│ ├── face_camera.py
│ ├── voice_mic.py
│ └── init.py
├── 📂 templates
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── goodbye.html
├── 📂 static
│ ├── trend.png
│ └── bar.png
├── 📂 uploads
│ └── (user-uploaded behavior files)
├── app.py # Main Flask app
├── run.py # Standalone test runner
├── README.md
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
├── .gitignore
├── haarcascade_eye.xml # OpenCV Haar cascade for eye detection
├── multimodal_fatigue_pipeline.py
├── users.json # User credentials (hashed)


---

## 🧪 Technologies Used

- Python 3
- Flask
- OpenCV
- PyAudio / Speech Recognition
- Pandas, Matplotlib
- FPDF
- Bootstrap 5 (UI)
- JSON, CSV
- Git & GitHub

---

## 📷 Screenshots

> _(Add your own screenshots here if available)_

---

## 🌐 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/mahiikaa/Cognisense.git
   cd Cognisense
