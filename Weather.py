#import pandas as pd
import requests as ureq
from bs4 import BeautifulSoup as Soup
j = 0
pinfenomena = []
pinthermokrasia = []
pinora = []
url = "http://www.meteo.gr/cf.cfm?city_id=1"
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

page = ureq.get(url,headers=headers)
soup = Soup(page.content,'html.parser')

cont = soup.find_all(class_='innerTableCell temperature tempwidth')
time = soup.find_all(class_='innerTableCell fulltime')

for link in soup.find_all(class_='innerTableCell PhenomenaSpecialTableCell phenomenafull'):
    pinfenomena += [link.find(class_="CFicon")['title']]

for i in cont:
    pinthermokrasia.append(i.get_text().strip()) #prosthetei data sto telos tis listas olo to antikimeno pou zitame akrivos meta
    pinora.append(time[j].get_text().strip()) 
    j+=1

#finalpin = pd.DataFrame(      kanoume pinaka meso ton pandas
#    {
#        'Time': pinora,
#        'Temperature': pinthermokrasia,
#        'Fenomeno': pinfenomena
#    })

print(pinthermokrasia)
#finalpin.to_csv('Kairos.csv')  meso ton pandas kanei ton pinaka csv file


#.replace('n',' ') antikathista ola ta n me keno h me otidipote theloume se ena keimeno


# try:  #exception handler stin python
#    print("something")
# except:
#    pass