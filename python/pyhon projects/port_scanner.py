import socket
import sys
import time
import threading
import pyfiglet

usage = "  python3 port_scaner.py [TARGET] [START_PORT] [END_PORT]"
banner = pyfiglet.figlet_format("Port Scanner")
print(banner,end="")
print("|"+"_"*22 + "@Yashparwal1" + "_"*22+"|")
print("\n")
start_time = time.time()

# if 4 arguments args are not recieved from user, then print the usage and exit
if (len(sys.argv) != 4):
    print("-"*26 + " USAGE " + "-"*27)
    print(usage)
    print("-"*60)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1]) #resolve host to ip
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
print("Scanning target", target)
def scan_port(port):
   # print("Scanning", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    conn = s.connect_ex((target, port))
    if(not conn): #OR if(conn == 0):
        print("Port {} is OPEN".format(port))
    s.close()
    
# multiplethreading requires a function that's why 
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()

end_time = time.time()
print("Scan Completed in :", end_time - start_time  , "sec")