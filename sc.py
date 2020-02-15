from bs4 import BeautifulSoup as Bs
from selenium import webdriver as Wd
import requests as ur

url = 'https://apps.it.teithe.gr/announcements'
driver = Wd.Firefox('/home/pantelis/Downloads')
driver.get('https://apps.it.teithe.gr/announcements')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
page = Bs(res,'html.parser')
dive = page.find_all(id="row_5d95bfb507681a5af23187cb")
for i in dive:
    print(i.get_text().strip())
#print(page.prettify())
