import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as microphone:
            recognizer.adjust_for_ambient_noise(microphone, duration=0.2)
            audio = recognizer.listen(microphone)

            text = recognizer.recognize_ibm(audio_data=audio)
            print(f"Recognized {text}")
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue