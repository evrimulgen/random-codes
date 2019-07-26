from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
import random
import requests
#import number

profile_dic = 'C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//used_profiles'

class SMS:
	login = requests.get('http://www.getsmscode.com/do.php?action=login&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text
	getmobile = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10').text
	getsms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(getmobile)).text
	addblack = requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(getmobile)).text
	mobilelist = requests.get('http://www.getsmscode.com/do.php?action=mobilelist&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text

	def getsms_(phone_number):
		print(phone_number)
		black_check = input("blacklist?")
		if black_check == "y":
			requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(phone_number)).text
			num = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10')
			return SMS.getsms_(num.text)
		else:
			pass
		i = 0
		while True:
			i+=1
			sleep(10)
			sms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(phone_number)).text
			print(i, requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(phone_number)).text)
			# if sms != 'Message|not receive':
			# 	try:
			# 		code = sms.split(">")[1]
			# 		print(code)
			# 		input("click a button to process after you done with logging in with your phone")
			# 		return Spammer.join_china(phone_number=getmobile)
			# 	except:
			# 		code = sms.split("]")[1]
			# 		print(code)
			# 		input("click a button to process after you done with logging in with your phone")
			# 		return Spammer.join_china(phone_number=getmobile)
			# else:
			# 	pass
			if i % 10 == 0:
				k = input("blacklist?")
				if k == "y":
					requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(phone_number)).text
					num = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10')
					return SMS.getsms_(num.text)
				else:
					pass

# class Spammer:
# 	phone_code = ""
# 	count = 0
# 	profile = webdriver.FirefoxProfile(profile_dic + '//%s//' % listdir(profile_dic)[random.randint(0, len(listdir(profile_dic))) -1])
# 	driver = webdriver.Firefox(profile)
# 	driver.set_window_position(1000, 768)
# 	spam_txt = open('spam.txt', 'r').read().split()

# 	def join_china(phone_number, **kwargs):
# 		if phone_number == "Message|Issue,Try later!":
# 			print(phone_number)
# 			sleep(30)
# 			return Spammer.join_china(phone_number=requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10').text)
# 		else:
# 			pass
# 		Spammer.driver.get("https://web.telegram.org/#/login")
# 		# driver.file_detector()
# 		sleep(20)
# 		area_tel = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input")
# 		area_tel.send_keys(Keys.CONTROL,"a")
# 		area_tel.send_keys("86")
# 		num = phone_number[2::]
# 		print(phone_number)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys(Keys.CONTROL,"a")
# 		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys(num)
# 		sleep(1)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a/my-i18n").click()
# 		sleep(2)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button[2]").click()
# 		sleep(20)
# 		for error_might_be in Spammer.driver.find_elements_by_xpath("//h4[@class]"):
# 			if error_might_be.get_attribute("class") == "md_simple_header":
# 				print("Error Found")
# 				Spammer.driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
# 				sleep(2)
# 				whole_message = Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/textarea").text
# 				error_message = search('"error_message":"', whole_message)
# 				wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
# 				print(wait_time)
# 				if wait_time == "FORBIDDEN":
# 					try:
# 						Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button").click() # tekrar dene falan
# 						print("Clicked")
# 						SMS.getsms_(phone_number=phone_number)
# 					except:
# 						print("couldnt click :(")
# 						SMS.getsms_(phone_number=phone_number)
# 					# return Account_create.wait_for_code() #(code=code, phone_number=phone_number)
# 				elif wait_time == "BANNED":
# 					Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button").click()
# 					print("added black list")
# 					requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(phone_number)).text
# 					new_num = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10').text
# 					print(new_num)
# 					return Spammer.join_china(phone_number=new_num)
# 				else:
# 					pass 
# 			else:
# 				pass
# 		give_code = input("what is the code on telegram?")
# 		sleep(1)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a/my-i18n").click()
# 		sleep(2)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button[2]").click()
# 		sleep(2)
# 		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[4]/input").send_keys(give_code)
# 		print("done")
# 		return number.Spammer.event()


SMS.getsms_(phone_number=SMS.getmobile)