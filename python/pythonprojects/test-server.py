key = 25
msg = input("Enter msg: ")
data = msg.encode()
print(data)
# x = bytearray(len(data))

for i in range(len(data)):
    encrypted_msg = data[i] ^ key
    print(f"{encrypted_msg}\n")