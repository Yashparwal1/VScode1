import socket
import sys
import time
# import threading


usage = "python3 scan_port.py TARGET START_PORT END_PORT"

print("*"*70)
print("Port Scanner")
print("*"*70)

start_time = time.time()
                       
if (len(sys.argv) != 4):
    print(usage)
    sys.exit()

#Exception Handeling
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

for port in range(start_port, end_port+1):
    print(f"Scanning Port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.timeout(2)
    conn = s.connect_ex((target, port))
    if(not conn):
        # print("Port {} is OPEN".format(port))
        print("Port {port} is OPEN")
    s.close()
    # thread = threading.Thread(target = scan_port, args = (port,))
    # thread.start()

# end_time = time.time()

# print("Time Ellapsed:", end_time - start_time, "sec")