""" 
==> WHAT IS PYTHON?
* Python is a dynamically typed general purpose programming language that supports OOP approach as well as a functional programming approach.
* Python is an interpreted and a high-level programming language.
* It was created by Guido Van Rossum in 1989.

==> FEATURES OF PYTHON
* Simple and easy to understand, User Friendly
* Faster
* Best package for AI
* Exensively used in industry
* Read code line by line
* Portable
* Platform independent

==> Identifier
* It can be any alphabet between A to Z or a to z
* it cannot be started with any digit
* it cannot be started with any special character except underscore( _ )
* A keyword cannot be an identifier.

eg. 
a=10
print(a)
--------- 
A=20
print(A)
---------
_abc = 100
print(_abc)
---------

==> KEYWORDS:
* Keywrods are the restricted words in python which cannot be used as identifiers
* To know the keyword -- command is: help('keywords)

==> SINGLE LINE STATEMENT:-
a = 'This is my python class' [with single quotes]
a = "This is my python class" [with double quotes]
a = '''This is my python class''' [with triple-single quotes]

==> MULTIPLE LINE STATEMENT:-
a = '''This
is
me'''
print(a)


# # Method 1 - using single triple quotes (used for multiline string)
# print('''My name is Yash
# and I am studying in GNIOT''')

# # Method 2 - using double triple quotes
# print('''My name is Yash 
# and I am studying in GNIOT''')

# # Method 3 - using double quotes
# print("My name is Yash\nand I am studying in GNIOT")

# # Method 4 - using single quotes
# print('My name is Yash\nand I am studying in GNIOT')



==> DATATYPES
1. Numeric Datatypes
    - int
    - float
    - complex
2. Sequence Datatypes
    - list
    - tuple
    - dictionary
    - string
    - set
3. Boolean Datatypes
    - True
    - False
------------------------------------------------------------

==> NUMERIC DATATYPES

a = 10
b = 10.6
c = 2+3i

print(a)
print(type(a)) # will print the datatype of a
print(id(a)) # will print the memory location of a

print(b)
print(type(b)) # will print the datatype of b
print(id(b)) # will print the memory location of b

print(c)
print(type(c)) # will print the datatype of c
print(id(c)) # will print the memory location of c

==> INPUT FROM USER

num = int(input("Enter any no.: "))
print(num)

num = float(input("Enter any float no.: "))
print(num)

num = complex(input("Enter any complex no.: "))
print(num)

"""

# print("[ + ] Please enter first no. greater than second no. [ + ]")
# num1 = int(input("Enter first no. "))
# num2 = int(input("Enter second no. "))

# print(f"Addition: {num1+num2}")
# print(f"Subtration: {num1-num2}")
# print(f"Multiplication: {num1*num2}")
# print(f"Division: {num1/num2}")
# print(f"Floor Divison (Integer division): {num1//num2}")
# print(f"Modulus: {num1%num2}")

# --------------------------------------------------------------------------
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


# mylist = []
# for i in range(0, 4):
#     data = int(input("Please enter 4 values: "))
#     mylist.append(data)

# mylist.sort()

# print(f"Largest no: {mylist[3]}")
# print(f"Smallest no: {mylist[0]}")

#using max and min function
# print(max(mylist))
# print(min(mylist))

# --------------------------------------------------------------------------

# 1. Arithmatic Operator
# +, -, *, /, //, %, **

# 1.
# a = 10 
# b = 20
# c = a+b
# print(c)
# 2.
# a = 10
# b = 5
# c = a-c
# print(c)
# 3.
# a = 10
# b = 2
# c = a*b
# print(C)
# 4.
# a = 10
# b = 3
# c = a/b
# print(C)
# 5.
# a = 20
# b = 5
# c = a//b
# print(C)
# 6.
# a = 15
# b = 2
# c = a%b
# print(C)
# 7.
# a = 4
# b = 2
# c = a**b
# print(C)

