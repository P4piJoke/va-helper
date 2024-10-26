import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')
        print("L")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 10)

    try:
        print("R")
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()