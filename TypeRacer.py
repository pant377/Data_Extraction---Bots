from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
import time
import re
lista = []
url = input("Enter url > ") 
driver = webdriver.Firefox(executable_path='/Users/pantelis/Downloads/geckodriver.exe')
driver.get(url)
time.sleep(5)
driver.find_element_by_class_name('qc-cmp-button').click()
time.sleep(0.6)
driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a').click()
time.sleep(2.3)
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, 'html.parser')
texts = soup.find_all('span')[2:]
for i in texts:
    if('' == i.text)or('('==i.text[0]):
        print("pass: "+i.text)
        pass
    else:
        lista.append(i.text)
        print(i.text)
while (driver.find_element_by_class_name('txtInput').is_enabled()==False):
    time.sleep(0.1)
while (driver.find_element_by_class_name('txtInput').is_enabled()):
    n = lista.pop(0)
    if(len(n)>=5):
        frash = re.split("( )",n)
        for i in frash:
            #print(" pano "+i)
            driver.find_element_by_class_name('txtInput').send_keys(i)
            time.sleep(0.43)
    else:        
        #print(n)
        driver.find_element_by_class_name('txtInput').send_keys(n)
#auto me to countdown tha einai deutero panta [1]