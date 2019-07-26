from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
from os import listdir
import random, logging

LOG_FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(
	filename = "C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//file_info.log",
	level = logging.WARNING,
	format = LOG_FORMAT,
	filemode = "a"
)

profile_dic = 'C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//new_profiles'

line = [[
		"Biggest and the greatest Pump/Investment channel Supreme Investments is back to make your wallet go up. Nearest pump is Tomorrow.", "Dont forget to attent for the big pump.", "Join before its too late"
		],[
		"Tomorrow is the day for PUMP", "Any of you guys doing pumps?", "Supreme Investments is best channel for pumps and Investments"
		],[
		"I saw Supreme Investments, the best Investments/Pump channel on telegram", "I also heard that the pump. You guys can check them out, they are really friendly as I see so far"
		],[
		"As you know Pumps are really good and easy way to get some money.", "I know a channel named Supreme Investments follow them on telegram for nearest pump which is this Monday."
		]]

class Spammer():
	acc = ''
	count = 0
	profile_num = 0
	profile = webdriver.FirefoxProfile(profile_dic + '//%s//' % listdir(profile_dic)[0])#random.randint(0, len(listdir(profile_dic))) -1])
	driver = webdriver.Firefox(profile)
	spam_txt = open('whole_spam.txt', 'r').read().split()
	insta_ban = open('whole_spam.txt', 'r').read().split("#")[0].split("\n")
	sent_list = []

	def prof_change(num):
		# banned_list = open("file_info.log", "a")
		# banned_list.write("\n" + str(num))
		# banned_list.close()

		try:
			# banned_list = open("file_info.log", "r").read().split("\n")
			# if str(num) in banned_list:
			# 	return True

			print("New account is {}".format(listdir(profile_dic)[num]))
			Spammer.acc = '%s//%s//' % (profile_dic, listdir(profile_dic)[num])
		except IndexError:
			Spammer.profile_num, num = 0, 0
			print("New account is {}".format(listdir(profile_dic)[num]))
			Spammer.acc = '%s//%s//' % (profile_dic, listdir(profile_dic)[num])

		Spammer.driver.quit()
		Spammer.profile = webdriver.FirefoxProfile(Spammer.acc)
		Spammer.driver = webdriver.Firefox(Spammer.profile)
		sleep(1800)
		Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[random.randint(0, len(Spammer.spam_txt)) -1]))

	def join():
		Spammer.driver.get("https://web.telegram.org/#/im")
		sleep(15)
		area_tel = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input")
		area_tel.send_keys(Keys.CONTROL,"a")
		area_tel.send_keys("+1")
		phone = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input")
		phone.send_keys("7209906742")
		sleep(1)
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a/my-i18n").click()
		sleep(2)
		Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button[2]").click()
		input("ready?")
		return Spammer.event()

	def look_for_error(channel_number, **kwargs):
		sleep(10)
		for error_might_be in Spammer.driver.find_elements_by_xpath("//h4[@class]"):
			try:
				if error_might_be.get_attribute("class") == "md_simple_header":
					Spammer.driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
					sleep(2)
					whole_message = Spammer.driver.find_element_by_css_selector(".error_modal_details").text#"/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea").text   .error_modal_details
					error_message = search('"error_message":"', whole_message)
					wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
					print(wait_time, Spammer.spam_txt[channel_number], listdir(profile_dic)[Spammer.profile_num], sep=" - ")
					if wait_time == "FORBIDDEN" or wait_time == "PRIVATE":
						Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[random.randint(0, len(Spammer.spam_txt)) -1]))
						sleep(10)
						Spammer.try_join()
						sleep(10)
						Spammer.write(channel_number)
						sleep(10)
						break
					elif wait_time == "MUCH" or  wait_time == "CHANNEL":
						Spammer.profile_num += 1
						Spammer.prof_change(Spammer.profile_num) #- 1)
						#Spammer.log_it()
						break
					try:
						if int(wait_time).__class__ == int:
							Spammer.profile_num += 1
							Spammer.prof_change(Spammer.profile_num)
							break
						else:
							break
						# print("Waiting {} mins".format(round(int(wait_time) / 60)))
						# sleep(int(wait_time) + 5)
					except:
						break
				else:
					break
			except:
				break
	

	def log_it():			#calismiyor xdxd
		print("logging it")
		banned_list = open("file_info.log", "r")
		banned_list = banned_list.readlines()
		for i in range(len(banned_list)):
			print(banned_list[i], Spammer.profile_num)
			if re.search("account %s is banned\n" % (Spammer.profile_num) ,banned_list[i]).group(0) == "account %s is banned\n" % (Spammer.profile_num):
				print("exist")
				break
			else:
				logging.getLogger().warning("account %s is banned" % listdir(profile_dic)[Spammer.profile_num])
				print("wrote it")
		print("done")

	def write(channel_number):
		try:
			#rd = random.randint(0, len(line) -1)
			write_bar = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]")
			for i in range(len(line[Spammer.profile_num])):
				write_bar.send_keys(line[Spammer.profile_num][i])
				# if  random.randint(0,1) == 1:
				# 	write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
				# else:
				write_bar.send_keys(Keys.ENTER)
				sleep(0.1)
				
			# if channel_number < len(Spammer.insta_ban):
			# 	write_bar.send_keys('(@)supreme_investments')
			# else:
			# 	write_bar.send_keys('@supreme_investments')
			sleep(0.1)
			write_bar.send_keys('(@)supreme_investments')
			write_bar.send_keys(Keys.ENTER)
			sleep(0.1)
			write_bar.send_keys('@supreme_investments')
			write_bar.send_keys(Keys.ENTER)
			Spammer.count += 1
			print(Spammer.count)
		except:
			pass

	def try_join():
		try:
			for join_might_be in Spammer.driver.find_elements_by_xpath("//a[@ng-click]"):
				if join_might_be.get_attribute("ng-click") == "joinChannel()":
					Spammer.driver.find_element_by_xpath("//a[@ng-click='joinChannel()']").click()
		except:
			pass

	def event():
		# reverse_or_normal = random.randint(0,1)
		for channel_number in range(len(Spammer.spam_txt)):
			# if reverse_or_normal == 0:
			random_channel = random.choice(Spammer.spam_txt)
			Spammer.sent_list.append(random_channel)
			# print(random_channel)
			if Spammer.sent_list in Spammer.spam_txt:
				# print("already Sent")
				continue
				# Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.random.choice(Spammer.spam_txt)))
			else:
				# Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[channel_number]))
				Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(random_channel))
			# else:
			# 	Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[len(Spammer.spam_txt) - (channel_number + 1)]))
			Spammer.look_for_error(channel_number)
			Spammer.try_join()
			Spammer.look_for_error(channel_number)
			Spammer.write(channel_number)
			Spammer.look_for_error(channel_number)
			# if  random.randint(0, 9) == 0:
			# 	print("Rigged")
			# 	Spammer.profile_num += 1
			# 	Spammer.prof_change(Spammer.profile_num)
			# 	sleep(30)
			# else:
			# 	sleep(200)	
			sleep(random.randint(150, 300))			

		print("LENS--->", len(Spammer.spam_txt), len(Spammer.sent_list))
		Spammer.sent_list = []
		return Spammer.event()

while True:
	Spammer.event()