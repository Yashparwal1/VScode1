#imports and dependencies
import socket
import threading

#function for encryption
def enc_xor(data,key):
  res = b''
  for each_chr in data:
    temp = ord(each_chr)^key
    res = res + chr(temp).encode()
  return res

#function for decryption
def dec_xor(data,key):
  res = b''
  for each_chr in data:
    temp = each_chr^key
    res = res + chr(temp).encode()
  return res 


#thread recieve function
def thread_recv(sock_fd,key):
  while True:
      encrypted_msg = sock_fd.recv(1024)
      print(encrypted_msg)
      dec_msg = dec_xor(encrypted_msg,key) #calling decrytion function
      print("\n[+] Data:", dec_msg.strip().decode())
      if(dec_msg.strip() == b'exit'):
        print("[!] byebye!")
        sock_fd.close()
        break

#main function for listening for connection from client and sending data
def main():
  HOST = "127.0.0.1" #IP address
  PORT = 1234 #Port no. to listen on
  s = socket.socket()
  s.bind((HOST, PORT))
  s.listen(1)
  print("[+] Listining...")
  sock_fd, conn = s.accept() 
  #fd - file descriptor
  # sock_fd is connection received
  # and here, conn is address
  if(conn):
    print("[+] new connection:", conn)
    key = 25 #the key used in the XOR encryption
    new_thread = threading.Thread(target=thread_recv, args=(sock_fd,key))
    new_thread.start() # run the thread
    print("[+] recv is running as a thread!")
    while True:
      normal_msg = input("[+] input: ")
      enc_msg = enc_xor(normal_msg,key) #calling encrytion function
      sock_fd.send(enc_msg+b'\n')

main()
# --------------------------------------------------------
'''
# for i in 'KINGPING':
#   temp = ord(i)^90
#   res = res+chr(temp).encode()
# print(res)

r = b'\x11\x13\x14\x1d\n\x13\x14\x1d'
for i in r:
  print(i)
  print(f"{i}^90={chr(i^90)}")

# hex=11 -> binary -> 00010001 -> decimal -> 17 -> 17^90 -> 75 -> chr(75) -> K
# hex=13 -> binary -> 00010011 -> decimal -> 19 -> 19^90 -> 73 -> chr(73) -> I
# hex=1d -> binary -> 00011101 -> decimal -> 29 -> 29^90 -> 71 -> chr(71) -> G 

'''

""" 
# bruteforce key 

enc_msg = b'\x11\x13\x14\x1d\n\x13\x14\x1d'
# key = None
for key in range(80,100):
  res = ''
  for i in enc_msg:
    res = res+chr(i^key)
  print(f"for {key} => {res}")

# Now we can see the output and guess the most sensible word

 """