# ==> COMPARISION OPERATOR
# 1. 
# a = 10
# b = 20
# print(a==b)
# OUTPUT: False
# 2. 
# a = 20
# b = 10
# print(a>b)  -- True 
# print(a<b)  -- False
# print(a!=b) -- True
# 3. 
# a = 10
# b = 2
# print(a>=b) -- True
# print(a<=b) -- False

# ==> LOGICAL OPERATOR
# and , or , not

# print(not(True)) -- False
# print(not(False)) -- True
# print(not(1)) -- False
# print(not(0)) -- True
# print(not(10)) -- False
# print(not(-10)) -- False

# print(True and True) -- True
# print(True and False) -- False
# print(False and True) -- False
# print(False and False) -- False

# print(10 and 10) -- 10
# print(0 and 0) -- 0
# print(1 and 0) -- 0
# print(-10 and -10) -- -10
# print(1 and 1) -- 1
# print(10 and 20) -- 20
# print(20 and 10) -- 10

# print(True or True) -- True
# print(True or False) -- True
# print(False or True) -- True
# print(False or False) -- False

# print(10 or 10) -- 10
# print(0 or 0) -- 0
# print(1 or 0) -- 1
# print(-10 or -10) -- -10
# print(1 or 1) -- 1
# print(10 or 20) -- 10
# print(20 or 10) -- 20

# ==> ASSIGNMENT OPERATOR

# a = 20

# a += 10 --> a = 20 + 10 = 30
# a -= 10 --> a = 20 - 10 = 10
# a *= 10 --> a = 20 * 10 = 200
# a /= 10 --> a = 20 / 10 = 2
# a //= 10 --> a = 20 // 10 = 2
# a %= 10 --> a = 20 % 10 = 0

# ==> MEMBERSHIP OPERATOR

# in 

# eg.
# a = "This is my Python class"
# print('This' in a) -- True
# print('y' in a) -- True

# not in
# a = "This is my Python class"
# print('This' not in a) -- Flase
# print('f' not in a) -- True

# a = "This is my python class"
# print("This" is a)

# b = "This is my python class"
# print("This is my python class" is b)

# c = "This"
# print('This' is c)
# print("This" is not c)

# # a = 10
# # b = 10
# # print(id(a))
# # print(id(b))

# a = [1]
# b = [1]
# print(id(a))
# print(id(b))


# DATATYPES

# 1. List :
# Its a collection of various datatypes
# It is enclosed in square brackets
# Its is separated by comma
# It is mutable

# a = [10, 10.5, 4+5j,True, None, 'Python']
# print(a)
# print(type(a))
# print(id(a))

# Append element to the end of the list.
# a.append(10) #10 will be added at end

# # Clear delets all the elements and will give empty list 
# a.clear()

# # Copy all the elements of a list into another list 
# b = a.copy
# print(b)

# # Count the occurance an element in a list.  
# a = [1,1,1,1,1,4,5,63,5]
# print(a.count(2))

# # Extend list by appending elements from the iterable.
# a = [1,2,3,4]
# b = [5,6,7]
# a.extend(b) #extending a with the help of b
# b.extend(a) #extending b with the help of a
# print(a)

# # Return the index of a value
# a = [11,22,33,44,55,66,77]
# a.index(33) #output is 2


# # insert(index_number,value)
# a = [11,22,33,44,55,66,77]
# a.insert(-1,5)  
# a.insert(7,5) 

# #Remove and return item at index (default last).
# a = [11,22,33,44,55,66,77]
# a.pop()  #remove element at last index
# a.pop(2) #remove element at index 2 

# # Remove first occurrence of value.
# a = [11,22,33,44,55,66,77]
# a.remove(33) #remove 33

# a = [2,4,4,6,7,4,3,5,7]
# a.sort() #sort the list in assending order
# a.sort(reverse=True)

# a.reverse() #reverse the list

# -------------------------------------------------------------------------------------

# 2. TUPLE 
# It is enclosed in parenthesis
# It is separated by comma
# It is immutable
# It consists of diff. datatypes

# a = (10,10.5, 'Python', None, True, True, True, False)

# # Return number of occurrences of value.
# print(a.count(True))
# print(a.count('Python'))

# # Return first index of value.
# print(a.index(None))

# ------------------------------------------------------------------------------

# 3. String 

# a = 'This is my Python Class'
# print(a)
# print(type(a))
# print(id(a))


# a = 'This is my Python Class'
# b = "I am a BCA student"
# a.count("i")
# a.count("This")

# # a.lower() #convert all characters into lowercase

# a.title() #capitalize the first letter of each word

# a.capitalize() #capitalize the first letter of first word and 

# a.replace('i','y') #replace all 'i' with 'y'
# a.replace("Python", "Java")

# print(a.split(' '))  #['This', 'is', 'my', 'Python', 'Class']
# print(a.split('my')) ['This is ', ' Python Class']

# c = '. '.join([a,b])
# print(c)

#concatination
# print(a+'. '+b)

# ---------------------------------------------------------------------------------

# 4. SETS
# It is enclosed in curly braces {}
# It is separated by comma
# It is an unordered collection of data
# It consist of unique elements
# It consist of various datatypes
# Mathematical Operations can be done on set

# a = {2,3,4,5,34,3,4,5,3,3,45,43,3}
# print(a) #{34, 3, 2, 4, 5, 43, 45}
# print(type(a))
# print(id(a))

# a.add(5) #no duplicate elements !!
# a.add(1)
# print(a)
# b = {1,2,3,5,6,7}
# b.add(4) 
# print(b)

# a = {1,2,3,4}
# b = {5,6,7}

# b = a.copy()

# a.pop() #removes 1st element

# a.remove(4) #remove(value)

# a = {1,2,3,4,5,6}
# b = {1,2,7,8,9}
# a.difference(a) #a-b
# a.union(b) 
# a.intersection(b)

# ------------------------------------------------------------------------------

# 5. Dictionary
# It is a collection of key:value pair 
# It consist of unique keys
# It is enclosed in curly braces
# It is separeated by comma
# Key and Value is separated by colon

# a = {1:'Python',
# 2:'Java',
# 3:'C++' }
# print(a)
# print(type(a))
# print(id(a))

# 1,2,3 are keys
# 'Python','Java','C++' are values

# print(a.keys())

# print(a.values())

# print(a.items())

# a.clear()

# b = a.copy()

# a.get(3) #values availabe on 3 key

# a.fromkeys() #Create a new dictionary with keys from iterable and values set to value.

# ==> Slicing

# a = 'This is my Python Class'
# print(a[::8])

# ==> CONDITIONAL STATEMENT

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a>b:
#     print("A is bigger")
# if b>a:
#     print("B is bigger")
# if a==b:
#     print("A and B are equal")

# ------------------------------------------------------------

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# if a>b:
#     print("A is bigger")
# elif b>a:
#     print("B is bigger")
# else:
#     print("A and B are equal")

# wap to find the greater number between 2 numbers
# wap to find the greatest number between 3 numbers
# wap to swap 2 numbers
# wap to find whether the given number is even or odd

# a = int(input("Enter first number: ")) 
# b = int(input("Enter second number: ")) 
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if(a>b):
#     print(f"no. {a} is greater")
# else:
#     print(f"no. {b} is greater")

# if(a>b and a>c):
#     print(f"no. {a} is greatest")
# elif (b>a and b>c):
#     print(f"no. {b} is greater")
# else:
#     print(f"no. {c} is greater")


# if(a>b and a>c and a>d):
#     print("a is greatest")
# elif(b>a and b>c and b>d):
#     print("b is greatest")
# elif(c>a):
#     print("c is greatest")
# else:
#     print("d is greatest")    
# -----------------------------------------------------
    
# a,b = b,a
# print(a,b)
# -----------------------------------------------------

# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")
# -----------------------------------------------------
# if(a>0):
#     print(f"{a} is positive")
# elif(a<0):
#     print(f"{a} is negative")
# else:
#     print(f"{a} is zero")

# ----------------------LEAP YEAR------------------------------
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

# ------------------FACTORIAL-------------------------

