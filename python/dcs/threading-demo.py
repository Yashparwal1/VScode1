from threading import *
from time import sleep 

class One(Thread):
    def run(self):
        for i in range(50):
            print("Class One")
            sleep(1)

class Two(Thread):
    def run(self):
        for i in range(50):
            print("Class Two")
            sleep(1)

obj1 = One()
obj2 = Two()
obj1.start()
obj2.start()

# we can see that threads of class one and class two running simultaneously 

# -----------------------------------------------------------------

# t1 = threading.Thread(target=obj1.run())
# t1.start()
# t2 = threading.Thread(target=obj2.run())
# t2.start()
