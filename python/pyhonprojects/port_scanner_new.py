# import pyfiglet
import sys
import socket
from datetime import datetime

# ascii_banner = pygiglet.figlet_format("PORT SCANNER")
# print(ascii_banner)

target = input("Target IP: ")

print("*"*50)
print(f"Scanning {target}")
print(f"Scanning Started at: {str(datetime.now())}")
print("*"*50)

try:
    #Scan all the ports on the target IP
    for port in range(20,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)

        #Return Open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("[ * ] Port {} is open".format(port))
        s.close() 
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
except socket.error:
    print("\nHost not Responding")
    sys.exit()