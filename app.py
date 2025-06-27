from flask import Flask, render_template, request, send_file, redirect, url_for, jsonify
from model.face_camera import detect_eye_closure_from_image, detect_eye_closure
from model.voice_mic import capture_voice_input
from model.behavior_reader import read_behavior_info
from multimodal_fatigue_pipeline import MultimodalFatigueModel
from fpdf import FPDF
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
import json

app = Flask(__name__)
model = MultimodalFatigueModel()

os.makedirs("results", exist_ok=True)
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

behavior_file_path = ""

def log_prediction_to_csv(mode, prediction):
    filename = "results/history.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "mode", "prediction"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), mode, prediction])

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        if username in users:
            return "Username already exists!"

        users[username] = password
        with open("users.json", "w") as f:
            json.dump(users, f)

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.json", "r") as f:
            users = json.load(f)

        if username in users and check_password_hash(users[username], password):
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def dashboard():
    global behavior_file_path
    result = ""
    graph = None
    bar = None

    if request.method == "POST":
        if "upload_behavior" in request.form:
            uploaded_file = request.files["behavior_file"]
            if uploaded_file:
                behavior_file_path = os.path.join("uploads", uploaded_file.filename)
                uploaded_file.save(behavior_file_path)

        elif "upload_face_image" in request.form:
            image_file = request.files["face_image"]
            if image_file:
                img_path = os.path.join("uploads", image_file.filename)
                image_file.save(img_path)
                result = detect_eye_closure_from_image(img_path)
                log_prediction_to_csv("face-image", result)

        elif "start_detection" in request.form:
            face = detect_eye_closure()
            voice = capture_voice_input()
            behavior = read_behavior_info(behavior_file_path)

            log_prediction_to_csv("face", face)
            log_prediction_to_csv("voice", voice)
            log_prediction_to_csv("behavior", behavior)

            result = model.predict(face, voice, behavior)

        elif "export_pdf" in request.form:
            df = pd.read_csv("results/history.csv")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_path = f"results/fatigue_report_{timestamp}.pdf"

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Fatigue Detection Report", ln=True, align='C')
            pdf.ln(10)

            for _, row in df.iterrows():
                line = f"{row['timestamp']} | {row['mode']} | {row['prediction']}"
                pdf.cell(200, 10, txt=line, ln=True)

            pdf.output(pdf_path)
            return send_file(pdf_path, as_attachment=True)

        elif "export_csv" in request.form:
            df = pd.read_csv("results/history.csv")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_path = f"results/fatigue_data_{timestamp}.csv"
            df.to_csv(csv_path, index=False)
            return send_file(csv_path, as_attachment=True)

        elif "trend_graph" in request.form:
            df = pd.read_csv("results/history.csv", parse_dates=["timestamp"])
            df["hour"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M")
            trend = df[df["prediction"].str.contains("fatigued")].groupby("hour").size().reset_index(name="count")

            plt.figure(figsize=(8, 4))
            plt.plot(trend["hour"], trend["count"], marker="o", color="red")
            plt.xticks(rotation=45)
            plt.tight_layout()
            graph_path = "static/trend.png"
            plt.savefig(graph_path)
            graph = graph_path

        elif "bar_graph" in request.form:
            df = pd.read_csv("results/history.csv")
            counts = df["prediction"].value_counts()

            plt.figure(figsize=(5, 4))
            counts.plot(kind="bar", color=["green", "red", "orange"])
            plt.title("Prediction Summary")
            plt.tight_layout()
            bar_path = "static/bar.png"
            plt.savefig(bar_path)
            bar = bar_path

    return render_template("index.html", result=result, graph=graph, bar=bar)

@app.route("/webcam")
def webcam_page():
    return render_template("webcam.html")

@app.route("/exit")
def exit_app():
    return render_template("goodbye.html")

if __name__ == "__main__":
    app.run(debug=True)
