import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    
    engine.runAndWait()

def takeCommand():
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
        time.sleep(2)
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if (message == 1):
        query = takeCommand()
        print(query)
    else:
        query = message

    try:
        if 'open' in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)
        else:
            print("not run")

    except Exception as e:
        print('Error')
        
    eel.ShowHood()