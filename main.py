import speech_recognition as sr
from speech_to_text import recognize_speech_from_mic
from text_to_speech import speak
from openai_integration import get_openai_response

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        print("Listening...")
        speech = recognize_speech_from_mic(recognizer, microphone)
        if not speech["success"]:
            print("Error: {}".format(speech["error"]))
            continue
        
        print("You said: {}".format(speech["transcription"]))
        if speech["transcription"].lower() == "exit":
            break

        response = get_openai_response(speech["transcription"])
        print("Assistant: {}".format(response))
        speak(response)

if __name__ == "__main__":
    main()
