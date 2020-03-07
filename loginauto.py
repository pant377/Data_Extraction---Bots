from selenium import webdriver

user = ''
passw = ''
url = 'http://pithia.teithe.gr/unistudent/'

driver = webdriver.Chrome("/home/pantelis/Downloads/chromedriver")
driver.get(url)
driver.find_element_by_id('userName').send_keys(user)
driver.find_element_by_id('pwd').send_keys(passw)
driver.find_element_by_id('submit1').click()
