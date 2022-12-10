
""" 
<== 1 ==>
sName = input("Enter the Name: ")
print("Enter the marks of student",sName,"Out o 100: ")
# print("Enter the marks out of 100")
eng = int(input("Marks of English : "))
hin = int(input("Marks of Hindi:  "))
maths = int(input("Marks of Maths: "))
science = int(input("Marks of Science: "))
sanskrit = int(input("Marks of sSanskrit: "))
total = 500
marks = eng + hin + maths + science + sanskrit
percent = marks/total*100
print("Total marks: ",marks)
print("You got", percent, "%")
if percent < 35:
    print("You have failed ! by", 35-percent, "percent")
elif percent == 35:
    print("Just Passed, keep it up!!")
elif percent > 35 and percent < 80:
    print("Good, You are promoted")
elif percent >= 80  and percent < 100:
    print("Excellent !!!")
else:
    print("Ah Swap! You have entered some wrong input, run the program again !!!")
"""
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

"""
<== 2 ==>
#cost of item per unit
pen = 10
notebook = 40
book = 120
gbox = 50
#get customer and product details
name = str(input("Enter Name: "))
email = str(input("Enter Email: "))
phno = int(input("Enter phone no.: "))
totalPen = int(input("How many pens purchased: "))
totalNotebook = int(input("How many Notebooks purchased: "))
totalBook = int(input("How many books purchased: "))
totalGbox = int(input("How many geometry box purchased: "))

#calculation of total bill value
tcPen = pen*totalPen
tcnotebook = notebook*totalNotebook
tcBook = book*totalBook
tcGbox = gbox*totalGbox
bill = tcPen+tcnotebook+tcBook+tcGbox

#printing customer details and bill values
print("------------------------------------------------------------")
print("Customer's Details")
print("------------------------------------------------------------")
print("| Name: ", name)
print("| Email: ", email)
print("| Phone no.: ", phno)
print("------------------------------------------------------------")
print("Total cost of Pen: ", tcPen)
print("Total cost of Notebook: ", tcnotebook)
print("Total cost of Book: ", tcBook)
print("Total cost of Geometry Box: ", tcGbox)
print("=====================================================")
print("Total bill: ",bill)
print("=====================================================")

if (bill >= 1000):
    print("Congrats!! You got 40 pecent discount.")
    discount = (40/100)*bill
    bill = bill - discount
    print("Now total bill is: ",bill)
    print("=====================================================")
elif (bill > 500 and bill < 1000):
    print("Congrats!! You got 20 pecent discount.")
    discount = (20/100)*bill
    bill = bill - discount
    print("Now total bill is: ",bill)
    print("=====================================================")
elif (bill >= 100 and bill <= 500):
    print("Congrats!! You got 10 pecent discount.")
    discount = (10/100)*bill
    bill = bill - discount
    print("Now total bill is: ",bill)
    print("=====================================================")
elif (bill < 100):
    print("Congrats!! You got 5 pecent discount.")
    discount = (5/100)*bill
    bill = bill - discount
    print("Now total bill is: ",bill)
    print("=====================================================\n")

choice = int(input("Do customer want a carry bag or home delivery?\n\n[1] for Carry bag\n[2] for Home delivery: "))
if (choice == 1):
    bagCharge = 5
    print("\nBag charges: ",bagCharge)
    bill = bill + bagCharge
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Final bill is: ",bill)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
elif (choice == 2):
    dc = (3/100)*bill
    bill = bill + dc
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Final bill is: ",bill)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
"""
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# <== 3 ==>
#TO FIND EXACT HOW OLD A PERSON IS.
# dday = int(input("Enter Birth date : "))
# dmonth = int(input("Enter Birth month : "))
# dyear = int(input("Enter Birth year : "))

# cd,cm,cy = 8,10,2022

# if cy>year:
#     if cm>month:
#         age = cy-dyear
#         print(age)
#     elif cm==dmonth:
#         if cd>=dday:
#             age = cy-dyear
#             print(age)
#         else:
#             age = cy-dyear-1
#             print(age)
#     else:
#         age = cy-dyear-1
#         print(age)
# else:
#     print("You have entered something wrong")

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# <== 4 ==>
# file = open("dcs.txt","w")
# for i in range(5):
#     file.write("* "*i)
# file.close()

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

