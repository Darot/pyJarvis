__author__ = 'daniel'

from gtts import gTTS
import pygame

class JarviceVoice:

    def __init__(self, language):
        self.__language = language

    def say(self, text):
        tts = gTTS(text=text, lang='de')
        tts.save("test.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("test.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue




