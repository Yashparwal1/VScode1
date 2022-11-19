# # Method 1 - using single triple quotes (used for multiline string)
# print('''My name is Yash
# and I am studying in GNIOT''')

# # Method 2 - using double triple quotes
# print("""My name is Yash
# and I am studying in GNIOT""")

# # Method 3 - using double quotes
# print("My name is Yash\nand I am studying in GNIOT")

# # Method 4 - using single quotes
# print('My name is Yash\nand I am studying in GNIOT')

# name = input("Enter Your Name: ")

""" 
Variable - identifier
- first letter cannot be any digit
- first letter can be alphabet, underscore(_)
- variable name can contain (other than first letter) digits, alphabets or underscore
- varibale name cannot contain space
- keywords (32 keywords are there.. [going to be 36 soon]) cannot be identifier
"""

# 5yash = "my name" #syntax error
# yash5 = "my name" #no error
# _yash = "my name" #no error
# yash_parwal = "my name" #no error


# # a = 4
# num = int(input("Enter any no.: "))
# if(num%2 == 0):
#     # print("No.", num, "is Even")
#     print(f"No {num} is even")
# else:
#     # print("No.", num, "is Odd")
#     print(f"No {num} is odd")

# a = 10
# b = 20
# print(f"Before swapping a = {a} and b = {b}")
# temp = a
# a = b
# b = a
# b = temp
# print(f"After swapping a = {a} and b = {b}")

"""QUESTION:  a = 10, b=20 c=30
    a = 30 b=10 c=20 """

# a,b,c = 10,20,30
# print(f"Before swapping a = {a} and b = {b}")
# # a,b = b,a
# # b,c = c,b
# # a,b = b,a
# a,b,c = b,c,a
# print(f'''After swapping
# a = {a}
# b = {b}
# c = {c}''')

'''QUESTION: 
1. WAP to find whether the year is leap year or not
year should be divisible by 4 and not by 100 or year should be divisible by 400 
agar 4 se nhi ho rha to obviously nhi h, but 4 se ho rha h to 100 se nhi hona chahiye tab vo leap yr h agar phir bhi 100 se ho rha h to phir 400 se bhi hona chahiye 

OR

leap year if it it divisible by 100 and 400 OR leap year if it is not divisible by 100 and divisible by 4
[agar 100 se h to 400 se bhi hona chahiye |OR| agar 100 se nhi h to phir 4 se hona chahiye]
if(y%100==0 && y%400==0 || y%100!=0 && y%4==0)

2. WAP to find whether the giver no. is pelendrome or not

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

# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print(f"year {year} is a leap year")
# else:
#     print(f"year {year} is NOT a leap year")



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

# print("===============XYZ University Examination Form===============")
# name = input("Enter your name: ")
# roll = int(input("Enter your Roll No.: "))
# clgname = input("Enter your College name: ")
# aid = int(input("Enter your Aadhar Card No.: "))
# fee = 4000
# print("\n===============Student Details===============")
# print(f"Name: {name}")
# print(f"Roll No.: {roll}")
# print(f"College Name: {clgname}")
# print(f"Examination Fees: {fee}")
# print(f"Aadhar No.: {aid}")


""" 
Hospital Name and address
Patient name, age, phone no., sex, date, blood group, disease, recommended doctor name according to disease
"""
# print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-Surya Kids Hospital+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
# print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+Jaipir Rajasthan+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
# print("_"*75)
# print("+-+-+-+-+-+-+-+-+-+-+-+-+Parient Information Form+-+-+-+-+-+-+-+-+-+-+-+-+-\n")
# print("x-----------------xx-----------------xx-----------------xx-----------------x")
# print("GENERAL INFORMATION")
# fname = input("[ + ]- Patient's First Name: ")
# lname = input("[ + ]- Patient's Last Name: ")
# dob = input("[ + ]- Patient's Date of Birth (DD/MM/YY): ")
# age = int(input("[ + ]- Patient's Age: "))
# name = input("[ + ]- Patient's Sex: ")
# name = input("[ + ]- Patient's Address: ")
# name = input("[ + ]- Patient's Mob. No.: ")
# print("SYMPTOMS OR DISEASES")
# print('''
#         [ Press 1 ]- For Common Cold, Cough, Throat Infection, Ear problem
#         [ Press 2 ]- For Stomachace, Liver Problem, Intestine Problem 
#         [ Press 3 ]- For Heart problem, Respiratory System Problem 
# ''')
# ch = int(input("Enter Choice according to your symptoms: "))
# if ch == 1:
#     print("[\*/] Your Symptoms/Diseases are (related to): Common Cold, Cough, Throat Infection, Ear problem\n")
#     print("[\*/] Doctor Recommendation: Dr. Rajeev Singh (Cabin No. 14)")
# elif ch == 2:
#     print("[\*/] Your Symptoms/Diseases are (related to): Stomachace, Liver Problem, Intestine Problem\n")
#     print("[\*/] Doctor Recommendation: Dr. Natwar Parwal (Cabin No. 41)")
# elif ch == 3:
#     print("[\*/] Your Symptoms/Diseases are (related to): Heart problem, Respiratory System Problem\n")
#     print("[\*/] Doctor Recommendation: Dr. Shubham Sharma (Cabin No. 45)")
# else:
#     print("-----------Please Enter Correct Choice (choose from 1 to 3)------------")

