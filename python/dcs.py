 
# for i in range(1,5):
#     print(i)
# for i in range(1,5):
#     print("yash")

# for i in range(1,10,2):   #print 1 to 10 with gap of 2
#     print(i)
# for i in range(5):   #print 0 to 4, it will take
#     print(i)

# no = 153
# sum=0

# for i in range(len(str(no))):
#     rem = no%10
#     sum = sum + (rem*rem*rem)
#     no = no//10

# if(no==sum):
#     print("Armstrong no.")
# else:
#     print("Not an armstrong no.")

# for i in range(4):
#     for j in range(i+1):
#         print("* ",end="")
#     print("\n")

""" for i in range(1,6):
    print(" "*(5-i) + ("*"*i))
 """
"""  
new = 0
for i in range(1,5):
    print(" "*(5-i) + "*"*new)
    new = new+2
 """

""" new = 0
for i in range(0,7,2):
    print(" "*(i-new) + "*"*(7-i))
    new = new+1
"""

# for x in range(1,10):
#     if(x/3==2):
#         # break
#         # continue
#         # pass
#         print(x)
# #code

# for i in range(1,101):
#     if(i%2 == 0):
#         continue
#     else:
#         print(i)

# if not 5>3:
#     print("done")

#############################################################################################################
# 2/10/22
# ___________________________________________________________________________________________________________

"""
List: collection of items
grocery = ["harpic", "vim", "deo", "bhujiya", "lollypop", 56, True]
note: any type of data can be entered in list
"""
# x = list(range(1,5))
# x = list()
# if [""]:  #empty list means false
#     print("x")

# data = [1,2,3,"Hello",True]
# print(data[0])
# print(data[2])
# print(data[-1]) #negative indexing
# for i in data:
#     print(i)

# data.append(4) #add the data as a single item at last of the list
# print(data)
# data.append([4,5]) #we can provide list within a list
# print(data)

# print(data[-1]) # will give [4,5]
# print(data[-1][0]) # will give 4

# data.extend([4,5]) #add the data as diff. items
# print(data)

# data.insert(3,"hlo") #hlo will be inserted at 3rd index
# print(data) 
#NOTE: in negative indexing, first it it converted into equivalent positive index and then data is inserted

# data=[1,2,3, "hello", True,]

# for i in data[::-1]:
#     print(i)

# given: [5,4,3,"y","a","s",8,9]
# to print: [3,4,5,8,9,"y","a","s",]

# ip = input("Enter IP: ")
# print(ip)
# print(type(ip))

# a = 10
# b = 5
# print(a,b)
# temp = a
# a = b
# b = temp
# print(a,b)

# import os
# ip = '192.168.1.'

# for x in range(0,256):
#     addr = ip+str(x)    
#     print(addr)
#     result = os.popen(f"ping -n 1 {addr}")

