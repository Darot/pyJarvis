__author__ = 'daniel'
from voice.JarviceVoice import JarviceVoice
from recognition.DefaultRecognizer import DefaultRecognizer

voice = JarviceVoice("de");
recognizer = DefaultRecognizer();

voice.say("GO!")

recognizer.listen();


