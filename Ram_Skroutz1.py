from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import smtplib
import time
url = 'https://www.skroutz.gr/c/56/mnhmes-pc-ram/f/46394_46403_46405_583121/DDR3-Desktop-2-modules-16GB.html'

    # anigei to connection kai pernei tin selida
def check():
    uClient = ureq(url)
    page = uClient.read()
    uClient.close()
    # html parser
    soup1 = Soup(page, 'html.parser')
    items = soup1.findAll("li", {"class":"cf card"})
    
    for i in items:
        brand = i.h2.a["title"]
        f = i.find("div", {"class":"price react-component"})
        price = f.div.a.string
        print("\nRam Maker : ", brand,"  \nPrice : ", price)

check()
