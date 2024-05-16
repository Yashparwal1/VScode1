import hashlib
Key = "9828"
message = "yash"
hashed_key = hashlib.sha256(Key.encode()).digest()
length_of_hashed_key = len(hashed_key)
print("hashed key === ",hashed_key)
print("length: ",length_of_hashed_key)
# # Encrypt the message using the hashed key
# encrypted_message = lsb.hide(str(filename), message)

# Embed the hashed key along with the encrypted message in the stego image
combined_data = length_of_hashed_key.to_bytes(1, byteorder='big') + hashed_key + message.encode()
print("combined = ", combined_data)

stored_hashed_key = combined_data[:32]  # Assuming the length of the hashed key is 32 bytes (256 bits)
print("stored === ", stored_hashed_key)

if hashed_key == stored_hashed_key:
    print("marched")