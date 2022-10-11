""" #! py
import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile) 

for x in range(len(wifi_list)):
    print(wifi_list[x]) """

#! py
import cmd
from distutils.cmd import Command
import subprocess
import re

command = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profiles = (re.findall("All User Profile     : (.*)\r", command))
WifiList = []

if len(profiles) != 0:
    for name in profiles:
        WifiProfile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            WifiProfile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            __password__ = re.search("Key Content            : (.*)\r", profile_info_pass)
            if __password__ == None:
                WifiProfile["password"] = None
            else:
                WifiProfile["password"] = __password__[1]
            WifiList.append(WifiProfile) 

for x in range(len(WifiList)):
    print(WifiList[x])