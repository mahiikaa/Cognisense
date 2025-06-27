import cv2

# 👁️ Function for detecting eye closure from an uploaded image (used in web version)
def detect_eye_closure_from_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return "not fatigued (face)"  # Can't read image
    # You can add actual logic here, this is a placeholder
    return "fatigued (face)"  # Simulated result

# 👁️ Existing function for webcam detection (keep this if you're using desktop app too)
def detect_eye_closure():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "not fatigued (face)"  # Camera not available

    # Simple logic (replace with real detection if needed)
    ret, frame = cap.read()
    cap.release()
    if ret:
        return "fatigued (face)"  # Placeholder
    else:
        return "not fatigued (face)"
