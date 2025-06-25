from multimodal_fatigue_pipeline import MultimodalFatigueModel
from model.face_camera import detect_eye_closure
from model.voice_mic import capture_voice_input

# Helper function to read behavior input from file
def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

# Step 1: Capture inputs from all three modalities
input_data = {
    "face": detect_eye_closure(),                # Webcam-based eye state
    "voice": capture_voice_input(),              # Mic-based voice input
    "behavior": read_file("data/behavior.txt")   # Text-based behavior input
}

# Step 2: Initialize the model and make predictions
model = MultimodalFatigueModel()
results = model.predict(input_data)

# Step 3: Print and save predictions
print("Prediction result:", results)

with open("results/prediction_output.txt", "w") as file:
    for r in results:
        file.write(r + "\n")

print("Saved prediction to results/prediction_output.txt")





