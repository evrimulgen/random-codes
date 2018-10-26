from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import requests
from faker import Faker as fk


driver = webdriver.Firefox()
driver.get("http://sv3e8g.srv.plusclouds.net/accounts/signup/")

while True:
	try:
		sleep(1)
		signup = driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(fk().city())
		signup = driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys("sallama1234")
		signup = driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys("sallama1234")
		driver.find_element_by_xpath('/html/body/div/div[2]/div/form/button').click()
		sleep(1)
		driver.find_element_by_xpath('/html/body/div/div[1]/a[4]').click()
		driver.get("http://sv3e8g.srv.plusclouds.net/accounts/signup/")
		
		# driver.quit()
	except:
		pass