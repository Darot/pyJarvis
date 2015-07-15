__author__ = 'daniel'
import speech_recognition as sr
r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("Say something:")
    print("You said " + r.recognize(audio))
except LookupError:
    print("Sorry - I did not understand that!")