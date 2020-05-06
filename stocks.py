from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from lxml import html
import time

driver = webdriver.Firefox(executable_path='/Users/pantelis/Downloads/geckodriver.exe')
driver.get("https://www.investing.com/")
time.sleep(3)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Got it"))
    )
    element.click()
except:
    print("Nothing still ..")
#button = driver.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[2]/div[2]/a[1]').click()
                                    
#driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/form/button[1]').click()
time.sleep(1)
res = driver.execute_script("return document.documentElement.outerHTML")
tree = html.fromstring(res)
#soup = BeautifulSoup(res, 'html.parser')
'''
value = tree.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/text()')
pattern = tree.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/div[3]/div[2]/div[1]/span[1]/span/text()')
print(value[0])
print(pattern[0] +" Pattern Detected")                    
'''
#Fw(b) Fl(end)--m Fz(s) C($primaryColor
#https://finance.yahoo.com/quote/GOOG/