# f = int(input("Enter a number: "))
# fact = 1
# for i in range(f,0,-1):
#     fact = fact*i
# print(f"Factorial of {f} is {fact}")

#-----------------------prime no.---------------------

# num = int(input("Enter a number: "))
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count+=1
# if num == 1:
#     print(f"{num} is prime no.")
# elif count == 2:
#     print(f"{num} is prime no.")
# else:
#     print(f"{num} is NOT a prime no.")


# =========================================FOR LOOP==========================================

# for i in range(0,2):
#     print("Manish")

# a = 'This'
# for i in a:
#     print(i) #it will print T h i s line by line

# for i in range(0,4):
#     print(i) #it will print the index line by line


# a = 'This is my Python Class'
# for i in range(0,10):
#     print(a)

# for i in range(0,len(a)):
#     print(i)

# for i in range(0,len(a)):
#     print(a[i])
# ======================================================================================

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print('''+ = Addition
# - = Subtraction
# * = Multiplication
# / = Division''')
# print("*"*20)
# ch = input("Enter operator: ")
# print("*"*20)
# if ch=='+':
#     print(f"{a}+{b} = {a+b}")
# elif ch=='-':
#     print(f"{a}-{b} = {a-b}")
# elif ch=='*':
#     print(f"{a}*{b} = {a*b}")
# elif ch=='/':
#     print(f"{a}/{b} = {a/b}")
# else:
#     print("Worong operator entered !!!")


""" name, phone no., age, location , pin code, email id, alt. contact no, aadharcard. 
which disease?
list of doctors with their specialization
enter the choice
doctor name is been appointed for your consultantation 
"""

# import pyfiglet
# banner = pyfiglet.figlet_format("Surya Hospital")
# print(banner,end="")
# # print("*"*10 + "" + "*"*10)
# print("-"*70)
# print("*"*25 + "FIll Patient Details" + "*"*25)
# print("-"*70)
# name = input("Name: ")
# ph = int(input("Phone number: "))
# aph = int(input("Alternate Phone number: "))
# age = int(input("Age: "))
# loc = input("Address: ")
# pin = int(input("Pin Code: "))
# email = input("Email: ")
# aadhar = int(input("Aadhar No.: "))
# print("-"*30)
# while(True):
#     print('''[ 1 ]. Cold
# [ 2 ]. Feaver
# [ 3 ]. Stomachache
# [ 4 ]. Heart Problem
# [ 5 ]. Skin Problem''')
#     doc = {1:'Dr. Ramhesh', 2:'Dr. Suresh', 3:'Dr. Natwar', 4:'Dr. Mahesh', 5:'Dr. Ram'}
#     disease = int(input("Enter Number from above list your disease is related with: "))

    # if disease==1:
    #     print("Dr. Ramesh is appointed for your consultation")  
    #     break 
    # elif disease==2:
    #     print("Dr. Suresh is appointed for your consultation")   
    #     break 
    # elif disease==3:
    #     print("Dr. Natwar is appointed for your consultation")   
    #     break 
    # elif disease==4:
    #     print("Dr. Mahesh is appointed for your consultation")   
    #     break 
    # elif disease==5:
    #     print("Dr. Ram is appointed for your consultation")   
    #     break 
    # else: 
    #     print("Enter choice from given list !!!")

    # for key,value in doc.items():
    #     key = disease
    #     if key == 1:
    #         print(value)
    #         break
    #     elif key == 2:
    #         print(value)
    #         break
    #     elif key == 3:
    #         print(value)
    #         break
        
# -------------------------------------------------------------------

# ================================== FUNCTIONS =============================

# def func_name():
#     statements

# by default function returns None Value 

# def add(): #function defination
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     print(f"Sum of {a} and {b} is {a+b}")
# add() #Function call

# def add(): #function defination
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c = a+b
#     return c
# print(add()) #Function call

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# def sum(a,b):
#     print(f"{a}+{b} = {a+b}")
# def sub(a,b):
#     print(f"{a}-{b} = {a-b}")
# def mul(a,b):
#     print(f"{a}*{b} = {a*b}")
# def div(a,b):
#     print(f"{a}/{b} = {a/b}")