# again = input('''Do you want to choose Symptoms option again?
# Press[y] for Yes and [N] for No
# ''')

# =========================================LISTS===========================================
""" 
Collection of diff. datatypes
List is Mutablle
"""

# l = [1,2,3,4,5,6,7]
# m = [10,11,12,13]
# l.append(9) #can add one element at one time at the end
# l.extend(m) #extend list a and add list m in list l


# name = 'This is my python class'
# # print(name[::-1]) 
# for i  in name[::-1]:
#     print(i,end="")

# m = l.copy() #copy list l into m
# l.count(4) #count the occurance of 4

# print(l.index(3)) #find out the index no. ==>the item '3' is on which index ==> like its on 2nd index

# l.insert(1,222) #insert 222 at index one
# l.pop() #remove the last element
# l.remove(1,222) #remove the
# print(l)
# l.reverse() #reverse the whole string
# t = [1,2,3,1,True,'a','l','b']
# t = [1,2,3,1]
# t.sort() #sort the whole list in assending order
# print(t)

# f_name = input("Enter your First name: ")
# m_name = input("Enter your Middle name: ")
# l_name = input("Enter your Last name: ")

# print(f"My name is {f_name} {m_name} {l_name}")

# a = 10
# b = 2
# print(f"The addition of a and b is {a+b}")
# print(f"Subtraction of a and b is is {a-b}")
# print(f"Product of a and b is {a*b}")
# print(f"Division of a and b is {a/b}")
# print(f"Floor division of a and b is = {a//b}")
# print(f"Modulo of a and b is {a%b}")

# ========================================================================================

#supermarket form.

stockPen = 10
stockBook = 10
stockCopy = 10
stockGbox = 10
stockBag = 10
price = 0
totalprice = 0
shoppingList = []
itemList = []
qtyList = []
priceList = []
print("=====List of available items=====")
print('''
1. Pen   Rs.10/each
2. Book  Rs.90/each
3. Copy  Rs.50/each
4. Gbox  Rs.25/each
5. Bag   Rs.200/each
''')

# items = {1:10,2:90,3:50,4:25,5:200}
items = {"pen":10,"book":90,"copy":50,"gbox":25,"bag":200}

for i in range(len(items)):
    shopping = int(input("Press 1 to Buy\nPress 2 to Generate Bill\n"))
    if shopping == 2:
        break
    elif shopping == 1:
        # product = int(input("Enter item no.: "))
        item = input("Enter item name from above list: ")
        if item in items:
            qty = int(input("Enter quantity: "))
            for item in items.keys():
                # price = qty * items.values() #values are in string so, int*str not possible
                price = qty * (items[item])
                shoppingList.append((item,qty,items,price)) 
                totalprice = totalprice+price
                itemList.append(item)
                qtyList.append(qty)
                priceList.append(price)
        else:
            print("Item is not available")
    else:
        print("Worong choice, Choose again")
        continue

print("==================================================")
print("                     BILL                         ")
print("==================================================")
print(len(shoppingList))
for i in range(len(shoppingList)):
    print(itemList,qtyList,priceList)       

# valid = False
# while (valid == False):
#     print("Which product(s) you want to order: ")
#     print("1. Pen [10/-]\n2. Book [90/-]\n3. Copy [50/-]\n4. Gbox [25/-]\n5. Bag [200/-]\n0. Generate Bill")
#     ch = int(input("Choose between 1 to 5: "))
#     if (ch == 1):
#         qtyPen = int(input("Specify quantity of Pens: "))
#         pricePen = 10*qtyPen
#         stockPen = stockPen-qtyPen
#     elif (ch == 2):
#         qtyBook = int(input("Specify quantity of Books: "))
#         priceBook = 90*qtyBook
#         stockBook = stockBook-qtyBook
#     elif (ch == 3):
#         qtyCopy = int(input("Specify quantity of Copy: "))
#         priceCopy = 90*qtyCopy
#         stockCopy = stockCopy-qtyCopy
#     elif (ch == 4):
#         qtyGbox = int(input("Specify quantity of Geomatry box: "))
#         priceGbox = 90*qtyGbox
#         stockGbox = stockGbox-qtyGbox
#     elif (ch == 5):
#         qtyBag = int(input("Specify quantity of Books: "))
#         priceBag = 90*qtyBag
#         stockBag = stockBag-qtyBag
#     elif (ch == 0):
#         valid = True
#         print("Generating Bill........")
#     else:
#         print("Worng choice !!!, Please choose again")

# print("==================================================")
# print("                     BILL                         ")
# print("==================================================")
# print("Your product list")
# print(f"{}")
