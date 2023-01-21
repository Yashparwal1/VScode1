import time, stem
from stem import Signal
from stem.control import Controller
import webbrowser
import pyautogui
import requests

# from stem.control import Controller

# # opening TOR 
# url = 'wiki47qqn6tey4id7xeqb6l7uj6jueacxlqtk3adshox3zdohvo35vad.onion'
# webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"D:\Tor Browser\Browser\firefox.exe"))
# webbrowser.get('firefox').open(url)

def change_tor_ip():
  # with Controller.from_port(port = 9151) as controller:
  #   controller.authenticate(password="test@7654321")
  #   controller.signal(stem.Signal.NEWNYM)

  # requests.get("http://localhost:9151/tor/renew")
  
  pyautogui.hotkey("ctrl","shift","l")  
  print("\nNew Circuit Established")

# time.sleep(10)
while True:
  totalsec = 20
  for i in range(20,0,-1):
    print(f"\rNew Circuit establishing in {i:02} sec",end='')
    time.sleep(1)
  change_tor_ip()
  time.sleep(10)

"""
we r using the stem library to connect to the Tor controller, authenticate, and then send the NEWNYM signal, which instructs Tor to change the circuit for connections made by the client. 
"""