from bs4 import BeautifulSoup as bs
import requests
from lxml import html
import time

soup = bs(requests.get('https://www.worldometers.info/coronavirus/').content,'html.parser')
 #tree = html.fromstring(requests.get('https://www.worldometers.info/coronavirus/').content)
cases = soup.findAll(id='maincounter-wrap')
infected = cases[0].find('span').text.replace(",","")
deths = cases[1].find('span').text.replace(",","") #na thimase oti se auto pou vrikes mporeis na kaneis find
#withxpath = tree.xpath('//*[@id="maincounter-wrap"]/div/span/text()')
#for i in withxpath:
   # number = i.replace(' ','').replace(',','.') 
   # print(float(number))
persent = (float(deths)/float(infected))*100
print("Cases: "+infected+" |Deaths: "+deths+" |Persentage of deaths: "+str(persent)[0:5]+" %")
time.sleep(10)