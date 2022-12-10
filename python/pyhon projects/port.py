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

try:
    domain = input("[ + ] Enter Target domain or IP: ")
    try:
        target = socket.gethostbyname(domain) #resolve host to ip
    except socket.gaierror:
        print("Name Resolution Error")
        print("Exiting...")
        sys.exit()
    start_port = int(input("[ + ] Enter Starting port: "))
    end_port = int(input("[ + ] Enter Ending Port: "))
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

# try:
#     target = socket.gethostbyname(domain) #resolve host to ip
# except socket.gaierror:
#     print("Name Resolution Error")
#     print("Exiting...")
#     sys.exit()
# start_port = int(input("[ + ] Enter Starting port: "))
# end_port = int(input("[ + ] Enter Ending Port: "))

print("-"*40)
print("Scanning Target ==>", target)
print("-"*40)

def scan_port(port):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()
    s.settimeout(5)
    conn = s.connect_ex((target, port))
    if(conn == 0):
        print(f"Port {port} is OPEN")
    s.close() 
try:
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target = scan_port, args = (port,))
        thread.start()
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

# end_time = time.time()
# print("Scan Completed in :", end_time - start_time  , "sec")