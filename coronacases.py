from bs4 import BeautifulSoup as bs
import requests
from decimal import Decimal

soup = bs(requests.get('https://www.worldometers.info/coronavirus/').content,'html.parser')
cases = soup.findAll(id='maincounter-wrap')
infected = cases[0].find('span').text.replace(",",".")
deths = cases[1].find('span').text.replace(",",".")   #na thimase oti se auto pou vrikes mporeis na kaneis find
persent = (float(deths)/float(infected))*100
print("Cases: "+infected+" |Deaths: "+deths+" |Persentage of deaths: "+str(persent)[0:4]+" %")


