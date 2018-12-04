from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
import random
import requests

class Spammer:
	phone_code = ""
	count = 0
	profile = webdriver.FirefoxProfile('C://Users//Raq//AppData//Roaming//Mozilla//Firefox//w8z62y4j.default//')
	driver = webdriver.Firefox(profile)
	#driver.set_window_position(1000, 768)
	spam_txt = open('spam.txt', 'r').read().split()

	def join_china(phone_number, **kwargs):
		print("Hi China")
		Spammer.driver.get("https://web.telegram.org/#/login")
		# driver.file_detector()
		sleep(20)
		area_tel = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input")
		area_tel.send_keys(Keys.CONTROL,"a")
		area_tel.send_keys("86")
		num = phone_number[2::]
		print(phone_number)
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys(num)
		sleep(1)
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a/my-i18n").click()
		sleep(2)
		Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button[2]").click()
		sleep(20)
		for error_might_be in Spammer.driver.find_elements_by_xpath("//h4[@class]"):
			if error_might_be.get_attribute("class") == "md_simple_header":
				print("Error Found")
				Spammer.driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
				sleep(2)
				whole_message = Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/textarea").text
				error_message = search('"error_message":"', whole_message)
				wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
				print(wait_time)
				if wait_time == "FORBIDDEN":
					try:
						Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button").click() # tekrar dene falan
						print("Clicked")
						SMS.getsms_()
					except:
						print("couldnt click :(")
						SMS.getsms_()
					# return Account_create.wait_for_code() #(code=code, phone_number=phone_number)
				elif wait_time == "BANNED":
					print("added black list")
					SMS.addblack
				else:
					pass 
			else:
				pass
		give_code = input("what is the code on telegram?")
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[4]/input").send_keys(give_code)
		return Spammer.event()
