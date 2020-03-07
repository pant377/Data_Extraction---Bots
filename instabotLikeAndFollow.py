from selenium import webdriver
import os 
import time 
#login
url = 'https://www.instagram.com/accounts/login/'
user = ''
passw = ''
driver = webdriver.Chrome("/Users/pantelis/Downloads/chromedriver.exe")
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(user)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(passw)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
users = ['','']
#user managment
instabaselink = 'https://www.instagram.com/'

def photo_like():

    for user in users[:len(users)]:
        time.sleep(2)
        driver.get(instabaselink+user)
        time.sleep(1)
        imgs = driver.find_elements_by_class_name('_9AhH0')
        #posts = driver.find_element_by_class_name('g47SY ').get_text()
        for img in imgs[:10]:
            img.click() 
            time.sleep(2) 
            try:
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/button[1]').click() 
            except:
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                pass
    driver.close()            

def userfollow():

    for user in users[:len(users)]:
        time.sleep(3)
        driver.get(instabaselink+user)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
        time.sleep(1)
    driver.close()


photo_like()