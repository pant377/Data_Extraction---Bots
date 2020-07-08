import pyttsx3
import requests
import speech_recognition as sr
import re
import time

def speak(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Speak Please ..")
        audio = r.listen(source, timeout=5)
        said = ""
        try:
            said = r.recognize_google(audio) 
        except Exception as e:
            print("Exception:",str(e))    
    return said.lower()        
print(get_audio())