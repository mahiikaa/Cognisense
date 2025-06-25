import speech_recognition as sr

def capture_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Please speak now... (fatigued or normal voice)")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Speech recognition service error.")
        return ""
