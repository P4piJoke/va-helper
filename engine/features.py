import os
import re
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import eel
import pywhatkit as kit

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening " +  query)
        os.system('start ' + query)
    else:
        speak("Not found")

def playYoutube(query):
    search_term = extractYoutubeTerm(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

def extractYoutubeTerm(query):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1) if match else None