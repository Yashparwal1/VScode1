
# =========== Ans. 10 ===================

# mylist = []
# for i in range(0, 4):
#     data = int(input("Please enter 4 values: "))
#     mylist.append(data)

# mylist.sort()

# print(f"Largest no: {mylist[3]}")
# print(f"Smallest no: {mylist[0]}")

# -------------OR------------------

# num1 = int(input("Enter first no: "))
# num2 = int(input("Enter second no: "))
# num3 = int(input("Enter third no: "))
# num4 = int(input("Enter fourth no: "))

# if (num1>num2):
#     if (num1>num3):
#         if (num1>num4):
#             print(f"{num1} is largest")
#         else:
#             print(f"{num4} is largest")
#     else:
#         if (num3>num4):
#             print(f"{num3} is largest")
#         else:
#             print(f"{num4} is largest")
# else:
#     if (num2>num3):
#         if (num2>num4):
#             print(f"{num2} is largest")
#         else:
#             print(f"{num4} is largest")
#     else:
#         if (num3>num4):
#             print(f"{num3} is largest")
#         else:
#             print(f"{num4} is largest")

# =========== Ans. 11 ===================
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# r = 5
# space = 8
# for i in range(1,6):
#     print("*"*i + " "*space + "*"*i)
#     space = space-2 

# space = 2
# for i in range(4,0,-1):
#     print("*"*i + " "*space + "*"*i)
#     space = space+2 

# =========== Ans. 12 ===================
import time

totalsec = 3610
for i in range(totalsec,0,-1):
    hour = i//3600
    min = (i//60)%60 #%60 so that we cannot exceed above 60
    sec = i%60
    print(f"\r{hour:02}:{min:02}:{sec:02}",end="")   
    # print(f"\r{int(i):02}",end="")   
    time.sleep(1)
print("target achieved ....")