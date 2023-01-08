# import random
# import string

# def fuzz(length=100):
#     for i in range(length):
#         return ''.join(random.choice(string.printable))

# out=''
# for i in range(32):
#     out = out+fuzz()
# print(out)

import random


def fuzzer():
    ran_chars = ''
    for i in range(100):
        ran_chars = ran_chars+chr(random.randrange(0, 256))
        return ran_chars

for i in range(40):
    print(fuzzer(),end='')
