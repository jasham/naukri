from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver = webdriver.Chrome("C:\Python33\chromedriver.exe")
driver.get('https://login.naukri.com/')
uname=driver.find_element_by_id('emailTxt')
uname.send_keys('xyz@gmail.com')
passwd=driver.find_element_by_id('pwd1')
passwd.send_keys("xxxxx")
passwd.send_keys(Keys.ENTER)
var=1
while var==1:

	skills=driver.find_element_by_xpath("//a[@href='//my.naukri.com/ITSkills/edit?id=&altresid=']")
	time.sleep(2)
	skills.click()
	time.sleep(4)
	save_button=driver.find_element_by_css_selector('.w150bt.fl')
	save_button.click()
