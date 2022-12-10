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
The interpreter of python was officially written in C lang known as CPython. But there are several more implementation of python like Jpython which was written in Java, IronPython which was written in C# and PyPy which was written in Python itself.

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

#==================================TYPECASTING=============================================

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

#================================Conditional Statements=====================================

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

#-----------------------------------THRUTHNESS----------------------------------------------

    # in binary: 1 -> True and 0 -> False
    ### False items are: 0, Empty Objects, Empty String, None 

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

#---------------------------------------is keyword--------------------------------------------- 
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



#====================================LOOPS IN PYTHON===========================================
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

#------------------------------------range()------------------------------------------------
#range(start,stop,step)
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

new = 0
for i in range(1,5):
    print(" "*(5-i) + "*"*new)
    new = new+2


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

#=====================================JUMP STATEMENT========================================== 
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

# ==> 3. index(index_number,object_to_add)
# data.insert(3,"hlo") #hlo will be inserted at 3rd index
# print(data) 

# ------------------------------- PROBLEM WITH NEGATIVE INDEXING ------------------------------
#NOTE: in negative indexing, first it it converted into equivalent positive index and then data is inserted
# temp = [1,2,3]
# temp.insert(-1,4) #4 should be added at last ==> [1,2,3,4] but NO....
# ---------------------------------------------------------------------------------------------
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

'''_____________________________________________________________________________________'''

# ====================================STRING==============================================
# STRING FUNCTIONS (Note: these func do not modify the original string)

'''
# PYTHON STRING METHODS https://www.w3schools.com/python/python_ref_string.asp

name = "yash parwal"

# 1. capitalise -- capital the first letter of string
name.capitalize()

# 2. count -- coubt the no of letters in a string
name.count("a")

# 3. endswith -- S.endswith(suffix[, start[, end]]) -> bool
# Return True if S ends with the specified suffix, False otherwise.
name.endswith("l")

# 4. find -- print the first ouucurance of the provided letter in string 
name.find("h")
# if not there, it will return -1

# 5. index -- 	Searches the string for a specified value and returns the position of where it was found


# if not there, it will give error due to which further program execution will stop

# 6. Replace -- replace all occurance of 1st item with second item
name.replace("a","b")

# 7. upper and lower
name.upper()
name.lower()

# 8. strip -- Return a copy of the string with leading and trailing whitespace removed.
name.strip() 

# 9. exit

# 10. encode & decode -- Encode the string using the codec registered for encoding.
# Convert the string into byte/binary from
name.encode()
name.decode()
'''

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

#DICTIONARY COMPREHENSION

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
#	# some_code

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

#\_____________________________________PYTHON-9 29oct.___________________________________________/ 

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


#\_____________________________________PYTHON-10 30oct.___________________________________________/

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