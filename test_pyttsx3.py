# test_pyttsx3.py
import pyttsx3

def test_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

test_speak("Testing pyttsx3 installation.")
