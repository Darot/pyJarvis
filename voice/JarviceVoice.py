__author__ = 'daniel'

from gtts import gTTS
import os

class JarviceVoice:

    def __init__(self, language):
        self.__language = language

    def say(self, text):
        tts = gTTS(text=text, lang='de')
        tts.save("test.mp3")
        os.system('mpg321 test.mp3 &')



