from selenium import webdriver
import configparser
import os 
import time 

def photo_like():

    for user in users[:len(users)]:
        time.sleep(2)
        driver.get(instabaselink+user)
        time.sleep(1)
        imgs = driver.find_elements_by_class_name('_9AhH0')
        #posts = driver.find_element_by_class_name('g47SY ').get_text()
        for img in imgs[:2]:
            img.click() 
            time.sleep(1.4) 
            try:
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                driver.find_element_by_xpath('/html/body/div[3]/button[1]').click() 
            except:
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                pass
    return             

def userfollow():

    for user in users[:len(users)]:
        time.sleep(2)
        driver.get(instabaselink+user)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
        time.sleep(1)
   
url = 'https://www.instagram.com/accounts/login/'
driver = webdriver.Chrome("/Users/pantelis/Downloads/chromedriver.exe")
#usr = ['vogobarel@webmaild.net','vakofiyo@umail365.com']
#passw = ['thebotn1','thebotn2']

with open('D:/Files/WebScraping/list.txt') as f:
    for i in range(0,2):
        
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(f.readline())
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(f.readline())
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        users = ['pantelis_.pap']
        instabaselink = 'https://www.instagram.com/'
        photo_like()
