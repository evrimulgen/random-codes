from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.google.com")
#"//*[@id='lst-ib']"
# a=0
# for i in driver.find_elements_by_xpath("//a[@class]"):
# 	a+=1
# 	print(a)
# 	if i.get_attribute('class') == "_Gs":
# 		print(i.get_attribute('class'))
# 		driver.find_element_by_xpath("//a[@class='_Gs']").click()
# 		break
# 	else:
# 		pass
# print("hello world!")

print(driver.find_element_by_xpath("//*[@id='_eEe']").text)








# for i in driver.find_elements_by_xpath("//input"):
# 	if i.get_attribute("name") == "q":
# 		driver.find_element_by_xpath("//input[@name='q']").send_keys("mal beran")
# 	else:
# 		pass
# 	for i in driver.find_elements_by_xpath("//input"):
# 		if i.get_attribute("name") == "btnK":
# 			print(i.get_attribute("name"))
# 			driver.find_element_by_xpath("//input[@name='btnK']").click()






	#driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys("sa")

# if "/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]" in driver.find_elements_by_xpath("/html"):
# 	driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]").click()
# else:
# 	print(False)
# 	driver.quit()

#driver.quit()