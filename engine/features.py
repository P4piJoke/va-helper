import os
import sqlite3
import re
import webbrowser
from playsound import playsound
from engine.command import speak
from engine.config import *
import eel
import pywhatkit as kit

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

@eel.expose
def playAssistantSound():
    playsound(MUSIC_ROOT)

def executeQuery(query, app):
    cursor.execute(query, (app,))

    return cursor.fetchall()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, EMPTY)
    query = query.replace(OPEN, EMPTY)
    query.lower()

    app_name = query.strip()

    if app_name != EMPTY:

        try:
            results = executeQuery(SYS_COMMAND_QUERY, app_name)

            if len(results) != 0:
                speak(OPENING + query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                results = executeQuery(WEB_COMMAND_QUERY, app_name)
                
                if len(results) != 0:
                    speak(OPENING + query)
                    webbrowser.open(results[0][0])

                else:
                    speak(OPENING + query)
                    try:
                        os.system(START + SPACE + query)
                    except:
                        speak(NOT_FOUND)
        except:
            speak(SMTH_WENT_WRONG)

def playYoutube(query):
    search_term = extractYoutubeTerm(query)
    speak(PLAYING + search_term + ON_YOUTUBE)
    kit.playonyt(search_term)

def extractYoutubeTerm(query):
    match = re.search(PATTERN, query, re.IGNORECASE)

    return match.group(1) if match else None