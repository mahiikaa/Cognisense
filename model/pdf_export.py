from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv
import os
from datetime import datetime

def export_csv_to_pdf(csv_file="results/history.csv", pdf_file="results/fatigue_report.pdf"):
    if not os.path.exists(csv_file):
        print("No history to export.")
        return

    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Cognitive Fatigue Detection Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = height - 100
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            line = ", ".join(row)
            c.drawString(50, y, line)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50

    c.save()
    print(f"Report exported to {pdf_file}")
