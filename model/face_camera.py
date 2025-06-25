import cv2

def detect_eye_closure():
    print("Detecting eyes... Press 'q' to quit")

    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return "no face detected"

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        cv2.imshow("Eye Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Simulated output for now
    return "not fatigued"
