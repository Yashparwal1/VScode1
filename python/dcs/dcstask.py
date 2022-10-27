
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
