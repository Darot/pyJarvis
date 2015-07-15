__author__ = 'daniel'
import speech_recognition as sr
r = sr.Recognizer(language = "de-DE")
from voice.JarviceVoice import JarviceVoice
import time

voice = JarviceVoice("de");

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    order = r.recognize(audio).lower()
except LookupError:
    voice.say("Entschuldige! Das habe ich"
                     " nicht verstanden!")

if(order == "sprich mir nach"):
    voice.say("Soll ich dir nach sprechen?")

time.sleep(5)

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    order = r.recognize(audio).lower()
except LookupError:
    voice.say("Entschuldige! Das habe ich"
                     " nicht verstanden!")

if(order == "ja"):
    voice.say("ok!")

time.sleep(5)

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    text = r.recognize(audio).lower()
except LookupError:
    voice.say("Entschuldige! Das habe ich"
                     " nicht verstanden!")

voice.say(text)