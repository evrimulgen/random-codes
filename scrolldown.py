from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import search
from os import listdir
import random, logging


URLS = Nakış, Örgü çanta, Tığ ile örgü, Dantel 2, Gül ve kelebek, Kurdelen çiçek, Taş boyama, Rokoko, Patik, '30_alti': [Örgü, Ziyaret edilecek yerler, Kurdelen yaprak, Atatürk]

driver = webdriver.Firefox()
#driver.get("https://tr.pinterest.com/muhsineyidiz/oyalar/")
#driver.get("https://tr.pinterest.com/muhsineyidiz/dantel/")
driver.get("https://tr.pinterest.com/muhsineyidiz/t%C4%B1%C4%9F-i%C5%9Fi-yaprak/")

sleep(5)
while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")