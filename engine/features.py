import os
import sqlite3
import struct
import time
import webbrowser
from hugchat import hugchat
from playsound import playsound
import pvporcupine
import pyaudio
from engine.command import speak
from engine.config import *
import eel
import pywhatkit as kit

from engine.helper import extractYoutubeTerm


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

def hotword():
    print('hotword')
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=['jarvis','alexa']) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown('win')
                autogui.press('j')
                time.sleep(2)
                autogui.keyUp('win')
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path='engine\\cookies.json')
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response