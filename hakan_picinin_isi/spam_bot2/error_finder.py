# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from re import search
# from os import listdir
# import random, logging


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
					Spammer.prof_change(Spammer.profile_num)
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