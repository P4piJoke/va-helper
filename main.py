import os

import eel

from engine.features import *
from engine.command import *
from engine.auth import recognize

def start():
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        eel.hideLoader()
        speak('Ready for Face Authentication')
        flag = recognize.AuthenticateFace()
        
        if (flag == 1):
            eel.hideFaceAuth()

            speak('Authentication is sucessful')
            eel.hideFaceAuthSuccess()

            speak('You are welcome, how can I help you?')
            eel.hideStart()

            playAssistantSound()
        else:
            speak('Authentication is failed')

    os.system('start msedge.exe -app="http:/localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)

