from bs4 import BeautifulSoup as bs
import requests
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
inputcountry = input("Give me a country (type ALL or country name (start with capitall letter except USA and UK)) OR (you can export it in csv just type csv) > ")
if inputcountry == 'ALL':
   print(totalcases)
elif inputcountry == 'csv':
   tablecsv.to_csv("C:/Users/pantelis/Desktop/file.csv",sep=',',index=False)   
else:   
   print(tablecsv.loc[tablecsv['Country']== inputcountry])