# https://www.rocketsend.io/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #for starting and stopping the chrome driver
# from selenium.webdriver.chrome.options import Options # to perform ops like opeing chrome in max mode, disabling extensions, disabling pupups etc
from selenium.webdriver.common.action_chains import ActionChains # for pressing key on browser
from selenium.webdriver.common.keys import Keys # for pressing key on browser
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By # alt. is action_chains
from webdriver_manager.chrome import ChromeDriverManager # **
import time
from urllib.parse import quote
import os

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument("--user-data-dir=C:\\Users\\Yash\\Documents\\chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# f = open("message.txt", "r", encoding="utf8")
with open("message.txt", 'r') as file:
	message = file.read()
print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
# f = open("numbers.txt", "r")
with open("numbers.txt", 'r') as file:
	for line in file.read().splitlines():
		if line.strip() != "":
			numbers.append(line.strip())
print(numbers)
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #original
# driver = webdriver.Chrome(options=options) #chatgpt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # from yt
# time.sleep(10)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "Press ENTER after successful login..." + style.RESET)

for ind, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((ind+1), total_number, number) + style.RESET)
	try:
		url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
		sent = False
		for i in range(3): 
			if not sent:
				driver.get(url)
				time.sleep(5)
				try:
					send = ActionChains(driver)
					send.send_keys(Keys.ENTER)
					send.perform()
					time.sleep(5)
					sent = True
					print(style.GREEN + f'Message sent to {number}' + style.RESET)
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
			else:
				break
		if not sent:
			print(style.RED + f'Failed to send message to {number} after 3 attempts' + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)


		# for i in range(3): #retrying for 3 times
		# 	if not sent:
		# 		driver.get(url)
		# 		try:
		# 			click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
        #         except Exception as e:
		# 			print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
		# 			print("Make sure your phone and computer is connected to the internet.")
		# 			print("If there is an alert, please dismiss it." + style.RESET)
        #     else:
        #         sleep(1)
        #         click_btn.click()
        #         sent=True
        #         sleep(3)
        #         print(style.GREEN + 'Message sent to: ' + number + style.RESET)

driver.close()
