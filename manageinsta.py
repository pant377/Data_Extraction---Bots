from selenium import webdriver
from pynput.mouse import Button, Controller
import os 
import time 
mouse = Controller()
s = 500
x = 0

url = 'https://www.instagram.com/accounts/login/'
driver = webdriver.Chrome("/Users/pantelis/Downloads/chromedriver.exe")
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("vogobarel@webmaild.net")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("thebotn1")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
mouse.position = (495, 420)

while True:
    try:
        time.sleep(1)
        driver.execute_script("window.scrollTo( %d , %d)" % (x,s)) 
        mouse.click(Button.left, 2)
    except:
        print('den vrethike bro')
        break    
    s += 600
    x = s
