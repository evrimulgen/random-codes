import time
import pyautogui


class Spammer():
	count = 0

	def copy():
		spam_txt = open('spam.txt', 'r')
		split = spam_txt.read().split()
		for i in range(len(split)):
			pyautogui.click(350, 110)
			pyautogui.click(350, 110)
			pyautogui.click(350, 110)
			time.sleep(0.5)
			pyautogui.typewrite("https://web.telegram.org/#/im?p=", interval=0.10)
			time.sleep(0.1)
			pyautogui.hotkey('shift', '2')
			pyautogui.typewrite(split[i].upper(), interval=0.10)		# writing channel name
			time.sleep(0.1)
			pyautogui.hotkey('enter')
			time.sleep(4)
			# pyautogui.click(90, 250)					# clicking channel			
			# time.sleep(2)
			pyautogui.click(425, 700) 					# join channel if not a member
			time.sleep(0.5)
			pyautogui.click(425, 700)
			pyautogui.click(425, 700)
			time.sleep(2)
			# pyautogui.click(410, 630) 					# write segment
			# pyautogui.click(410, 630)
			# time.sleep(1)
			# pyautogui.typewrite('...Crypto For Money...'.upper(), interval=0.10)
			# pyautogui.hotkey('shift', 'enter')
			# time.sleep(0.1)
			pyautogui.typewrite('I lately joined a channel named cryptoformoney, not happy about it', interval=0.10)
			pyautogui.hotkey('shift', 'enter')
			time.sleep(0.1)
			# pyautogui.typewrite('Our campaign will start when there are 1000 users who are also will be in core group.', interval=0.10)
			# pyautogui.hotkey('shift', 'enter')
			# time.sleep(0.1)
			pyautogui.typewrite('they only scam people to get money, they always prepump. Dont join the filthy channel named cryptoformoney, they scammed me probably will scam you as well', interval=0.10)
			# pyautogui.hotkey('shift', 'enter')
			# time.sleep(0.1)
			# pyautogui.typewrite('to join  ----> ', interval=0.10)
			# # if i < 5:
			# # 	pyautogui.hotkey('shift', '9')
			# # 	pyautogui.hotkey('shift', '2')
			# # 	pyautogui.hotkey('shift', '0')
			# # 	pyautogui.typewrite(' cryptoformoney')
			# pyautogui.hotkey('shift', '2')
			# pyautogui.typewrite('cryptoformoney', interval=0.10)
			# time.sleep(0.1)
			pyautogui.hotkey('enter')
			Spammer.count += 1
			print(Spammer.count)
			if Spammer.count > len(split):
				time.sleep(30)
			else:
				time.sleep(120)
		return Spammer.copy()

print(time.strftime("%H:%M:%S", time.gmtime()))
Spammer.copy()