# print('''+ = Addition
# - = Subtraction
# * = Multiplication
# / = Division''')
# print("*"*20)
# ch = input("Enter operator: ")
# print("*"*20)
# if ch=='+':
#     sum()
# elif ch=='-':
#     sub()
# elif ch=='*':
#    mul()
# elif ch=='/':
#     div()
# else:
#     print("Worong operator entered !!!")

# sum(10,20)
# sub(14,3)
# mul(2,5)
# div(20,2)

# =============================================================================
# WAP to find whether a given no. is even or odd using function

# def func(a):
#     if a%2 == 0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")

# ch = 'y'
# while(ch != 'n'):
#     a = int(input("Enter any number: "))
#     func(a)
#     ch = input("Run again ? (y/n)")

# ==============================================================================
# WAP to find the largest out of three numbers using functions and check which is even or odd and also check if it is positive or negative


# ==============================================================================
# WAP to add two strings

# a = 'Python Class'
# b = 'BCA Student'
# # 1. using concatination
# print(a+' '+b)
# # 2. using join method
# print(' '.join([a,b]))

# WAP t odo the following things
# # 1. slice - Class from a
# print(a[7:len(a)])
# # 2. slice - BCA from b
# print(a[:3])
# # 3. make all letter capital in a and small in b
# print(a.upper())
# print(b.lower())

# ------------------------------------------------------------------------

# def Evenodd(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
# def posnev(n):
#     if n>0:
#         print(f"{n} is positive")
#     elif n<0:
#         print(f"{n} is negative")
#     else:
#         print(f"{n} is zero")
# def large(a,b,c):
#     if(a>b and a>c):
#         print(f"no. {a} is greatest")
#         Evenodd(a)
#         posnev(a)
#     elif (b>a and b>c):
#         print(f"no. {b} is greater")
#         Evenodd(b)
#         posnev(b)
#     else:
#         print(f"no. {c} is greater")
#         Evenodd(c)
#         posnev(c)
# a = int(input("Enter first no.: "))
# b = int(input("Enter second no.: "))
# c = int(input("Enter third no.: "))
# large(a,b,c)
# -----------------------------------------------------------------------------

# ==> Shorthand If else statement
# a = 10
# b = 20
# print("a is greater" if a>b else "b is greater")

# ==> Nested if else statememnt 
# a = 10
# b = 20
# if a != 0:
#     if a>b:
#         print("a is greater")
#         if a%2==0:
#             print("a is even")
#         else:
#             print("a is odd")
#     else:
#         print("b is greater")   
# else:
#     print("invalid entry")


# ==> Nested Loop
# r = 5
# for i in range(r):
#     for j in range(i+1):
#         print("*",end="")
#     print("\n")

# r = 5
# for i in range(r+1,0,-1):
#     for j in range(i-1):
#         print("*",end="")
#     # print("\n")

# r = 5
# for i in range(r):
#     for j in range(r-1):
#         print("*",end='')
#     print("\n")

# for i in range(5,0,-1):
#     print("*"*i)
#     i-=1
        
# ==> lambda function 
# func = lambda a,b,c: a+b+c
# func(10,20,30)


# mylist = [1,2,5,63,7]
# for i in mylist:
#     for j in mylist:
#         j = i+1
#         if i>j:
#             i,j = j,i
#             print(i,j)
# print(mylist)


#WAP to find SI and CI
# p = int(input("Enter principle value: "))
# r = int(input("Enter rate : "))
# t = int(input("Enter time in year: "))
# print (f" Simple interest is {(p*r*t)/100}")
# print (f" Compound interest is {p*((1+r)/100)**t}")
# print (f" Compound interest is {p*pow((1+r/100),t)}")


#WAP to find whether a no. is armstrong or not
# num = int(input("Enter a no.: "))
# x = str(num)
# for i in x:
#     sum = sum + i**3
# if sum == int(x):
#     print("Armstrong no.")
# else:
#     print("Not a Armstrong no.")

