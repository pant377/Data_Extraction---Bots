from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
countrylist = []
countryc = []
dpcountry = []
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
page = requests.get("https://www.worldometers.info/coronavirus/", headers=headers)
soup = bs(page.content,'html.parser')
cases = soup.findAll(id='maincounter-wrap')
infected = cases[0].find('span').text.replace(",","")
deths = cases[1].find('span').text.replace(",","") 
table = soup.find(id="main_table_countries_today")
countrys = table.find_all((("a", {"class":"mt_a"})))
for i in countrys:
   try:
      txt = i.text
      cpc = i.next.next.next.text
      dpc = i.next.next.next.next.next.next.next.next.text
      print(txt," -- ",cpc," -- ",dpc)
      countrylist.append(txt)
      countryc.append(cpc)
      dpcountry.append(dpc)
   except:
      print("")   
tablecsv = pd.DataFrame({'Country':countrylist[0:],
                         'Cases':countryc[0:],
                         'Deaths':dpcountry[0:]})      

tablecsv.to_csv("C:/Users/pantelis/Desktop/file.csv")                         
                         
persent = (float(deths)/float(infected))*100
print("Cases: "+infected+" |Deaths: "+deths+" |Persentage of deaths: "+str(persent)[0:5]+" %")
#time.sleep(10)
