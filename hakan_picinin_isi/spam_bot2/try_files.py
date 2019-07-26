from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
import random
from os import listdir

profile_dic = 'C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//used_profiles'

line = ["Hello{}".format("." * random.randint(0,5)), "Did you hear about Supreme Investments?", 
		#"Do you guys remember Supreme Investments?", 
		#"I suggest you guys to join them {}".format(":)" * random.randint(0,3)), 
		"They make awesome Pump and Dump again{}".format("." * random.randint(0,4))]

class Spammer:
	acc = ''
	count = 0
	profile_num = 0
	profile = webdriver.FirefoxProfile(profile_dic + '//%s//' % listdir(profile_dic)[profile_num])
	driver = webdriver.Firefox(profile)
	spam_txt = open('spam.txt', 'r').read().split()
	insta_ban = open('spam.txt', 'r').read().split("#")[0].split("\n")

	def event():
		for channel_number in range(len(Spammer.spam_txt)):
			Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[channel_number]))

			#sleep(10)
			#Spammer.try_join()
			#sleep(10)
			#Spammer.write(Spammer.count)
			sleep(15)
			Spammer.driver.quit()
			sleep(5)
			Spammer.profile_num += 1
			Spammer.prof_change(Spammer.profile_num)

	def prof_change(num):
		try:
			Spammer.acc = '%s//%s//' % (profile_dic, Spammer.listdir(profile_dic)[num])
		except IndexError:
			Spammer.profile_num, num = 0, 0
			Spammer.acc = '%s//%s//' % (profile_dic, Spammer.listdir(profile_dic)[num])

		Spammer.profile = webdriver.FirefoxProfile(Spammer.acc)
		Spammer.driver = webdriver.Firefox(Spammer.profile)

	def write(channel_number):
		write_bar = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]")
		for i in range(len(line)):
			write_bar.send_keys(line[i])
			write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
			sleep(0.1)
			
		if channel_number < len(Spammer.insta_ban):
			write_bar.send_keys('to join (at) supreme_investments')
		else:
			write_bar.send_keys('@supreme_investments')
		sleep(0.1)
		write_bar.send_keys(Keys.ENTER)

	def try_join():
		for join_might_be in Spammer.driver.find_elements_by_xpath("//a[@ng-click]"):
			if join_might_be.get_attribute("ng-click") == "joinChannel()":
				Spammer.driver.find_element_by_xpath("//a[@ng-click='joinChannel()']").click()

Spammer.event()