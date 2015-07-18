__author__ = 'daniel'
import speech_recognition as sr
from voice.JarviceVoice import JarviceVoice

class DefaultRecognizer:

    def __init__(self):
        self.r = sr.Recognizer(language = "de-DE")
        self.r.dynamic_energy_threshold = True
        self.voice = JarviceVoice("de");

    def listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize(audio).lower()
            if(text == "leck mich am arsch"):
                self.voice.say("Alles Klar! Hose runter!")
        except LookupError:
            self.voice.say("Entschuldige! Das habe ich"
                     " nicht verstanden!")
            self.listen()

