from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
import time

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
driver.get('http://inventwithpython.com')
time.sleep(1)
driver.quit()
