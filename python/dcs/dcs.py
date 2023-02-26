"""
What is Python?
Python is an interpreted, high level and object oriented programming language which is also used as a scripting language to connect existing components together.

Some key Differences
	1. High/Low level languages
		High level lang are more programmer friendly while low level languages are more machine friendly
	2. Interpreted and compiled languages
		A. In compiled language,
			• The machine directly translates the code in compiled version.
			• Compiler is used as a mediator to translate source code to machine code
			• Compiler compile the whole code in one go and then gives error(if any).
		B. In interpreted language,
			• the code is read and interpreted in real time.
			• Interpreter is used as a mediator to translate source code to machine code
			• Interpreter executes the code line by line and gives error (if any) and stop further execution
	3. Programming and Scripting language
		Scripting language do not require an explicit compilation step. So all scripting languages are programming languages but all programming languages are not scripting languages.
	4. Platform Dependent/Independent language
		Those languages in which program is written on one platform (OS) can be run on any other platform (OS) with the same output are Platform Independent Languages. While the languages in which program is written for some specific platform (OS) and cannot be run on other platforms are Platform dependent Languages.

======= IMPLEMENTATION OF PYTHON ========
# and PyPy which was written in Python itself.
The interpreter of python was officially written in C lang known as CPython. But there are several more implementation of python like Jpython which was written in Java, IronPython which was written in C

** This info will be helpful when we use different interpreters in some special situations like many burp extensions want us to provide them Jpython interpreter

======= Compilation Process ========
Source code (.py) ==> [internally] ==> byte code (.pyc) ==> [internally] ==> machine code (0,1)

2**3 -- exponential
10%2 -- modulos
10/3 = 3.3 -> this is floating point division or simple division
10//3 = 3 -> this is integer division or floor division
9.0//2.0 = 4.0 -> this is integer division but since the operands are in float, it'll give result in float


======== Like BODMAS, python follows PEMDAS ==========
P - parenthesis ()
E - exponents **
MD - Multiplication and Division (solve left to right)
A - addition
S - subtraction

====== Comments ========
	Comments are the nothing but code itself which is ignored by the interpreter. Generally comments are used to gives some notes or additional info to other user within the actual source code.

	1. Single line comment #this is ex of single line comment
	2. Multiline comment
	''' developer : ayush
	age:40
	gender: male
	'''

====== Variable ========
	• Variables are the containers which stores some data.
	• Variables can be assigned to other variables.
	>>>ayush=5
	>>>aman = ayush
	>>>ayush = 7
	>>>ayush = 0
	>>>a,b = 3,4

	• Variables can be reassigned with another datatype
			A = 5
			A = 5.2
			A = "yash"
		**This is known as dynamic typing.

****• Rules of declaring variables:
		1. Var. name must start with letter or underscore
		2. Var. name other than 1st character must contain only letters, numbers or underscore.
		3. Var. name cannot have any space.

	• Generally programmers define variables like this-
		Is_Male = 1
		IsMale = 1
		__password__ = 1
		__name__ = 1 -- ye find karne me help karta hai ki jo script run ho rahi hai wo direct ho rahi hai ya dusre file se import hokar

======= DATATYPES =======
		1. Int (integer values)
		2. Float (decimal values)
		3. Bool (true or false / yes or no)
			isMale = false
			isMale = false -- wrong(first letter of true and false must be capital)
		4. Complex
			X = 3e+5j
		5. None (same as NULL)
			isPremium=None

	String: sequence of unicode characters
		a. Single line string: can be declared with single or double quotes
			'hello'
			"hello"
		b. Multi line string: declared with triple single quotes
			Name = '''yash
					Parwal
					'''
			Print(Name)

	NOTE: string can be multiplied by integer but cannot perform addition.

	Escape sequence chars.
		\char ==> char has some meaning
		\n ==> n means new line
		\\ ==> \ means backslash
		\t ==> t means tab


Print(This\n\tis\n\t\tMetaxone\n\t\t\tSolutions)

'Ayush"Pathak'
'Ayush"Pathak'

"Ayush'Pathak"
"Ayush'Pathak"

'''Ayush pathak" '''
'Ayush pathak" '

''' Ayush ' pathak '''
" Ayush ' pathak "

"Ayush \" Pathak"
'Ayush " Pathak'

'Ayush \' Pathak'
"Ayush ' Pathak"

"""
# name = 'yash'
# # ageS = '19' #if this is number then it'll not be added to string
# ageN = 19 # this is integer
# # print(name + ageN) #str+int=error
# print(name,ageN) #we can join like this but cannot add using + operator

# # print("hello",end="") #end="" is hidden due to which new print function executes from next line

# \__________________________________ PYTHON - 2 (25 sept) __________________________________/

# first = 'yash'
# last = 'parwal'
# age = 19
# print(f"my name is {first} {last} and I am {age} years old") #docstring

# name = "yashparwal"
# print(name)
# print(name[2]) #char at index 2
# print(name[1:3]) #start:stop index (stop index is not included)
# print(name[:3]) #0 to 3 but 3 is not included

# # Negative indexing -- index starts from last (reverse)
# print(name[0:-1]) # -1=last , -2=last-1

# ==================================TYPECASTING=============================================

# ==> Converting one datatype into another
# Implicit ==> done by interpreter like 9//3.0=3.0 ==> 9 will be converted into 9.0
# Explicit ==> done by programmer like int to str ==> str(var_name)
# first = 'yash'
# last = 'parwal'
# age = 19
# # print(first + last + age) #error
# print(first + last + str(age)) #typecasting

