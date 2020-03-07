from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup

url = 'https://www.skroutz.gr/s/424179/Corsair-Vengeance-16GB-DDR3-1600MHz-CMZ16GX3M2A1600C10.html'
urlClient = ureq(url)
page = urlClient.read()
urlClient.close()
soup = Soup(page, 'html.parser')
shops = soup.findAll(class_="cf card js-product-card")

for i in shops:
    dive = i.find(class_="price")
    shop = i.find(class_="shop-name").string
    price = dive.div.a.string
    print("\nTimi : ", price," Magazi : ",shop)
