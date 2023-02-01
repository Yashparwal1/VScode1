import requests
from bs4 import BeautifulSoup
# URL = "https://gitlab.com/kalilinux/packages/fern-wifi-cracker"
URL = "https://www.kali.org/tools/wifite/"
# URL = "https://github.com/aircrack-ng/aircrack-ng"
print("please wait..\r", end="")
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
paras = soup.select('pre')  # hardik
# paras = soup.select('article[class="file-holder limited-width-container readme-holder"]')
print(paras[0].text)

# def run_on_browser(URL):
#     # print("[+] Opening url")
#     print("[+] Opening Article")
#     proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
#     # there keyfor success output and noththere for error output
#     (there, notthere) = proc.communicate()
#     there = there.decode()
#     there = there.split("/")
#     if "root" in there:
#         os.system(f"firefox {URL} 2>dev/null")
#     else:
#         # this is to get desktop enviroment
#         proc = subprocess.Popen(
#             [f"echo $DESKTOP_SESSION"], stdout=subprocess.PIPE, shell=True)
#         (envo, noenvo) = proc.communicate()
#         # this is to get username
#         proc = subprocess.Popen(
#             [f"cat /etc/passwd | grep {there[2]}"], stdout=subprocess.PIPE, shell=True)
#         (uid, notuid) = proc.communicate()
#         uid = uid.decode()
#         uid = uid.split(":")
#         if envo == "GNOME":
#             os.system(
#                 f"sudo chown root:root /run/user/{uid[2]}/gdm/Xauthority")
#             os.system(f"firefox {URL} 2>/dev/null")
#         else:
#             os.system(f"sudo chown root:root /home/{there[2]}/.Xauthority")
#             os.system(f"firefox {URL} 2>/dev/null")


#!/usr/bin/python

# import subprocess,os

# # url = "https://www.google.com/"
# # print("[+] Opening Article")
# proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
# (there, notthere) = proc.communicate()
# there = there.decode()
# there = there.split("/")
# print(there)

# proc = subprocess.Popen([f"cat /etc/passwd | grep {there[1]}"], stdout=subprocess.PIPE, shell=True)
# (uid, notuid) = proc.communicate()
# uid = uid.decode()
# uid = uid.split(":")
# print(uid)
# # if "root" in there:
# # 	os.system(f"firefox {url} 2>/dev/null")


