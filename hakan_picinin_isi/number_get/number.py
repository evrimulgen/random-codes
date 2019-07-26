from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
import random
import requests

class SMS:
	code= ""
	login = requests.get('http://www.getsmscode.com/do.php?action=login&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text
	getmobile = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10').text
	getsms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(getmobile)).text
	addblack = requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(getmobile)).text
	mobilelist = requests.get('http://www.getsmscode.com/do.php?action=mobilelist&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text

	def getsms_():
		i = 0
		while True:
			i+=1
			sleep(10)
			sms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(SMS.getmobile)).text
			print(i, sms)
			if sms != 'Message|not receive':
				code = sms.split(">")[1]
				print(code)
				input("click a button to process after you done with logging in with your phone")
				return Spammer.join_china(phone_number=getmobile)
			else:
				pass
			if i > 10:
				SMS.addblack
				break

class Account_create:
	#profile = webdriver.FirefoxProfile('C:/Users/Raq/AppData/Roaming/Mozilla/Firefox/firefox-mirkan/')
	driver = webdriver.Firefox()
	random_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
	areacodes = [205, 251, 256, 334, 938, 907, 209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 628, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 831, 858,
			916, 925, 949, 951, 239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954, 229, 404, 470, 478, 678, 706, 762, 770, 912, 217, 224, 309, 312,
			331, 618, 630, 708, 773, 779, 815, 847, 872, 231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989, 218, 320, 507, 612, 651, 763, 952, 212, 315, 332, 347, 516, 518,
			585, 607, 631, 646, 680, 716, 718, 845, 914, 917, 929, 934, 216, 220, 234, 330, 380, 419, 440, 513, 567, 614, 740, 937, 210, 214, 254, 281, 325, 346, 361, 409, 430, 432,
			469, 512, 682, 713, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979, 276, 434, 540, 571, 703, 757, 804, 262, 414, 534, 608, 715, 920, 401, 787, 939, 503, 541]

	def choice():
		for i in range(random.randint(5,15)):
			yield random.choice(Account_create.random_letters)

	def getnada():
		Account_create.driver.get("https://getnada.com/")
		sleep(2)
		Account_create.driver.find_element_by_css_selector(".icon-plus").click()
		sleep(2)
		Account_create.driver.find_element_by_xpath("/html/body/div/div[1]/footer/a[2]").click()	
		sleep(2)
		adress = Account_create.driver.find_element_by_css_selector(".address").text
		print(adress)
		if adress.split("@")[1] == "undefined":
			return Account_create.getnada()
		else:
			return Account_create.textnow(adress)

	def textnow(adress):
		Account_create.driver.get("https://www.textnow.com/signup")
		sleep(2)
		
		# input("r?")
		# Spammer.driver.quit();
		Account_create.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[2]").click()
		Account_create.driver.find_element_by_xpath('//*[@id="first"]').send_keys([i for i in Account_create.choice()])																	#NAME

		Account_create.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[1]/div").click()
		Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[2]/input').send_keys([i for i in Account_create.choice()])					#LASTNAME

		Account_create.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[3]/div/div").click()
		Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[3]/div/input').send_keys([i for i in Account_create.choice()])				#USERNAME

		Account_create.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div/div").click()
		Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div/input').send_keys([i for i in Account_create.choice()] + ["1pass1"])	#PASSWORD

		Account_create.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[5]/div").click()
		Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[5]/div/input').send_keys(adress)												#EMAIL 
		
		Account_create.driver.find_element_by_xpath('//*[@id="re_captcha"]').click()																									#RECAPTHA
		sleep(2)

		try:
			Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/button[1]').click()																	#SIGNUP
		except:
			return Spammer.join_china(phone_number=SMS.getmobile)
			#input("Could not do, you try!")
			# return Account_create.textnow(adress=adress)
			Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/button[1]').click()

		sleep(25)

		for error_might_be in Account_create.driver.find_elements_by_xpath("//p[@class]"):
			if error_might_be.get_attribute("class") == "help-block alert alert-danger error-message ng-binding":
				print("ERROR")
				for i in range(5):
					print(i, end=", ", flush=True)
					if i == 4:
						sleep(18)
						# Account_create.driver.close()
						# return Account_create.getnada()
						return Account_create.textnow(adress=adress)
					else:
						try:
							sleep(25)
							Account_create.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/form/button[1]').click()
						except:
							Account_create.textnow(adress=adress)
			else:
				pass

		sleep(20)
		Account_create.driver.find_element_by_xpath('//*[@id="areacode"]').send_keys(random.choice(Account_create.areacodes))															#ARENACODE
		Account_create.driver.find_element_by_xpath('//*[@id="areacode"]').send_keys(Keys.ENTER)
		sleep(5)
		Account_create.driver.find_element_by_xpath('//*[@id="recaptcha-verify-container"]').click()																					#RECAPTHA
		sleep(10)
		# except:
		# 	return Account_create.textnow(adress=adress)

		try:
			Account_create.driver.find_element_by_xpath('//*[@id="close-button"]').click()																								#CLOSEBUTTON
		except:
			input("Could not do, you try!")
			Account_create.driver.find_element_by_xpath('//*[@id="close-button"]').click()
		print(Account_create.driver.find_element_by_css_selector(".phoneNumber").text)
		return Spammer.join(phone_number=Account_create.driver.find_element_by_css_selector(".phoneNumber").text)								#BURADAN NEREYE GIDILECEGI KESIN DEGIL DUZELT

	def wait_for_code():
		i=0
		phone_number = Account_create.driver.find_element_by_css_selector(".phoneNumber").text
		while True:
			code = Account_create.driver.find_element_by_css_selector(".message").text
			i+=1
			sleep(20)
			print(code, i, sep=",", flush=True)
			if code.split(" ")[-1] != "here":
				print(int(code.split(" ")[-1]))
				code = code.split(" ")[-1]
				Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[4]/input").send_keys(code)
				sleep(5)
				return Spammer.event(channel_number=0)			#GOES TO SPAMMER() CLASS
			else:
				print("Didnt found yet ", i)
				pass


