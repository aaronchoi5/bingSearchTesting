from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


#for obvious security reasons I will not have my email and password hard coded
#also might extend this application to include multiple accounts
with open("../userinfo.txt",) as fs:
	email = fs.readline()
	passwrd = fs.readline()

with open("../searchlist.txt",) as ls:
	searchItems = ls.readlines()

driver = webdriver.Chrome()
driver.get('http://www.bing.com/')

#might randomize times in order to throw off potential bing bot detector
time.sleep(3)
driver.find_element_by_id("id_l").click()
time.sleep(3)

name_field = driver.find_element_by_id("i0116")
name_field.send_keys(email)
time.sleep(2)

driver.find_element_by_name("passwd").send_keys(passwrd)
time.sleep(3)
for i in range(len(searchItems)):

	#normally i'll use an action chain to do this
	driver.find_element_by_class_name('b_searchbox').send_keys(searchItems[i])

	driver.find_element_by_class_name('b_searchbox').send_keys(Keys.ENTER)
	driver.find_element_by_class_name('b_searchbox').clear()
	time.sleep(3)
driver.quit()
