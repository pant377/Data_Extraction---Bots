from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pyttsx3
import requests
import speech_recognition as sr
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
    return said        

countrylist,countryc,dpcountry= [] , [], []
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
page = requests.get("https://www.worldometers.info/coronavirus/", headers=headers)
soup = bs(page.content,'html.parser')
cases = soup.findAll(id='maincounter-wrap')
infected = cases[0].find('span').text.replace(",","")
deths = cases[1].find('span').text.replace(",","") 
table = soup.find(id="main_table_countries_today")
countrys = table.find_all(class_="mt_a")

for i in countrys:   
   try:
      txt = i.text
      cpc = i.next.next.next.text
      dpc = i.next.next.next.next.next.next.next.next.text
      countrylist.append(txt)
      countryc.append(cpc)
      dpcountry.append(dpc)
   except:
      txt = i.text
      cpc = i.next.next.next.text
      dpc = i.next.next.next.next.next.next.next.next.next.text
      countrylist.append(txt)
      countryc.append(cpc)
      dpcountry.append(dpc)   
tablecsv = pd.DataFrame({'Country':countrylist,
                         'Cases':countryc,
                         'Deaths':dpcountry})                           
persent = (float(deths)/float(infected))*100
totalcases = "Cases: "+infected+" |Deaths: "+deths+" |Persentage of deaths: "+str(persent)[0:5]+" %"
speak("Give me anorder ")
while True:
   inputcountry = get_audio()
   print(inputcountry)
   try:
      if ('All' in inputcountry) :
         print(totalcases)
      elif ('CSV' in inputcountry) :
         tablecsv.to_csv("C:/Users/pantelis/Desktop/file.csv",sep=',',index=False)   
      elif ('manual' in inputcountry):
         country = input("Give me Country name -> ")
         coun = tablecsv.loc[tablecsv['Country'] == country]
         print(coun)
      elif ('exit'in inputcountry)or('close'in inputcountry):
         break
      else:   
         for i in countrylist:
            if (i in inputcountry):
               coun = tablecsv.loc[tablecsv['Country'] == i]
               print(coun)
   except:
      print("Error posibly in country name ...")