class Spammer:
	phone_code = ""
	count = 0
	#profile = webdriver.FirefoxProfile('C://Users//Raq//AppData//Roaming//Mozilla//Firefox//w8z62y4j.default//')
	driver = webdriver.Firefox()
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





	def join(phone_number, **kwargs):
		Spammer.driver.get("https://web.telegram.org/#/login")
		# driver.file_detector()
		sleep(15)
		area_tel = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/input")
		area_tel.send_keys(Keys.CONTROL,"a")
		area_tel.send_keys("+1")
		# sleep(5)
		# p_number = int(input("Give me the number: "))
		# print(phone_number, type(phone_number))
		area_num = phone_number[1:4]					#Phone number
		num2 = phone_number[5::]
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys(area_num+num2)
		sleep(1)
		Spammer.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/a/my-i18n").click()
		sleep(2)
		Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button[2]").click()
		# kwargs.popitem()[1] kwargs'in value ciktisi icin
		Spammer.look_for_error(channel_number=0, phone_number=phone_number)
		return Account_create.wait_for_code()
		# input("ready?")
		# return Spammer.event()	

	def look_for_error(channel_number, **kwargs):
		sleep(20)
		# print("look_for_error - ", channel_number + 1)
		for error_might_be in Spammer.driver.find_elements_by_xpath("//h4[@class]"):
			try:
				if error_might_be.get_attribute("class") == "md_simple_header":
					print("Error Found")
					Spammer.driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
					sleep(2)
					whole_message = Spammer.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea").text
					print(whole_message)
					error_message = search('"error_message":"', whole_message)
					wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
					print(whole_message, wait_time, sep=" ,", flush=True)
					print(wait_time == "FORBIDDEN")
					if wait_time == "FORBIDDEN":
						try:
							print("Clicked")
							Spammer.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/button").click() # tekrar dene falan
						except:
							print("couldnt click :(")
							Spammer.phone_code = input("Waiting for you to sign up with Phone. Give phone number: ")
						return Spammer.event()
						# return Account_create.wait_for_code() #(code=code, phone_number=phone_number)
					else:
						pass
					#print(whole_message)
					#print(error_message)
					try:
						print("Waiting {} mins".format(round(int(wait_time) / 60)))
						sleep(int(wait_time) + 5)
					except:
						Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[channel_number + randint(1, 5)]))
				else:
					pass
			except:
				pass
		# return join(phone_number=phone_number)

	def write(channel_number):
		write_bar = Spammer.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]")
		write_bar.send_keys(('S u p r e m e I n v e s t m e n t s').upper())
		write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
		sleep(0.1)
		write_bar.send_keys('We are an investment channel about crypto currencies.')
		write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
		sleep(0.1)
		# write_bar.send_keys('Our campaign will start when there are 1000 users who are also will be in core group.')
		# write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
		# sleep(0.1)
		# write_bar.send_keys('We are going to share short or long term signals that are backed and discussed by experts with first comers.')
		# write_bar.send_keys(Keys.SHIFT, Keys.ENTER)
		# sleep(0.1)
		write_bar.send_keys('Join us... ')

		if channel_number < 14:
			write_bar.send_keys('search for (at) supreme_investments on telegram')
		else:
			write_bar.send_keys('@supreme_investments')
		sleep(0.1)
		write_bar.send_keys(Keys.ENTER)

	def event():
		for channel_number in range(len(Spammer.spam_txt)):
			Spammer.driver.get("https://web.telegram.org/#/im?p=@{}".format(Spammer.spam_txt[channel_number]))

			#LOOKING FOR ERROR#
			Spammer.look_for_error(channel_number = channel_number)

			for join_might_be in Spammer.driver.find_elements_by_xpath("//a[@ng-click]"):
				if join_might_be.get_attribute("ng-click") == "joinChannel()":
					Spammer.driver.find_element_by_xpath("//a[@ng-click='joinChannel()']").click()
					break
				else:
					pass

			#LOOKING FOR ERROR#
			Spammer.look_for_error(channel_number = channel_number)

			try:
				Spammer.write(channel_number = channel_number)
			except:
				pass

			if Spammer.count > len(Spammer.spam_txt):
				# NOT SURE IF NECCESARY OR NOT
				# channel_number = 0
				sleep(30)
			else:
				sleep(100)

			Spammer.count += 1
			print(Spammer.count)

		return Spammer.event()

# Spammer.join(phone_number="5301336881")

Account_create.getnada()