# int = 40.1
# # print(str(int)) #correct,, int varirable it typecasted into string
# '''
# print(int(int))
# error,, because here int is not int anymore, main work of int is replaced with 40.1 so interpreter will see it like this: print(40.1(40.1)) and this is not a correct syntax
# '''
# str = None
# print(str(int)) #NULL type variable is not callable

# no = input("Enter no: ") #bydefault input is of string type in python, so have to do some typecasting here like this...
# no = int(input(f"Enter number: "))
# print(f"number is {no}")
# print(type(no))
# print(round(no/3)) #will give round off value
# print(round(no/3,2)) #will give value upto 2 decimal places

# ================================Conditional Statements=====================================

# If condition:
# 	Statements
# Else:
# 	Statements

# a = 3
# b = 4
# if a<b:
#     print("Yes")
# elif a==b:
#     print("Equal")
# else:
#     print("No")

# if "yash"=="yaSh": #false
#     print("true")
# if 4=="4": #false
#     print("true")

# -----------------------------------THRUTHNESS----------------------------------------------

# in binary: 1 -> True and 0 -> False
# False items are: 0, Empty Objects, Empty String, None

# if 0:
#     print("true")
# else:
#     print("false")

# ====================================== Logical Operators =====================================
# Three logical operators are "and", "or" and "not".
# l = 5
# m = 10
# n = 15
# if l<m and m<n: #both conditions should be true for true output
# 	print("Alright")

# if l<m or m>n: #either of the condition is true, the output will be true
# 	print("Yeeees!! Alright!")

# if not True:
# 	print("Condition is now acting as false i.e this statement will not be printed !!!")
# if not l>m:
# 	print("l>m is false but still this will be printed becoz 'not' is making this true by telling that yesss this is true that l is not greater than m ")

# 10 and 10 -- 10 (True)
# 10 and 20 -- 20 (True)
# 20 and 10 -- 10 (True)
# True and True -- True
# True and False -- False
# False and True -- False
'''If both conditions are true, it will give the last value in case of "and" and first value in case of "or".'''

# if(10 and 20):
# 	print("yes")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TASK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
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
'''


# \__________________________________Python - 3 (2nd oct.)_____________________________________/


# String multiplication
# print("*"*5)
# print("yash"*5)

# ---------------------------------------is keyword---------------------------------------------
# whether the two variables refering to same object
# a=234.1
# b=234.1
# if a is b: #this will execute becoz a and b both are referencing to same location of 234.1
#     print("yes")
# else:
#     print("no")

# c = [1,2]
# d = [1,2]

# if c is d: #this checks this- if(id(c) == id(d)), and list always have diff. memory locations
#     print("right")
# else:
#     print("Wrong") #this will execute

# if c == d: # == checks the values
#     print("right") #this will execute
# else:
#     print("Wrong")

# c=d
# we can see their memor location by
# print(id(c)) #same
# print(id(d)) #same
# if c is d: #this
#     print("right") #NOW this will execute becoz now we assigned d into c, so these both will have same location
# else:
#     print("Wrong")

# SO WHAT IS THE DIFFERENCE BETWEEN "IS" & "=="
# == (checks for equality) compares the values, if they are equal or not WHILE is (checks identity) compares the memory location in terms of being the same object in the memory.


# a = 'yash'
# b = 'yash'


# ====================================LOOPS IN PYTHON===========================================
'''
==> For Loop:
syntax -
	For item in iterable_object:
		#code

Item: hold current value
Iterable_object: collection of values

==> While loop:
Syntax -
	While booleam_expression:
    #code
