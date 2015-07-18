__author__ = 'daniel'
from voice.JarviceVoice import JarviceVoice
from recognition.DefaultRecognizer import DefaultRecognizer

voice = JarviceVoice("de");
recognizer = DefaultRecognizer();

voice.say("Guten Tag ich bin Jarvis und hoere von jetzt an auf deine Befehle!")

recognizer.listen();


