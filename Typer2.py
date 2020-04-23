from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
import time
lista = []
url = input("Enter url > ") 
driver = webdriver.Firefox(executable_path='/Users/pantelis/Downloads/geckodriver.exe')
driver.get(url)
time.sleep(2)
driver.find_element_by_class_name('qc-cmp-button').click()
driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a').click()
time.sleep(2)
res = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(res, 'html.parser')
texts = soup.find_all('span')
for i in texts:
    if('' == i.text)or('('==i.text[0])or(i.text[0].isnumeric())or(i.text[0]==':'):
        pass
    else:
        lista.append(i.text)
while (driver.find_element_by_class_name('txtInput').is_enabled()==False):
    time.sleep(0.1)
while (driver.find_element_by_class_name('txtInput').is_enabled()):
    n = lista.pop(0)
    if(len(n)>=5):
        newlist = [n[i:i+5] for i in range(0,len(n),5)]
        for j in newlist:
            print(j)
            for x in j:
                if(x != ''):
                    driver.find_element_by_class_name('txtInput').send_keys(x)
            time.sleep(0.53)
    else:        
        driver.find_element_by_class_name('txtInput').send_keys(n)
        print(n)
        time.sleep(0.6)