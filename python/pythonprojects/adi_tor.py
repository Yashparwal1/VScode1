import platform
import subprocess
import pyautogui
import time

def new_identity():
  pyautogui.hotkey('ctrl', 'shift', 'l')
  # reference - https://tor.stackexchange.com/questions/7256/is-there-a-hot-key-for-new-identity

def new_identity_for_mac():
  pyautogui.hotkey('command', 'shift', 'l')
  # reference - https://stackoverflow.com/questions/56452938/what-is-the-hotkey-for-command-in-pyautogui
  
def open_tor_browser():
    os_name = platform.system()
    if os_name == "Linux":
      subprocess.run(["tor-browser"])
      try:
        while True:
          new_identity()
          time.sleep(15)
      except KeyboardInterrupt:
        print("Exiting program")
        
    elif os_name == "Windows":
      subprocess.run(["start", "tor-browser"], shell=True)
      try:
        while True:
          new_identity()
          time.sleep(15)
      except KeyboardInterrupt:
        print("Exiting program")
        
    elif os_name == "Darwin":
      subprocess.run(["open", "-a", "Tor Browser"])
      try:
        while True:
          new_identity_for_mac()
          time.sleep(15)
      except KeyboardInterrupt:
        print("Exiting program")
  
    else:
      print("The operating system is not supported")

open_tor_browser()