'''
# for i in range(1,5):
#     print(i)
# for i in range(1,5):
#     print("yash")

# ------------------------------------range()------------------------------------------------
# range(start,stop,step)
# for i in range(1,10,2):   #print 1 to 10 with gap of 2
#     print(i)
# for i in range(5):   #print 0 to 4, it will take
#     print(i)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ARMSTRONG NO. >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# no = 153
# n = no
# sum=0
# while n!=0:
#     rem = n%10
#     sum = sum + (rem*rem*rem)
#     n = n//10

# if(no==sum):
#     print("Armstrong no.")
# else:
#     print("Not an armstrong no.")

# OR

# no = str(no)
# for i in no:
#     sum = sum + int(i)**3
# if(sum == int(no)):
#     print("Armstrong no.")
# else:
#     print("NOT an armstrong no.")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< STAR PATTERNS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for i in range(4):
#     for j in range(i+1):
#         print("* ",end="")
#     print("\n")

# for i in range(5):
#     print("* "*i)

# for i in range(1,6):
#     print(" "*(5-i) + ("*"*i))

# j=1
# for i in range (1,6):
#     if i==5:
#         print(" "*(5-i) + "|"+"*"*j+"|" + " "*(5-i))
#     else:
#         print(" "*(5-i) + "/"+"*"*j+"\\" + " "*(5-i))
#     j=j+2
# for i in range(1,5):
#     print(" "*4 + "|*|")

# new = 0
# for i in range(1,5):
#     print(" "*(5-i) + "*"*new)
#     new = new+2


# new = 0
# for i in range(0,7,2):
#     print(" "*(i-new) + "*"*(7-i))
#     new = new+1
# these 👇 and ☝ both are same
# star = 7
# for i in range(5):
#     print(" "*i + "*"*star)
#     star -= 2

# a = 5
# while a>1:
#     print(a)
#     a=a-1

# =====================================JUMP STATEMENT==========================================
# 1. break statement -- exit from the loop
# 2. continue statement -- ignore the further execution and go over next iteration

# for x in range(1,10):
#     if(x/3==2):
#         # break
#         # continue
#         # pass #pass is not a jump statement
#         print(x)

# for i in range(1,101):
#     if(i%2 == 0):
#         continue
#     else:
#         print(i)

# if not 5>3:
#     print("done")

# _______________________________________________________________________________________________

# 2/10/22

# ----------------------------------------------- NOT -------------------------------------------
# if not 5>3:
#     print("Done")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TASK (in dcstask.py) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# ===============================================LISTS===========================================
"""
List: collection of diff. items of diff. datatypes
grocery = ["harpic", "vim", "deo", "bhujiya", "lollypop", 56, True]
* any type of data can be entered in list
* List is mutable
"""
# x = list(range(1,5))
# x = list()
# if [""]:  #empty list means false
#     print("x")


# data = [1,2,3,"Hello",True]
# print(len(data))
# print(len(143)) #integer has no length

# print(data[0])
# print(data[2])
# print(data[9]) #error, index out of range
# print(data[-1]) #negative indexing

# if 2 in data:
#     print("yes") # '2' is present in data or not
# for i in data:
#     print(i)
# ------------------------------------ LIST FUNCTIONS ----------------------------------------
# ==> 1. append()

# data.append(4) #add the data as a single item at last of the list
# print(data)
# data.append([4,5]) #we can provide list within a list
# print(data)
# print(data[-1]) # will give oblect at index(-1) of list that is [4,5]
# print(data[-1][0]) # will give index0 object of index(-1) object if the index(-1) object is a list othervise it'll give error
# item of a list within a list

# ==> 2. extend()
# a = [10,11,12,13]
# data.extend(a) #add list a into data with elements of list 'a' as individual items
# data.extend([4,5]) #add list [4,5] to the data as individual items like 4, 5
# print(data)

# ==> 3. insert(index_number,object_to_add)
# data.insert(3,"hlo") #hlo will be inserted at 3rd index
# print(data)

# ==> 4. clear
# data.clear() #do empty the list


# data = [1,2,3,"Hello",True,2,2]

# for i in data:
# 	data.remove(i)
# 	data.insert(0,i)
# print(data)

# ==> 5. pop()
# print(data.pop()) #remove the last item of the list and gives that item
# this means that it not just remove but also store the poped item in memory (or if we give any var, so in var)

# data.pop(3) #pop the element from index three
# data.pop(10) #IndexError: pop index out of range
# print(data)

# ==> 6. remove()
# print(data)
# data.remove(3) #will remove the defined element like here '3' will be removed
# data.remove('gg') #'gg' is not in the list, so it will give ValueError
# print(data)

# test = [3,2,1,2,5]
# test.remove(2) #removes only the first occurance
# print(test)

# ==> 7. index()
# print(data.index(3)) #three is on which index? (returns th index nummber)
# print(data.index(10)) #will return ValueError that 10 is not in the list.
# index(what_to_find , start_index , end_index)
# print(data.index(3,1,4)) #find 3 between one and four index.

# ------------------------------- PROBLEM WITH NEGATIVE INDEXING ------------------------------
# NOTE: in negative indexing, first it it converted into equivalent positive index and then data is inserted
# temp = [1,2,3]
# temp.insert(-1,4) #4 should be added at last ==> [1,2,3,4] but NO....
# ---------------------------------------------------------------------------------------------


# ==> 8. count(2) element 2 is how many times. That is 3 times.
# print(data.count(2))
# print(data.count(9)) #will give '0' as output

# ----------------------to remove duplicates of a particular item.---------------------------
# for i in range(data.count(2) - 1):
# 	data.remove(2)
# print(data)

# ==>
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

# ============================ LIST comprehension ============================
# It lets us create new lists based on sequences and ranges

# multiple = []
# for i in range(1,11):
# 	multiple.append(5*i)
# print(multiple)

# OR

# multiple = [5*i for i in range(1,11)]
# print(multiple)

# languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C', 'C++']
# length = [len(i) for i in languages]
# print(length)

# temp = [x for x in range(0,100) if x%3==0 ]
# print(temp)

# mylist = [10,3,5,6,4,8,0]
# mylist.sort()
# mylist.reverse()
# print(mylist)
# print(new.reverse())

'''_____________________________________________________________________________________'''

# ====================================STRING==============================================
# STRING FUNCTIONS (Note: these func do not modify the original string)


# # PYTHON STRING METHODS https://www.w3schools.com/python/python_ref_string.asp

# name = "yash parwal"

# # 1. capitalise -- capital the first letter of string
# name.capitalize()

# # 2. count -- coubt the no of letters in a string
# name.count("a")

# # 3. endswith -- S.endswith(suffix[, start[, end]]) -> bool
# # Return True if S ends with the specified suffix, False otherwise.
# name.endswith("l")

# # 4. find -- print the first ouucurance of the provided letter in string
# name.find("h")
# # if not there, it will return -1

# # 5. index -- 	Searches the string for a specified value and returns the position of where it was found


# # if not there, it will give error due to which further program execution will stop

# # 6. Replace -- replace all occurance of 1st item with second item
# name.replace("a","b")

# # 7. upper and lower
# name.upper()
# name.lower()

# # ******** 8. strip -- Return a copy of the string with leading and trailing whitespace removed.
# name.strip()

# # 9. exit

# # 10. encode & decode -- Encode the string using the codec registered for encoding.
# # Convert the string into byte/binary from
# name.encode()
# name.decode()


# =======================================DICTIONARIES=======================================
# DICTIONARIES constis of keys and value pairs

# test = {
#     "name":"yash",
#     "age":19,
#     # IsMale:True
#     2:25
# }

# or

# data = dict(name="Yash", age=15)

# print(data["name"])
# print(data["age"])

# for key,value in test.items():
#     print(key,value)
# for key in test.keys():
#     print(key)
# for value in test.values():
#     print(value)

# print("name" in test) #true ; search in keys
# print("yash" in test) #false ; search in keys
# print("yash" in test.values()) #true ; search in values

# test.clear()
# print(test)

# test2 = test.copy()
# print(test2)

# di = {"name":"yash",
#     "age":19,
#     # IsMale:True
#     2:25}
# {}.fromkeys(["name","age","anything"],1)
# print(di)


# print(test.get("name"))
# print(test["name"])

# print(test.pop("name")) #pop from begning
# print(test.pop("xyz")) #keyvalue error becoz xyz is not in dictionary.
# print(test)
# print(test.popitem()) #pop from end
# print(test)

# data={"name":"ayush",
#       "IsMale":True,
#       2:44
#       }
# new={"name":"kid",
#      "gender":"male"
#      }

# # data.update(new)
# # print(data)

# data["gender"]="MALE"
# #this will also update the dict like .update() but this is shortcut as in .update we have to create new dict but here we can directly give key:value
# print(data)

# DICTIONARY COMPREHENSION

# data = {"a":10, "b":20}

# new = {x for x in data} #this will create set not dict
# print(new)
# new = {key:value for key,value in data.items()} #this will create dict
# print(new)

# new={key+" done":value/5 for key,value in data.items()}
# print(new)

# new={key+" done":value/5 for key,value in data.items() if value==20}
# print(new)

# new={key+" done":(value/5 if value==20 else value*5) for key,value in data.items()}
# print(new)

# items = {"pen":10,"book":90,"copy":50,"Bag":200}
# for key,value in items.items():
# 	print(f"{key} : {value}")


# =========================================TUPLE==============================================
# TUPLE -- collection of item
# * Tuple is immutable i.e cannot be modified once created
# * Tuple is faster than list
# * used when we want the data to be constant always like date of acc. created, months in year
# name = ("yash", 1,2, True)
# we can create tuple like this also
# name = tuple([1,2,3,4])

# * We can use tuple as the key of a dictionary but cannot use list for the same
# * Slicing and nesting is same like we did in list

"""
Iterating Over Lists Using Enumerate

When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

"""

# =========================================SETS==============================================
# SETS - well defined collection of distinct objects
# Sets have no order
# Sets cannot be accesed by index no.
# Sets objects can be iterated
# A = {1,2,True,"1"}
# print(A)
# B = set({}) #we can create set like this also
# a = {1,2,3}
# a.add(4)
# a.remove(1)
# a.remove(6) #error becz, 6 element is not there
# a.discard(6) #NO error, even if 6 is not there. it wll still not give error like that happened in .remove
# b = a.copy()
# print(b)
# a.clear()

# OPERATION ON STES
# 1. union a|b
# 2. intersection a&b

# c = {3,4,5}
# print(a|c) #union
# print(a.union(c))
# print(a&c) #intersection
# print(a.intersection(c))

# FILE HANDLING

# file = open("file_name", "mode")

# file = open("dcs.txt","r")
# data = file.read() #read complete data
# data = file.read(4) #read
# data = file.readline() #read one line only
# data = file.readlines() # gives a list with each line a an object of list
# print(data)

# ======================================= FUNCTION ===============================================
# - A part of code that does some specific task each time it is called
# - It can accept and return data upon calling
# - Doesn't gets executed unless called
# *- If you don't use return at the end of the function, python will auto return None
# *- Once a return statement is executed, no other code after that statement (within the function) will execute

# def name_of_function(parameters):
# # some_code

# def hello():
#     print("hello")
# hello()

# def hello():
#     return "hello"
# a = hello()
# print(a)

# def name(n,a,b): #these are parameters
#     print(n,a,b)
# name("yash",2,1) #these are arguments

# def add(a,b):
#     return a+b
# print(add(1,2))

# def add(a,b):
#     return a+b
# print(add(a=2,b=1)) #keyword arguments

# def add(a=4,b=5): #defaule parameters but these will overwrite if arg. are provided othervise not
#     return a+b
# print(add(2,1)) #arguments

# def do(func,a): #function can have other functiona as parameter
#     func(a)
# def hello(n):
#     print(n)

# do(hello,1) #we can pass functions also as argument

# =================================== 15/10/22 =============================================

# ----------------------------------VAriablle SCOPE -------------------------------------

# * Each variable has its own scope.
# * Global Variable -- variablles defined outside the main functions
# * Local Variable -- variablles defined within the main functions

# global keyword: global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.
# We can actually access global variables inside any function but we can't manipulate them, that's why global keyword is important.

# x,y = 7,4
# def add():
# 	x,y = 5,3
# 	print(x+y)
# add()

# def add():
# 	x,y = 1,2
# 	print(x+y)
# 	def again():
# 		print(x+y)
# 	again()
# add()

# x,y=6,7
# def add():
#     x,y=1,2
#     print(x+y)
#     def again():
#         nonlocal x,y
#         print(x+y)
#     again()
# add()

# ----------------------------- Function Documentation ---------------------------------------

# def sum(x,y):
# 	""" This functio is used to add 2 values"""
# 	return (x+y)
# sum(10,20)
# print(sum.__doc__) #will show the documentation of sum func.

# print(print.__doc__) #will show the documentation of print func.

# -------------------------------- Special Parameters ----------------------------------------
# ------------------------------- * and ** as parameters -------------------------------------

# *args (arguments) -- creates a tuple
# **kwargs (keyword arguments) -- creates a dictionary

# def mul(x,y,*args,**kwargs): #normal parameters,*args,**kwargs
# 	print(x,y,args,kwargs)

# mul(1,2,3,4,5,6,a=10,b=11,c=12,d=13) #normal parameters,*args,**kwargs


# ============================= Lambda Func. (Anonymous Functions) ==========================


# def add(x,y):
# 	return (x+y)


# add = lambda x,y:x+y #one liner function
# print(add(1,2))

# def do(x,y,func):
# 	ans = func(x,y)
# 	print(ans)
# do(1,2,lambda x,y:x+y)

# =========================== Some Important Built Func. ================================

# a = [1,2,3,4,5]

# for i in range(5):
# 	a[i] = a[i] +2
# print(a)

# 1. map() --  executes a function for each in an itrable/collection.
# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

# a = map(lambda x:x+2,a)
# print(list(a))


# 2. filter() -- elements are based on certain condition. and returns those elements for which function/condition is true
# a = filter(lambda x:x%2==0,a)
# print(list(a))

# name = ["Ayush","Aman","Srishti","Harsh"]

# new = filter(lambda x:len(x)>4,name)
# # print(list(new)) #it will reset
# new = list(new)
# new = map(lambda x:"Your instructor is "+x,new)
# print(list(new))

# 3. any() -- if any one item of list is true, it will return true othervise false
# 4. all() -- all the elements of list should be true, then only it will return true otherwise false

# a = [4,2,6,7,1,2]
# print(sorted(a))
# print(sorted(a,reverse=True))
# print(max(1,7,44,24,56,7))
# print(max('a','b'))
# print(min('a','b'))

# \_____________________________________PYTHON-9 29oct.___________________________________________/

# ========================================== OOP ================================================

# Models some process or thing in the world as class or object

# Blueprint for object that can contain methods(funcrions) and attributes(variables)
# When a function is associated with a class, then it it knows as method and when variables are associated with class, then these are known as attributes.

# ------------------------------------------ INSTANCE ------------------------------------------
# * These are nothing but objects thet are constructed from class blueprint that contain their class properties.
# * Any no. of objects or instances can be created of a class.
# * All objects are independent of each other.

# ---------------------------------------- PROPERTIES ------------------------------------------
# 1. Encapsulation -- Grouping of public/private methods and attributes in a programmiatic class making abstraction possible.(wrapping data and the methods that work on data within one unit.)

# 2. Abstraction -- Exposing only revelent data to outside and hiding the private attributes and methods's inner workings from users.

# class Users:
# 	def func():
# 		print("hello")


# \_____________________________________PYTHON-10 30oct.___________________________________________/

# 3. Inheritance -- OOP ability to define a class which inherits from another class (base or parent class)

# class User:
# 	def tell(self):
# 		print("I am a user")

# class Admin(User):
# 	print("I am also an Admin")

# obj = Admin()
# obj.tell()

# If we use super() method while multi inheritance python follows MRO(Method resolution) to find and eecute method from parent class

# 4. Polimorphism -- An object can take-on many(poly) forms(morph)

# Special or Magic methods

# class Test:
#     def __init__(self,first):
#         self.first=first
#     def __repr__(self):
#         pass
#     def __len__(self):
#         return 5
#     def __add__(self,x):
#         return Test(self.first+x.first+y.first)
# obj=Test(2)
# obj2=Test(4)
# obj3=Test(5)
# final = obj+obj2+obj3
# print(final.first)

# Iterator --
# Iterablle -- An object which will return an itertor when iter() method is called on it.

# generators ==> subsets of iterators
# Every genertor is iterator but not vice versa
# generatores takes much less space and time.
# Generators are created with:
# 1. generttor functions ("yield" keyword)
# 2. generator expression

# def count(max):
# 	count = 1
# 	while count <= max:
# 		print(count)
# 		count+=1
# 	return count
# count(5

# Decorators -- These are functions that wrap other functions and enhance their behaviour

# def do(func,x,y):
#     func(x,y)
#     def final():
#         print("done")
#     return final

# def add(x,y):
#     print(x+y)

# do(add,2,3)()


# ------------------------------------------------------------------------------------------

#!/bin/env python3

# server programming

# import socket

# def main(HOST, PORT):
#   s = socket.socket()
#   try:
#      s.bind((HOST, PORT))
#   except:
#     print("choose a different Port!")
#     exit()
#   print("[+] listining...")
#   s.listen()
#   sock_fd, conn = s.accept()
#   print("[+] Connection ESTAB", conn)
#   while(True):
#     tmp_bytes = sock_fd.recv(1024)
#     print("[+] Recvd:", tmp_bytes.decode().strip())

# main("127.0.0.1", 80)

# ---------------------------------------------------------------------------------

# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize//block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize%block_size
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return block_size*(full_blocks+1)
#     return block_size*(full_blocks)

# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192


# ---------------------------------------------------------------------------------

# def replace_ending(sentence, old, new):
# 	# Check if the old string is at the end of the sentence

# 	if sentence.endswith(old) is True:
# 		# Using i as the slicing index, combine the part
# 		# of the sentence up to the matched string at the
# 		# end with the new string
# 		# i = len(old)
# 		new_sentence = sentence[:-len(old)] + new
# 		return new_sentence

# 	# Return the original sentence if there is no match
# 	return sentence

# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# # Should display "The weather is nice in April"


# ---------------------------------------------------------------------------------

# def convert(sec):
# 	h = sec//3600
# 	remaining_sec = sec%3600
# 	m = remaining_sec//60
# 	s = remaining_sec%60
# 	return h,m,s

# result = convert(5000)
# print(result)

# ---------------------------------------------------------------------------------
# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.

# def skip_elements(elements):
# 	result = []
# 	for index, value in enumerate(elements):
# 		if index%2 == 0:
# 			result.append("{}".format(value))
# 		else:
# 			continue
# 	return result

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


"""
filenames = ["program.c", "stdio.hpp",
    "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for files in filenames:
    if files[-3:] == "hpp":
        newfiles = files[:-3] + 'h'
        newfilenames.append(newfiles)
    else:
        newfilenames.append(files)
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

"""
# -------------------------------------------------------------------------------------------------

"""
# Question 3
# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example:
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += '-'
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

"""

# --------------------------------------------------------------------------------------------


# def group_list(group, users):
# 	members = ''
# 	for user in users:
# 		members += user + ', '
# 	return group + ': ' + members
# # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))

# def group_list(group, users):
# 	members = ', '.join(users)
# 	return f"{group}: {members}"
# # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))

# -----------------------------------------------------------------------------------------------

# def email_list(domains):
#     emails = []
#     for domain, users in domains.items():
#         for user in users:
#             # print(user)
#             emails.append(user+"@"+domain)
#     return (emails)


# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
#       "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# -----------------------------------------------------------------------------------------------

# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	group_list = []
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			if user in user_groups:
# 				user_groups[user].append(group)
# 			else:
# 				user_groups[user]=[group]
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary

# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

# -----------------------------------------------------------------------------------------------

# def format_address(address_string):
#     house_no = 0
#     house_name = ''
#     string = address_string.split()
#     for x in string:
#         if x.isdigit():
#             house_no += int(x)
#         else:
#             house_name += x + ' '

#     print(house_no , house_name)
#     return "house number {} on street named {}".format(house_no, house_name)


# print(format_address("123 Main Street"))

# -------------------------------------------------------------------------------------------

# Question 7
# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   for letter in text.lower():
#     # Check if the letter needs to be counted or not
#     if not letter.isalpha():
#       continue
#     elif letter not in result:
#       result[letter] = 1
#     else:
#       result[letter] += 1

#     # Add or increment the value in the dictionary
#     # ___
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# ----------------------------------------------------------------------------------

# mydict = {"one":3, "two":4, "three":10}
# sum = 0
# test = mydict.values()
# # print(test)
# for x in test:
# 	sum  = sum + x
# print(sum)

# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	# for key,val in basket.items():
# 	# 	total += val
# 	prices = basket.values()
# 	for price in prices:
# 		total += price
# 	return round(total, 2)

# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44


# def combine_lists(list1, list2):
#     # Generate a new list containing the elements of list2 # Followed by the elements of list1 in reverse order
#     new_list = list2
#     for i in reversed(list1):
#         new_list.append(i)
#     return new_list


# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))

# ----------------------------------------------------------------------------------------------
# ----------------------------------------OOPS (Coursera)---------------------------------------

# class Flower:
#   color = 'unknown'

# rose = Flower()
# rose.color = 'red'

# violet = Flower()
# violet.color = 'blue'

# this_pun_is_for_you = 'this_pun_is_for_you'

# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you)

# --------------------------------------------------------------------------------------------------
"""
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.elevation > return_city.elevation:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3
	#Format the return string
	if return_city.name:
		return "{}, {}".format(return_city.name, return_city.country)
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

"""
# -------------------------------------------------------------------------------------------------

# class Piglet:
#     name = ""
#     def speak(self):
#         print(f"Oink! Oink! I am {self.name}")

# hamlet = Piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()

# class Piglet:
#     years = 0
#     def pig_years(self):
#         return self.years * 18

# piggy = Piglet()
# print(piggy.pig_years())
# piggy.years = 2
# print(piggy.pig_years())

# --------------------------------------------------------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, yr):
#         self.name = name
#         self.year = yr
        
#     def __str__(self):
#         return f"My name is {self.name} and I am {self.year} years old."
#     def greeting(self):
#         # Should return "hi, my name is " followed by the name of the Person.
#         return "hi my name is {}".format(self.name)


# # Create a new instance with a name of your choice
# some_person = Person("yash",20)
# print(some_person) #if we call the instance direct it will return the memory location that where this object is located at. So we need to define __str__ (self) in the class.
# # <__main__.Person object at 0x000001FB549CF510>
# print(some_person.greeting())

# --------------------------------------------------------------------------------------------------------

# class Elevator:
#     def __init__(self, bottom, top, current):
#         """Initializes the Elevator instance."""
#         self.bottom = bottom
#         self.top = top
#         self.current = current
#     def __str__(self):
#         return "Current floor: {}".format(self.current)
        
#     def up(self):
#         """Makes the elevator go up one floor."""
#         if self.current < self.top:
#             self.current += 1
#     def down(self):
#         """Makes the elevator go down one floor."""
#         if self.current > self.bottom:
#             self.current -= 1
#     def go_to(self, floor):
#         """Makes the elevator go to the specific floor."""
#         self.current = floor

# elevator = Elevator(-1, 10, 0)

# elevator.up() 
# print(elevator.current) #should output 1

# elevator.down() 
# print(elevator.current) #should output 0

# elevator.go_to(10) 
# print(elevator.current) #should output 10

# # Go to the top floor. Try to go up, it should stay. Then go down.
# elevator.go_to(10)
# elevator.up()
# elevator.down()
# print(elevator.current) # should be 9
# # Go to the bottom floor. Try to go down, it should stay. Then go up.
# elevator.go_to(-1)
# elevator.down()
# elevator.down()
# elevator.up()
# elevator.up()
# print(elevator.current) # should be 1

# elevator.go_to(5)
# print(elevator)


# --------------------------------------- INHERITANCE -------------------------------------------

# class Fruit:
# 	def __init__(self, color, flavor):
# 		self.color = color
# 		self.flavor = flavor

# class Apple(Fruit):
# 	pass
# class Banana(Fruit):
# 	pass

# jnc = Apple("red", "tart")
# raj = Banana("yelllow", "sweet")

# print(jnc.color)
# print(jnc.flavor)
# print(raj.color)
# print(raj.flavor)

# -----------------------------------------------------------------------------------------------------

# class Animal:
# 	sound = ''
# 	def __init__(self, name):
# 		self.name = name
# 	def speak(self):
# 		print(f"{self.sound}! I am {self.name}")

# class Pigllet(Animal):
# 	sound = 'Oink'

# anny = Pigllet("piggy")
# anny.speak()

# class Cow(Animal):
# 	sound = "Moooo"

# milky = Cow("krishna")
# milky.speak()

# -----------------------------------------------------------------------------------------------------

# __init__ is a method inside the repository class, that's making use of the values method in the dictionary class and it's accessing the size attribute in the package class. That is the power of composition. 
class Repo:
	def __init__(self):
		self.packages = {}
	def add_pkg(self, package):
		self.packages[package.name] = package
	def total_size(self):
		result = 0
		for pkg in self.packages.values():
			result += pkg.size
		return result

# -----------------------------------------------------------------------------------------------------

# QUESTION: Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

# class Clothing:
#   stock={ 'name': [],'material' :[], 'amount':[]}
#   def __init__(self,name):
#     material = ""
#     self.name = name
#   def add_item(self, name, material, amount):
#     Clothing.stock['name'].append(self.name)
#     Clothing.stock['material'].append(self.material)
#     Clothing.stock['amount'].append(amount)
#   def Stock_by_Material(self, material):
#     count=0
#     n=0
#     for item in Clothing.stock['material']:
#       if item == material:
#         count += Clothing.stock['amount'][n]
#         n+=1
#     return count

# class shirt(Clothing):
#   material="Cotton"
# class pants(Clothing):
#   material="Cotton"
  
# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)

# --------------------------------------------- CODE REUSE ------------------------------------------------------------------

# class Animal:
#     name = ""
#     category = ""
    
#     def __init__(self, name):
#         self.name = name
    
#     def set_category(self, category):
#         self.category = category

# """
# What we have is not enough to do much -- yet. That’s where you come in.

# In the next cell, define a Turtle class that inherits from the Animal class. Then go ahead and set its category. For instance, a turtle is generally considered a reptile. Although modern cladistics call this categorization into question, for purposes of this exercise we will say turtles are reptiles!
# """

# class Turtle(Animal):
#     category = "reptile"

# print(Turtle.category)

# class Snake(Animal):
#     category = 'reptile'

# """
# Now, let’s say we have a large variety of Animals (such as turtles and snakes) in a Zoo. Below we have the Zoo class. We’re going to use it to organize our various Animals. Remember, inheritance says a Turtle is an Animal, but a Zoo is not an Animal and an Animal is not a Zoo -- though they are related to one another.

# Fill in the blanks of the Zoo class below so that you can use zoo.add_animal( ) to add instances of the Animal subclasses you created above. Once you’ve added them all, you should be able to use zoo.total_of_category( ) to tell you exactly how many individual Animal types the Zoo has for each category! Be sure to run the cell once you've finished your edits.
# """

# class Zoo:
#     def __init__(self):
#         self.current_animals = {}
    
#     def add_animal(self, animal):
#         self.current_animals[animal.name] = animal.category
    
#     def total_of_category(self, category):
#         result = 0
#         for animal in self.current_animals.values():
#             if animal == category:
#                 result += 1
#         return result

# zoo = Zoo()

# turtle = Turtle("Turtle") #create an instance of the Turtle class
# snake = Snake("Snake") #create an instance of the Snake class

# zoo.add_animal(turtle)
# zoo.add_animal(snake)

# print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

# """
# Was the output of the above cell 2? If not, go back and edit the Zoo class making sure to fill in the blanks with the appropriate attributes. Be sure to re-run that cell once you've finished your edits.

# Did you get it? If so, perfect! You have successfully defined your Turtle and Snake subclasses as well as your Zoo class. You are all done with this notebook. Great work!
# """

# -----------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------- Assessment - Object-oriented programming ----------------------------------------------

"""
In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

Run the following code that defines this Server class.
"""

# #Begin Portion 1#
# import random

# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}

#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random()*10+1
#         # Add the connection to the dictionary with the calculated load
#         self.connections[connection_id] = connection_load

#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary
#         if connection_id in self.connections:
#             del self.connections[connection_id]
    
#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         # Add up the load for each of the connections
#         for load in self.connections.values():
#             total += load
#         return total

#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())
    
# #End Portion 1#

# """
# Now run the following cell to create a Server instance and add a connection to it, then check the load:
# """
# server = Server()
# server.add_connection("192.168.1.1")

# print(server.load())

# """
# After running the above code cell, if you get a NameError message, be sure to run the Server class definition code block first.

# The output should be 0. This is because some things are missing from the Server class. So, you'll need to go back and fill in the blanks to make it behave properly.

# Go back to the Server class definition and fill in the missing parts for the add_connection and load methods to make the cell above print a number different than zero. As the load is calculated randomly, this number should be different each time the code is executed.

# Hint: Recall that you can iterate through the values of your connections dictionary just as you would any sequence.

# Great! If your output is a random number between 1 and 10, you have successfully coded the add_connection and load methods of the Server class. Well done!

# What about closing a connection? Right now the close_connection method doesn't do anything. Go back to the Server class definition and fill in the missing code for the close_connection method to make the following code work correctly:
# """

# server.close_connection("192.168.1.1")
# print(server.load())

# """
# You have successfully coded the close_connection method if the cell above prints 0.

# Hint: Remember that del dictionary[key] removes the item with key key from the dictionary.

# Alright, we now have a basic implementation of the server class. Let's look at the basic LoadBalancing class. This class will start with only one server available. When a connection gets added, it will randomly select a server to serve that connection, and then pass on the connection to the server. The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them. This is the basic structure:
# """

# #Begin Portion 2#
# class LoadBalancing:
#     def __init__(self):
#         """Initialize the load balancing system with one server"""
#         self.connections = {}
#         self.servers = [Server()]

#     def add_connection(self, connection_id):
#         """Randomly selects a server and adds a connection to it."""
#         server = random.choice(self.servers)
#         # Add the connection to the dictionary with the selected server
#         self.connections[connection_id] = server
#         # Add the connection to the server
#         server.add_connection(connection_id)
        
#     def close_connection(self, connection_id):
#         """Closes the connection on the the server corresponding to connection_id."""
#         # Find out the right server
#         server = self.connections[connection_id]
#         # Close the connection on the server
#         server.close_connection(connection_id)
#         # Remove the connection from the load balancer
#         del self.connections[connection_id]

#     def avg_load(self):
#         """Calculates the average load of all servers"""
#         # Sum the load of each server and divide by the amount of servers
#         total_load = 0
#         for server in self.servers:
#             total_load += server.load()
#         avg_load = total_load/len(self.servers)
#         return avg_load

#     def ensure_availability(self):
#         """If the average load is higher than 50, spin up a new server"""
#         if self.avg_load() > 50:
#             self.servers.append(Server())

#     def __str__(self):
#         """Returns a string with the load for each server."""
#         loads = [str(server) for server in self.servers]
#         return "[{}]".format(",".join(loads))
# #End Portion 2#

# """
# As with the Server class, this class is currently incomplete. You need to fill in the gaps to make it work correctly. For example, this snippet should create a connection in the load balancer, assign it to a running server and then the load should be more than zero:
# """
# l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# print(l.avg_load())

# """
# After running the above code, the output is 0. Fill in the missing parts for the add_connection and avg_load methods of the LoadBalancing class to make this print the right load. Be sure that the load balancer now has an average load more than 0 before proceeding.

# What if we add a new server?
# """
# l.servers.append(Server())
# print(l.avg_load())

# """
# The average load should now be half of what it was before. If it's not, make sure you correctly fill in the missing gaps for the add_connection and avg_load methods so that this code works correctly.

# Hint: You can iterate through the all servers in the self.servers list to get the total server load amount and then divide by the length of the self.servers list to compute the average load amount.

# Fantastic! Now what about closing the connection?
# """

# l.close_connection("fdca:83d2::f20d")
# print(l.avg_load())

# """
# Fill in the code of the LoadBalancing class to make the load go back to zero once the connection is closed.

# Great job! Before, we added a server manually. But we want this to happen automatically when the average load is more than 50%. To make this possible, fill in the missing code for the ensure_availability method and call it from the add_connection method after a connection has been added. You can test it with the following code:
# """

# for connection in range(20):
#     l.add_connection(connection)
# print(l)

# """
# The code above adds 20 new connections and then prints the loads for each server in the load balancer. If you coded correctly, new servers should have been added automatically to ensure that the average load of all servers is not more than 50%.

# Run the following code to verify that the average load of the load balancer is not more than 50%.
# """
# print(l.avg_load())

# """
# Awesome! If the average load is indeed less than 50%, you are all done with this assessment.
# """

# -------------------------------------------------------------------------------------------------------------------------------------------------

# def get_event_date(event):
# 	return event.date

# def currnet_users(events):
# 	events.sort(key = get_event_date)
# 	machines = {}
# 	for event in events:
# 		if event.machine not in machines:
# 			machines[event.machine] = set()
# 		if event.type == "login":
# 			machines[event.machine].add(event.user)
# 		elif event.type == "logout":
# 			if event.user in machines[event.machine]:
# 				machines[event.machine].remove(event.user)
# 	return machines

# def generate_report(machines):
# 	for machine, user in machines.items():
# 		if len(user) > 0:
# 			user_list = ", ".join(user)
# 			print(f"{machine}: {user}")

# class Event:
# 	def __init__(self, event_date, event_type, machine_name, user):
# 		self.date = event_date
# 		self.type = event_type
# 		self.machine = machine_name
# 		self.user = user

# events = [
#     Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
#     Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
#     Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
#     Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
#     Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
#     Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
# ]

# users = currnet_users(events)
# print(users)

# generate_report(users)


# ----------------------------------------------------------------------------------------------------------------

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    file_contents = file_contents.lower()
    for char in punctuations:
        file_contents.replace(char,"")
    
    words = file_contents.split()
    
    word_count = {}
    for word in words:
        if word not in uninteresting words: #yha humne uninteresting words ko filter bhi kr lia
            if word.isalpha(): #yha humne check kia ki vo words alphabetic hi h na
                if word in word_count:
                    word_count[word] += 1 #agar duara aa rha h to 1 se increase krdo 
                else:
                    word_count[word] = 1 #else 1 hi rehene do

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()