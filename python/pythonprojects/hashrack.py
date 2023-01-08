import hashlib

# Obtain a list of hashes to crack
# hashes = ['ab56b4d92b40713acc5af89985d4b786', 'c5e433f17475d1e51f5ddb05fbb0e5e4']
hash_md5 = "f057f5ccb87a310534b9dda3a69a72c4"

# Define a function to calculate the hash of a password
def calculate_hash(password):
  return hashlib.md5(password.encode()).hexdigest()

# Create a list of potential passwords
passwords = ['password1', 'hii', 'password3']

# Iterate over the list of passwords and try to crack the hashes
for password in passwords:
  hash = calculate_hash(password)
  if hash == hash_md5:
    print('Password found:', password)
    break
else:
  print('Password not found')
