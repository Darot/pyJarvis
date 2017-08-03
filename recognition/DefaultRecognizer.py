__author__ = 'daniel'
import speech_recognition as sr
from voice.JarviceVoice import JarviceVoice

class DefaultRecognizer:

    def __init__(self):
        self.r = sr.Recognizer()
        self.r.dynamic_energy_threshold = True
        self.voice = JarviceVoice("de");

    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio, language="de").lower()
            print(text)
            self.listen()
        except sr.UnknownValueError:
            print("Didn't notice anything")
            self.listen()

