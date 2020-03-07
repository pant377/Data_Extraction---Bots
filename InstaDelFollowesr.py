from bs4 import BeautifulSoup
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
time.sleep(1)
driver.get('https://www.instagram.com/pantelis_.pap/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(1)

for f in range(1, 3):
    xpath = '/html/body/div[3]/div/div[2]/ul/div/li[%d]/div/div[3]/button' % (f)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
   
   