#WAP to find area of circle and rect.

# len = int(input("Enter length: "))
# wid = int(input("Enter width: "))
# side = int(input("Enter side of square: "))
# print(f"Area of square is: {side**2}")
# print(f"Area of rectangle is: {len*wid}")


#WAP to interchange first and last elements in the list
# mylist = [1,5,6,3]
# mylist[0],mylist[-1] = mylist[-1],mylist[0]
# print(mylist)

# WAP to swap two no. in list
# mylist = [1,5,6,3]
# mylist.index(5)
# mylist.index(6) 

#WAP to reverse a list
# mylist = [1,5,6,3]
# newlist = []
# for i in mylist[::-1]:
#     newlist.append(i)
# print(newlist)

# num = 121
# x = str(num)
# # for i in x:
# #     n = x(int(len(x),0,-1))
# rev = ''.join(reversed(x))

# if num == rev:
#     print("Yes")
# else:
#     print("No")

# WAP to find whether a number is palindrome or not 
# x = str(num)
# rev = x[::-1]
# rev = 
# if num == rev:
#     print(f"{num} is a palindrome number")
# else:
#     print(f"{num} is a NOT a palindrome number")


# --------------------------------------------------------------------------------

# PRACTICE QUESTIONS
'''
1. Who developed python ?
Ans. G.V Rossom

2. Is python case senditive while dealing with identifier?
Ans. Yes

3. What is the extension of python file.
Ans. .py

4. Output?
4+3%5
Ans. 7

5. Output?
print(2**3 + (5+6)**(1+1))
Ans. 129

6. Output?
var = 10
print(type(var))
var = 'Hello'
print(type(var))
Ans. Int and Str

7. Output?
print(type(5/2))
print(type(5//2))
Ans. Float and Int

8. Output?
a = [1,2,3,4,5]
sum = 0
for i in a:
    sum = sum + i
print(sum)
Ans. 15

9. WAP to find whether 's' is available in a string or not

a = 'This is me'
count = 0
for i in a:
    if i=='s':
        count += 1
print("Available {count} times")

10. WAP to convert a tuple into a list.
tp = (1,2,3,4)
my_list = list(tp)
print(type(my_list))

11. WAP
1
12
123
1234
12345

'''
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print('\n')

# l = []
# for i in range(1,6):
#     l.append(i)
#     print(l)

# l = ''
# for i in range(1,6):
#     l = str(l)+str(i)
#     print(l)

















































































































# ************************************ START ************************************************

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

""" 
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
 """

from pprint import pformat

from cycler import V


a = 21
b = 290
c = 3
d = 100

# a>b? (a>c? (a>d? a:d) : (a>d? c:(d>c? d:c))) : (b>c? (b>d? b:d) : (b>d? c:(d>c? d:c)))

# if a>b and a>c and a>d:
#     print(a)
# elif a>b and a>d:
#     print(c)
# elif a>b and d>c:
#     print(d)
# elif b>c and b>d:
#     print(b)
# elif b>d:
#     print(c)
# elif d>c:
#     print(d)
# else:
#     print(d)

# a,b,c,d

# if a>b: #--------bacd 
#     if a>c: #--------bcad 
#         if a>d: #--------bcda
#             print('a: ',a)
#         else: #--------bcad
#             print('d: ',d)
#     else: #--------bacd
#         if a>d: #--------bdac
#             print('c: ',c)
#         else: #--------bacd
#             if d>c: #--------bacd
#                 print('d: ',d)
#             else: #--------badc
#                 print('c: ',c)
# else: #--------abcd
#     if b>c: #--------acbd
#         if b>d: #--------acdb
#             print('b: ',b)
#         else: #--------acbd
#             print('d: ',d)
#     else: #--------abcd
#         if b>d: #--------adbc
#             print('c: ',c)
#         else: #--------abcd
#             if d>c: #--------abcd
#                 print('d: ',d)
#             else: #--------abdc
#                 print('c: ',c)