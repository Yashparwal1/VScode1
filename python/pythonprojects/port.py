import socket
import sys
import time
import threading
import pyfiglet

banner = pyfiglet.figlet_format("Port Scanner")
print(banner, end="")
print("|"+"_"*22 + "@Yashparwal1" + "_"*22+"|")
print("\n")

try:
    domain = input("[ + ] Enter Target domain or IP: ")
    try:
        target = socket.gethostbyname(domain)  # resolve host to ip
    except socket.gaierror:
        print("Name Resolution Error")
        print("Exiting...")
        sys.exit()

    start_port = int(input("[ + ] Enter Starting port: "))
    end_port = int(input("[ + ] Enter Ending Port: "))
# exception handeling for keyboard interrupt ctrl + c.
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

print("-"*40)
print("Scanning Target ==>", target)
print("-"*40)


def scan_port(port):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()  # socket start
    s.settimeout(5)  # setting timeout (time for waiting for connection)
    # bind host and port and establish connection and store in conn
    conn = s.connect_ex((target, port))
    # if connection exist that means port is open because connect_ex returns 0 if port is open.
    if (conn == 0):
        print(f"Port {port}: OPEN")
        try:
            # to detect service running on the port
            service = socket.getservbyport(port)
            print(f"Service running: {service}")
        except:
            print(f"Service running: NOT FOUND!!")
        print("-"*40)
    s.close()  # socket close

start_time = time.time() #calculating start time
thread_list = []
try:
    for port in range(start_port, end_port + 1):  # run loop from start port and end port
        thread = threading.Thread(target=scan_port, args=(port,))
        # calling scan_port func as one thread and similarly for each port a different threads is running.
        thread.start()
        # this appenig and for loop thing is for "Scan completed in: " thing 
        thread_list.append(thread) #add all threads in the list 
    for item in thread_list: #then iterate over that list and check for each thread whether that t. is completed or not 
        item.join() #ensure that if a thread is completed or not and then only it will move further 
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

end_time = time.time()
print("Scan Completed in :", end_time - start_time  , "sec")

""" 
Threading:

when we run a program, each line get executed line by line by one main thread.
In multithreading we can break the code in some parts and assign each part to diff. threads (means multiple taks executed at the same time) which runs parallel, and due to this our execution will take less time to complete.  

MAIN PROGRAM = CHILD THREAD  +  MAIN THREAD

Main thread will run the main program and a part of main program can be run as a child thread. And similarly different small parts of program (like diff. functions or same function in loop) can be run as different child threads. 
eg. a loop is running from 20 to 1000 ports.. So each loop can be run as one child thread, so there will be total 980 child threads running at the same time.

Without using multuithreading, the loop still runs 980 times but the 980 loops will be run one by one, not at the same time.

SO THIS IS THE BENIFIT OF MULTITHREADING. 

"""
