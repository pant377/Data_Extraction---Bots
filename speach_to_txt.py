import pyttsx3
import speech_recognition as sr
import re



def speak(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

#speak("this is a test beach ass nigga")

def listener():
    print("methodos")
    l = sr.Recognizer()
    print("after recognize")
    with sr.Microphone() as source:
        print("inside with")
        audio = l.listen(source)
        print("preee try")
        txt = ""
        print("pre try")
        try:
            print("mesa try")
            txt = l.recognize_google(audio)
            return txt.lower()  
        except Exception as e:
            print("Exception:",str(e))    

    return txt.lower()        

print(listener())