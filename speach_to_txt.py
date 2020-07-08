import pyttsx3
import requests
import speech_recognition as sr
import re
import time



def speak(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

#speak("this is a test beach ass nigga")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Speak Please ..")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio) 
        except Exception as e:
            print("Exception:",str(e))    

    return said.lower()        

print(get_audio())
time.sleep(3)