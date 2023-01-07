import random
import string

def fuzz(length=100):
    for i in range(length):
        return ''.join(random.choice(string.printable)) 

out=''
for i in range(32):
    out = out+fuzz()
print(out)