'''
<== 5 ==>
PYTHON PROGRAM TO FIND WHETHER A YEAR IS LEAP YEAR OR NOT
Concept:
year should be divisible by 4 and not by 100 or year should be divisible by 400 
agar 4 se nhi ho rha to obviously nhi h, but 4 se ho rha h to 100 se nhi hona chahiye tab vo leap yr h agar phir bhi 100 se ho rha h to phir 400 se bhi hona chahiye 
'''
# year = int(input("Enter the year: "))
# if (year % 4 == 0):  # if it is true
#     if (year % 100 == 0):  # then it should be false BUT if it is also true
#         if (year % 400 == 0):  # then it should also be true becoz 100 se divide hone ka mtlb h vo century year h so we have to check if this century year is divisible by 400 to be a leap year othervise no leap year.
#             print(f"Year {year} is a leap year")
#         else:
#             print(f"Year {year} is NOT a leap year")
#     else:
#         print(f"Year {year} is a leap year")
# else:
#     print(f"Year {year} is NOT a leap year")

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# <== 6 ==>
# PYTHON PROGRAM TO FIND WHETHER A NO IS PALINDROME OR NOT
# n = 121
# using string slicing(convert the no. into sting format)

# rev = str(n)[::-1] #start:stop:step
# if(n == rev):
#     print(f"No. {n} is a palindrome no.")
# else:
#     print(f"No. {n} is NOT a palindrome no.")

#using traditional method
# i=n
# rev=0
# while(i>0):
#     rem = i%10
#     rev = rev*10 + rem
#     i = i//10
# if(n == rev):
#     print(f"No. {n} is a palindrome no.")
# else:
#     print(f"No. {n} is NOT a palindrome no.")

#using reversed function
# rev = reversed(n) #int object is not reversible
# i = str(n) #convert int into str
# rev = ''.join(reversed(i)) #join is a function of string just like concatination in C
# if i==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

""" 
*******
|*****|
||***||
|||*|||
|||*|||
||***||
|*****|
*******
"""

# star=7
# pipe=3
# for i in range (0,4):
#     print("|"*i + "*"*star + "|"*i)
#     star = star-2
# star=1
# for i in range (1,5):
#     print("|"*pipe + "*"*star + "|"*pipe)
#     pipe = pipe-1
#     star = star+2


# space = 5
# for i in range (1,12,2):
#     print(" "*space + "*"*i)
#     space -= 1

# space = 1
# for i in range (9,0,-2):
#     print(" "*space + "*"*i)
#     space += 1

# TASK ==> Write a program to input a filename, read the file then calculate the total no. of alphabets in it. (not numbers, spaces or special characters). Remove all those alphabets and leave the file with rest of the characters.

""" 
alpha = 0
with open("dcs.txt", "w") as file:
    file.write(input("Enter some lines: "))
file.close()

file = open("dcs.txt", "r")
data = file.read()
print(data)

for i in data:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        alpha += 1
print(f"Total no. of alphabets in the stentence are: {alpha}")
for i in data:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        data = data.replace(i,'')
print(f"after removing all the alphabest, remaining chars are: {data}")
"""

# class Rectangle:
#     # l,b = 5,6
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def peri(self):
#         pr = 2*(self.l+self.b)
#         print(pr)
#     def area(self):
#         ar = (self.l*self.b)
#         print(ar)
#     def display(self):
#         print(self.l)
#         print(self.b)
#         self.peri()
#         self.area()
# l = int(input("Enter the length: "))
# b = int(input("Enter the breadth: "))
# obj = Rectangle(l,b)
# obj.display()


# x=[" "]
# if x:
#    print("True")

# print(str(int(str(int(str(int(str("22")))))))+"29.0"+3)

# mylist = []
# for i in range(0, 4):
#     data = int(input("Please enter 4 values: "))
#     mylist.append(data)

# mylist.sort()

# print(f"Largest no: {mylist[3]}")
# print(f"Smallest no: {mylist[0]}")

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

import time

# time 12:00:00
totalsec = 3610
# h = 1
# m = 60
# s = 60
for i in range(totalsec,0,-1):
    # hour = i/3600
    # min = (i/60)%60
    # sec = i%60
    # print(f"{hour}:{min}:{sec}",end="")   
    print(f"\r{int(i):02}",end="")   
    time.sleep(1)