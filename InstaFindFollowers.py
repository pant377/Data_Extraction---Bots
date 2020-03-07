from bs4 import BeautifulSoup as Bs
from selenium import webdriver
import time
user = ''
passw = ''
driver = webdriver.Chrome("/Users/pantelis/Downloads/chromedriver.exe")
url = 'https://www.instagram.com/accounts/login/'
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(user)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(passw)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
time.sleep(2)
driver.get('https://www.instagram.com/pantelis_.pap/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(2)
res = driver.execute_script("return document.documentElement.outerHTML")

page = Bs(res,'html.parser')
dive = page.find(class_="PZuss")
time.sleep(3)
for i in dive:
    fol = i.find(class_="wo9IH")
    print(fol)

driver.close()    