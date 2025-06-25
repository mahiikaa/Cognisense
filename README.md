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

![Screenshot 2025-06-25 173413](https://github.com/user-attachments/assets/69975169-3d54-4a76-87bb-48484476a2c3)
![Screenshot 2025-06-25 173442](https://github.com/user-attachments/assets/1565c32b-696c-4e2a-95a0-aa400567376a)
![Screenshot 2025-06-25 173521](https://github.com/user-attachments/assets/fe62af63-cda2-4bfe-b5be-e8934ea1eb6d)
![Screenshot 2025-06-25 173612](https://github.com/user-attachments/assets/1b1b703e-deb7-46fb-a2b6-77c96d566310)
![Screenshot 2025-06-25 173819](https://github.com/user-attachments/assets/7c305a19-32dc-4bee-b4a0-1a16369d99d5)
![Screenshot 2025-06-25 173839](https://github.com/user-attachments/assets/31bb9357-49c9-4ca8-a936-bb40d1adcfba)
![Screenshot 2025-06-25 173900](https://github.com/user-attachments/assets/ae80962b-3267-428a-8975-73627fd8aa2f)


---

## 🌐 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/mahiikaa/Cognisense.git
   cd Cognisense
