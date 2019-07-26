from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search, match
import random, requests, sys, os


new_location = "C://Users//Raq//Desktop//Others//hakan_picinin_isi//spam_bot2//new_profiles"
temp = "C://Users//Raq//AppData//Local//Temp"

info = {
	#'login': 'http://www.getsmscode.com/do.php?action=login&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626',
	#'getmobile': 'http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10',
	#'getsms': 'http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile=%s&author=mirkanbaba1@gmail.com',	#numara ver sms almak icin
	#'addblack': 'http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile=%s',		#numarayi gonder blacklist icin
	'login': 'http://www.getsmscode.com/do.php?action=login&username=kalaysrt@gmail.com&token=5e326123ee4a9d1f698b0b3e0064af94',
	'getmobile': 'http://www.getsmscode.com/do.php?action=getmobile&username=kalaysrt@gmail.com&token=5e326123ee4a9d1f698b0b3e0064af94&pid=10',
	'getsms': 'http://www.getsmscode.com/do.php?action=getsms&username=kalaysrt@gmail.com&token=5e326123ee4a9d1f698b0b3e0064af94&pid=10&mobile=%s&author=kalaysrt@gmail.com',
	'addblack': 'http://www.getsmscode.com/do.php?action=addblack&username=kalaysrt@gmail.com&token=5e326123ee4a9d1f698b0b3e0064af94&pid=10&mobile=%s',
	'mobilelist': 'http://www.getsmscode.com/do.php?action=mobilelist&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626'
	}



def create_account(sms):
	"""Making all the process untill the look_for_error function (fiving number, clicking etc.)"""
	print(requests.get(info['login']).text, sms)
	driver = webdriver.Firefox()
	driver.get("https://web.telegram.org/#/login")
	sleep(10)
	driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys(str(sms)[2:])
	driver.find_element_by_css_selector(".ng-pristine").send_keys(Keys.CONTROL, "A")
	driver.find_element_by_css_selector(".ng-pristine").send_keys(str(sms[:2]))
	sleep(5)
	driver.find_element_by_css_selector(".login_head_submit_btn > my-i18n:nth-child(1)").click()
	sleep(5)
	driver.find_element_by_css_selector("button.btn:nth-child(2)").click()
	return look_for_error(driver, sms)

def get_key(driver, sms):
	"""Waits for code to appear via API. If the code is not recieved restarts whole program"""
	count = 0
	while True:
		reply = requests.get(info['getsms'] % (sms)).text
		print(count, reply)
		if reply[-5:].isdigit():
			reply = reply[-5:]
			break
		# if reply != 'Message|not receive':
		# elif reply == "Message|mobile number not found!":
		if count > 10:
			driver.quit()
			print("%s is blacklisted" % (sms))
			requests.get(info['addblack'] % (sms))
			return create_account(str(requests.get(info['getmobile']).text))
		count += 1
		sleep(11)
	return we_done(reply, driver)

def we_done(reply, driver):
	"""After the code appears takes it and writes it down to where it need to be writen on selenium-web-page"""
	print(reply)
	driver.find_element_by_css_selector(".md-input").send_keys(str(reply))
	sleep(10)

	try:
		driver.find_element_by_css_selector(".btn").click() #FORGOT PASSWORD?
		sleep(10)
		driver.find_element_by_css_selector(".btn-md-danger").click() #RESET ACCOUNT
		sleep(10)
		driver.find_element_by_css_selector("button.btn:nth-child(2)").click() #RESET MY ACCOUNT
	except:
		print("excepted")

	sleep(180)
	print("I hope you done, cuz im done")
	return replace_file()

def replace_file():
	"""If we_done is succeded this function creates new file on desired location and replace webappstore.sqlite from temp location to desired location"""
	for i in os.listdir(temp):
		if match("rust", i):
			if os.path.isdir(temp + "//" + i):
				print("passed isdir")
				for j in os.listdir(temp + "//" + i):
					if match("webappsstore", j):
						print("passeed webapp")
						os.mkdir(new_location + "//" + str(len(os.listdir(new_location)) + 1))
						os.rename(temp + "//" + i + "//" + j, new_location + "//" + str(len(os.listdir(new_location))) + "//" + j)
	sys.exit()

def look_for_error(driver, sms, **kwargs):
	sleep(10)
	for error_might_be in driver.find_elements_by_xpath("//h4[@class]"):
			if error_might_be.get_attribute("class") == "md_simple_header":
				# try:
					driver.find_element_by_xpath("//a[@class='error_modal_details_link']").click()
					sleep(2)
					whole_message = driver.find_element_by_css_selector(".error_modal_details").text#"/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea").text   .error_modal_details
					error_message = search('"error_message":"', whole_message)
					wait_time = whole_message[error_message.end():].split("_")[-1].split('"')[0]
					print(wait_time)
					if wait_time == "PRIVATE" or wait_time == "FORBIDDEN":
						count = 0
						while True:
							count += 1
							reply = requests.get(info['getsms'] % (sms)).text
							print(count, reply)
						break
					elif wait_time == "BANNED":
						print("%s is blacklisted" % (sms))
						requests.get(info['addblack'] % (sms))
						driver.quit()
						return create_account(requests.get(info['getmobile']).text)
					elif wait_time == "MUCH" or  wait_time == "CHANNEL":
						# profile_num += 1
						# prof_change(profile_num)
						# log_it()
						break
					# try:
					# 	if int(wait_time).__class__ == int:
					# 		# profile_num += 1
					# 		# prof_change(profile_num)
					# 		break
					# 	else:
					# 		break
					# 	# print("Waiting {} mins".format(round(int(wait_time) / 60)))
					# 	# sleep(int(wait_time) + 5)
					# except:
					# 	break
					else:
						continue
				# except:
				# 	print("passed")
				# 	pass
	return get_key(driver, sms)


# create_account(str(requests.get(info['getmobile']).text))





num = requests.get(info['getmobile']).text
#print(num)

def run(num):
	print(requests.get(info['login']).text, num[3:])
	while True:
		try:
			sms = requests.get(info['getsms'] % (num)).text
			print(sms)
			if sms != 'Message|not receive':
				print("yap bakam bi, sonra duzeltirsin")
			sleep(10)
		except:
			print("banned")
			requests.get(info['addblack'] % (num)).text
			return run(requests.get(info['getmobile']).text)
#print(requests.get(info['getmobile']).text)
run(requests.get(info['getmobile']).text)
