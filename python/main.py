# 6
# print("hellow world", end=" whatever you want to print ")
# print("i am a good")
#print("hellow world","i am a good boy",)
#print("next line")
"""ESCAPE SEQUENCE CHARACTERS- 
\n(for new line)
\t(leave a tan)
etc...
"""
#print("yash is a\ngood boy\thelp")

#8-- variables, datatypes, typecasting
"""a = "hellow "
a1 = "yash"
b=25
c=5.5
print(a)                                                   #str
print(b)                                                   #int
print(c)                                                   #float
print(a+a1)                                                #str + str
print(b+c)                                                 #int + float
print(a+b)                                                 #error 
print(type(a1))                                            #datatype

var1="40"  
var2="50"
print(var1+var2)                                           #because these atr string
print(int(var1)+int(var2))                                 #converting strins into integer by using int() , more function are str(), float
print(10 * "hellow yash \n")                               #print anything a number of times
print("enter your number")
a = input()
print("you entered", int(a)+10)"""


"""                                     CALCULATER
print("enter first number")
a = input()
print("enter second number")
b = input()
print("sum of these numbers is :", int(a)+int(b))o
"""

                                                        # 9-- string slicing
"""
mystr = "harry is a good boy"
print(mystr[0])                     #strings starts with 0 & includes blank spaces also.
print(mystr[0:4])                   #[0 is included but 4 is not] so, y of harry is ignored                      
print(mystr[0:5])                   #this is claaed string slicing
print(len(mystr))                    #total words are 19 [length function]
print(mystr[0:19]) 
# print(mystr[0:len(mystr)])
print(mystr[20])                     #error
print(mystr[0:20])                    #no error
                                           #(((extended slicing)))

print(mystr[::])                     # defaylt -- 0:19:1 (19 is the total length)
print(mystr[0:19:2])                 # 0-2-4-6.....
print(mystr[::3])                    # 0-3-6......
print(mystr[::10000])                # leave 10000 spaces
                                           
                                           #(((negative indices)))

print(mystr[-4:0])                    # no output
print(mystr[-4:-2])                    #-4 or 15 and-2 or 17 means 15:17
print(mystr[15:17])                    # same result

                    note: in negative indices last word starts with 1
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            | 0    1    2    3    4       5       6    7    8    9   10    11 |
            | M    O    N    T    Y               P    Y    T    H    O     N |
            |-12  -11  -10  -9   -8      -7      -6   -5   -4   -3   -2    -1 |
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          
print(mystr[::-1])                     # REVERSE THE STRING
print(mystr[::-2])                      # REVERSE THE STRING AND CHOOSE 2nd WORD

print(mystr.isalnum())                  #boolen function this is false because it is not alphanumeric
print(mystr.isalpha())                  # because it is neither alpha. nor numeric
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())               #capitalize takes no argument (firsr letter) 
print(mystr.find("is"))                 #is starts with 6th index
print(mystr.lower())                    # (all letters)
print(mystr.upper())                    # (all letters)
print(mystr.replace("is", "was"))
"""

                                                               # 10--LISTS []
"""
grocery = ["harpic", "vim", "deo", "bhindi", "lollypop", 56]                                              
print(grocery)
print(grocery[2])
print(grocery[6])                                    #error

numbers = [2, 7, 9, 11, 3]
print(numbers[2])
numbers.sort()
numbers.reverse()
print(numbers[1:4])
print(numbers[1:5:2])
print(numbers[::-2])
print(numbers[::-3])
print(numbers[1:5:-3])                          # empty list
print(max(numbers))                              # len(), min(), max(), count(), append() etc.
numbers.append(100)                               # append means adding a number in the end
numbers.append(100)
numbers.append(100)
numbers.insert(1,67)                             #adding 67 at 1 index 
numbers.remove(9)
numbers.pop()
print(numbers)                                     #removing the last index
        # mutable = can change
        # immutable = cannot change 

numbers[1] = 98                                    #chanhing i index beacuse list is mutable
print(numbers)
                                   # TUPLES ()
tp = (1, 2, 3)                         
tp[1] = 65                                          # eror because tuple is immutable
tp = (1,)                                            # for one element , is necessary
print(tp)

a = 1
b = 2
a,b = b,a
print(a,b)
"""

                                                       # 11-- DICTONARY {}
# DICTONARY IS ALSO KNOWN AS KEY VALUE PAIRS
"""
d1 = {}
print(type(d1))                                           
d2 = {"harry":"burger", "rohan":"fish", 
      "ram":"roti", "shubham":{"B":"maggie", 
                                "L":"Roti", "D":"chicken"}}
print(d2["shubham"])
print(d2["shubham"]["B"])
d2["ankit"] = "junk food"                            # adding a key in dict.
d2[200] = "kabab"
del d2[200]                                          # removing a key from dict.

d3=d2
d3["yash"] = "parwal"
del d3["harry"]
print(d2)

d3=d2.copy()
d3["yash"] = "parwal"
del d3["harry"]
print(d2)

print(d2.get("harry"))
d2.update({"yash":"parwal"})                          # adding a key in dict.
print(d2.keys())                                      
print(d2.items()) 
"""

                                                   # 12-- exercise1-- making dictionary
"""
d = {"ram":"it is a name", "jaipur":"it is a place", "dog":"it is an animal", "cup":"it is a thing" }
print("enter you word")
print("meaning is :- ", d.get(input()))       #result                                         
print("enter your word")
d1 = input()                                    
print("meaning is :-", d.get(d1))               #result
"""

#13 -- SETS ()
"""
s = set()
print(type(s))
s_from_list = set([1,2,3,4])
print(s_from_list)
s.add(1)
s.add(2)
s.remove(2)
s.union()
s1 = s.union({1,2,3})
s2 = s.intersection({1,2,3})
s3 = {1,2,3,4,5}
s4 = {5,6}
print(s.isdisjoint(s3))
print(s.isdisjoint(s4))
print(s.issubset(s4))
"""
                                                # 14-- if else , elif

#var1 = 6
#var2 = 56
#var3 = int(input())

"""if var3>var2:                                 # here colon means that i want to go inside if-else function
        print("yes it is greater")
if var3==var2:                                # single = sigh is an assignment operator so, use double == sign
        print("it is equal")
else:
        print("no it is lesser")
"""
"""        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     note: |if var3 is greater than var2 then it should stop at 'if:' which satisfies the condition but it goes on and check all 'if:'|
           |Therefore, to save time when we have so much 'if:' conditions, we use "elif:" mean- elseif......                          |
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# if var3>var2:                                  # here colon means that i want to go inside if-else function
#        print("yes it is greater")
# elif var3==var2:                                # single = sigh is an assignment operator so, use double == sign
#        print("it is equal")
# else:
#        print("no it is lesser")


#list1 = [1,2,3]
#l1 = int(input())
# if l1 in list1:
#        print("yes it's in the list")                  # 'in' keyword is used here.
# else:
#        print("no it's not in the list")

#list1 = [1,2,3]
# print(5 in list1)                                       # boolen function(true or false) , 'in' keyword is used here.
# if 5 in list1:
#        print("yes it's in the list")                   # 'in' keyword is used here.
# else:
#        print("no it's not in the list")
#
#list1 = [1,2,3]
# print(5 not in list1)                                   #boolen function(true or false) , 'not in' keyword is used here.
# if 5 not in list1:
#        print("yes it's not in the list")               # 'not in' keyword is used here.
# else:
#        print("no it's in the list")

                                                # 15-- solution of ex.1
"""print("what is your age?")
age = int(input())
if 18>age>7:
        print("you cannot drive")
elif age == 18:
        print("come for test drive")
elif 100>age>18:
        print("you can drive")
elif age>100:
        print("you are dead and you cannot drive")
elif age<7:
        print("you are too small to drive so come after 18")
else:
        print("bye")"""

"""                                               #16 -- exercise-2 ...faulty calculater  
# 56 + 9 = 77 , 100 - 50 = 10 , 45 * 3 = 555 , 56/6 = 4. 
print("choose your operator")
op = input()
print("enter greater number : ")
num1 = int(input())
print("enter smaller number : ")
num2 = int(input())

if op=='+' and num1==56 and num2==9:
        print(num1, '+', num2, '=', 77)
elif op=='-' and num1==100 and num2 == 50:
        print(num1, '-', num2, '=', 10 ) 
elif op=='*' and num1==45 and num2==3:
        print(num1, '*', num2, '=', 555)
elif op=='/' and num1==56 and num2==6:
        print(num1, '/', num2, '=', 4)
elif op=='+':
        print(num1 + num2)
elif op=='-':
        print(num1 - num2)
elif op=='*':
        print(num1 * num2)
elif op=='/':
        print(num1 / num2)


else:
        print("invalid entry")"""

                                             # 17-- for loops in python

#list1 = ["harry", "carry", "larry", "marry"]
# print(list1[0], list1[1])  this is very lengthy method if there are many values in list, so.........

# for items in list1:                                # means we entered in for-loop
#        print(items)

# list1 = [["harry is",1], ["carry was",5], ["larry are",3], ["merie is",10],]  #list of list

# for items in list1:
#        print(items)                                            # this prints list as it is but......

# for x,y in list1:
#        print(x,y)                                       # this gives result in prper way i.e. by unpacking list of list   (OR)
#        print(x, "and the value is", y)                  # this gives result in prper way i.e. by unpacking list of list

# dict1 = dict(list1)                                              #for printing list as dict.
# print(dict1)
# for x,y in dict1:                                        # error
# for x,y in dict1.items():                                 # no error, .items() function is used in case of dict
#        print(x, "and the value is", y)


# test = ["yash", 3, 4 ,72, 78, 100, -5, "dinesh", "any", "thing"]
# for items in test:
#         if str(items).isnumeric() and items>7:
#                 print(items)
#         else:
#                 print("no")

                                # 18 and 19-- while loops in python, break and continue statement

"""
i = 0
while (i<45):
        print(i)              0 to 44
        print(i +1)           1 to 44                                  # while(1) and while(True) are the statements
        print(i end = " ")    in only one line                            which always goes on and never stops.
        i = i + 1             

 i = 0
 while (True):
         print(i)
         if i >= 50:
                 break                            # stop the loop 
         i = i + 1

 i = 0
 while (1):
         if i < 5:
                # i = i+1
                # print("yes")
                # continue                        # continue means forget the program written after this and return to while loop 
         print(i)
         if (i==50):
                # break                           # break means stoop the loop and come out the while loop
         i=i+1

"""


"""
print("enter the special code")
code = int(input())
if code<100:
        print("soory, try again")
while code<100:
        code = int(input())
        print("soory, try again")
        continue
if code > 100:
        print("congratulations, you are passed")
"""

# or

"""
print("now you have to enter the code")
while (1):
        print("enter your code")
        code = int(input())
        print("sorry, try again")
        if code>100:
                print("congratulations, you are pased")
                break
"""
# or
"""
while(1):
        code = int(input("enter your code \n"))
        if code > 100:
                print("congrets, you are a VIP member")
                break
        else:
                print("soory, you are not a VIP member\n")
                continue
"""
                                                   # 20 solution of faulty calculator
                                                   # 21 exercise 3
"""
print("So lets start the game \n you have to find the right code which is hidden between the numbers 0 and 50 ")
print("note that you have only 10 lives")
print("no. of lives remaining = 10")
i = 0

while(1):
        if i < 10:
                i = i+1
                
                print("enter the code to proceed")
                code = int(input())
                print("no. of lives remaining =", 10-i)
                if code>=0 and code<=17:
                        print("try again with bigger number")
                        continue
                elif code>=19 and code<=50:
                        print("try again with smaller number")
                        continue
                elif code>50:
                        print("invalid entry! plzz choose btw. 0 and 50")
                        continue
                elif code == 18:
                        print("lives spent = ",i+1)
                        print("hurrey! you WON!")
                        break
        else:
                print("GAME OVER")
                print(".....")
                print("....")
                print("...")
                print("..")
                print(".")
                break
                
"""
                                            #22 -- operators in python

"""
1 - Airthmetic operators
2 - Assignment operators
3 - Comparision operators
4 - Logical operators
5 - Identity operators
6 - Membership operators
7 - Bitwise operators

"""
# 1
"""
print("5 - 6 is", 5-6)
print("5 * 6 is", 5*6)
print("5 ** 6 is", 5**6)    # ** is called exponential operator ( 5 to the power 6)
print("5 / 6 is", 5/6)
print("5 + 6 is", 5+6)        
print("15 // 6 is", 15//6)  # // is called floor division operator which gives only intiger value and ignores the decimal values
print("5 % 10 is", 15%3)    # modulus operator which gives the remainder
"""

"""
#2 -- assignment operators
x = 5
print(x)
x += 10              # -=, /=, %= are assignment operators 
print(x)
"""
# 3 comparision operators
#i = 8
# print(i == 5)    # >, <, >=, <= are comparision operators

# 4 logival operators (and , or)
#a = True
#b = False

# print(a and a)               # true and true = true
# print(a and b)               # true and false = false

#print(a or b)

# 5 identity operator (is , is not)
"""
a = True
c = False

print(a is a)
print(a is not c)
print(5 is 6)
"""
# 6 mrmbership operator (in , not in)

# mylist = [21, 31, 41, 51, 61]
# print(61 in mylist )

# 7 bitwise operator
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

#print(0 & 1)
#print(0 | 1)

                                            # 23 -- short hand if else notation

"""
a = int(input("enter a\n"))
b = int(input("enter b\n"))

#if a>b: print("A is bigger than B ")

print("A is bigger than B") if a>b else print("A is smaller than B")
"""

                                              # 24 -- Functions and docstring

#
#a = 10
#c = 20
#b = sum((a, c))       # built-in function
#print(b)


#def function1():       # user dedined function
#    print("welcome now you are in function1")
#
#
#function1()   # for writing a line som many times
#function1()
#function1()
#function1()
#function1()
#function1()
#
#
#def function2(a, b):
#    print("welcome now you are in function1", a+b)
#
#
#function2(10, 20)
#
#
#def function3(a, b):
#    """this is a function which calculate average"""          # this is docstring
#    average = (a+b)/2
#    # print(average)
#    return average             # to store the average value in a variable
#
#
#v = function3(10, 20)
## this will return the doc string written as in form of comment
#print(function3.__doc__)


                                     # 25 -- Try Except Exception Handling in Python



"""num1 = (input("num1 =" ))
num2 = (input("num2 =" ))
try:                                                                  # it will try the function and if error occurs, it wll store it in assigned variable
        print("sum of num1 and num2 is =", int(num1)+int(num2))   
except Exception as e:                                                # e is the variable assigned to store the eror (if occurs)
        print(e)
        print("this line is very important")

"""

                                                    # 26 Python file IO basics

"""
"r" - Open file for Reading            # it is default mode
"w" - Open file for Writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - Text mode                        # it is default mode
"b" - Binary mode
"+" - Read & Write
"""

                                    # 27 - Open(), Read(), & Readline() for reading a file
                                    # 28 - exercise 3 solution

"""
f = open("keton.txt", "ab")     # r and t are default so the result will be the same
content = f.read()
print(content)
"""
# content = f.read(3)            # here it will read only first 3 characters of the file
# print(content)

# content = f.read(3)            # here it will read  next 3 characters of the file
# print(content)

# f.close()

"""
f = open("keton.txt")     
content = f.read()
for line in content:            # it will print all the characters line by line i.e. one char. in one line        
        print(line)
"""

"""
f = open("keton.txt")     
for line in f:                   # it will print all the content line by line        
        print(line, end="")      # end="" -- it will ignore spaces betw. tow lines
"""
# f = open("keton.txt")
# print(f.readline())
# print(f.readline())

#f = open("keton.txt")
#print(f.readlines())             # it will store all the lines in dict


                                       #29 -- Writing and apending to a file in python

"""
#f = open("keton2.txt", "w")            # open file in writing mode
f = open("keton2.txt", "a")             # open file appand mode 
#f.write("keton is very good machine\n")  
a = f.write("keton is very good machine\n") # it will print the no. of characters in the file  
print(a)
f.close

"""

        # handle red and write both at one time    

"""
f = open("keton3.txt", "r+")
print(f.read())
f.write("how are you")
"""

                                                        # 30-- exercise 4
"""
print("pattern printing game")
rows = int(input("enter the number of rows you want to print"))
boolean = bool(int(input("enter 1 for assending order\n enter 0 for decending order")))

if boolean == True:
        for x in range(1, rows + 1):
                print("*" * x, end="\n")
                x = 1

elif boolean == False:
        for x in range(1, rows + 1):
                print("*" * rows, end="\n")
                rows -= 1
"""

                                                        
                                                # 31-- Seek(), tell() & More On Python Files

"""
f = open("yash.txt")
#print(f.tell())                     # it shows the pointer location
print(f.readline())
#print(f.tell())
f.seek(10)                      # it place the pointer at the 10th character location
print(f.readline())
f.close()
"""

                                                # 32 -- Using With Block To Open Python Files

"""with open("yash.txt") as f:              # we do not need to cloas the file in this case.... with-as handles it on its on 
        file = f.read(3)                   
        print(file)"""

                                                # 33-- Exercise 5
"""
# HEALTH MAMANGEMENT SYSTEM
def getdate():
        import datetime
        return datetime.datetime.now()

print("[1]- log the value\n[2]- retrieve\nchoose an option : ")
a = int(input())
if a == 1:
        clients = int(input("your clients are :\n[1]. Harry\n[2]. Rohan\n[3]. Hammad\n choose your option:"))
        #c = Categoury = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
        if clients == 1:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))

                if c == 1:
                        f = open("harry-ex.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                elif c == 2:
                        f = open("harry-food.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Food name : ")
                                foodname = input()
                                f.write(str([str(getdate())]) + ": " + foodname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                else:
                        print("please choose correct option")

        elif clients == 2:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        f = open("rohan-ex.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                elif c == 2:
                        f = open("rohan-food.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Food name : ")
                                foodname = input()
                                f.write(str([str(getdate())]) + ": " + foodname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                else:
                        print("please choose correct option")
        elif clients == 3:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        f = open("hammad-ex.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                               
                                continue
                elif c == 2:
                        f = open("hammad-food.txt", "w")
                        k = 'y'
                        while (k != "n"):
                                print("Food name : ")
                                foodname = input()
                                f.write(str([str(getdate())]) + ": " + foodname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                else:
                        print("please choose correct option")               
        else:
                print("please choose correct option [1], [2], [3]")

elif a == 2:
        clients = int(input("your clients are :\n[1]. Harry\n[2]. Rohan\n[3]. Hammad\n choose your option:"))
        if clients == 1:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        with open("harry-ex.txt") as he:
                                file = he.read()
                                print(file)
                elif c == 2:
                        with open("harry-food.txt") as hf:
                                file = hf.read()
                                print(file)
                else:
                        print("choose correct option")
        if clients == 2:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        with open("rohan-ex.txt") as re:
                                file = re.read()
                                print(file)
                elif c == 2:
                        with open("rohan-food.txt") as rf:
                                file = rf.read()
                                print(file)
                else:
                        print("choose correct option")
        if clients == 3:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        with open("hammad-ex.txt") as hde:
                                file = hde.read()
                                print(file)
                elif c == 2:
                        with open("rohan-food.txt") as hdf:
                                file = hdf.read()
                                print(file)
                else:
                        print("choose correct option")
else:
        print("choose correct option")

"""

                                              #34 - Scope, Global Variables and Global Keyword

"""
l = 10                                 # this is global variable
def function1(n):
        #l = 5                          # this is local variable
        m = 7                          # this is local variable             
        
        global l                       # this allows to change the value of global variable inside a function
        l = l + 50
        print(l,m)
        print(n, "i have printed")
function1("this is me")
print(l)
"""
                                 
"""
def yash():
        x = 50
        def parwal():
                global x               # there is no global variable so it will print 50 only, not 100
                x = 100
        print(x)     
        parwal()
        print(x)
#print(x)                  # x is not defined because there is no global variable
yash()
print(x)                   # now it will create a global variable thai is x=100 and dut to globla x it will print 100
"""

                                                # 35 - Recursions: Recursive Vs Iterative Approach
"""
def funk1(str1):
        funk1(str1)                # RecursionError: maximum recursion depth exceeded
        print("this is " + str1)

funk1("yash")
"""
"""
def factorial_iterative(n):            # this is iterative approach to find factorial of any number
        fac = 1
        for i in range(n):
                fac = fac * (i+1)
        return fac

num = int(input("Enter your number"))
print("factorial using iterative method", factorial_iterative(num))

def factorial_recursive(n):            # this is recursive approach to find factorial of any number
        if n == 1 or n == 0:
                return 1
        else:
                return n * factorial_recursive(n - 1)
# the above if else function will work as:
#5 * factorial_recursive(4)
#5 * 4 * factorial_recursive(3)
#5 * 4 * 3 * factorial_recursive(4)
#5 * 4 * 3 * 2 * factorial_recursive(1)
#5 * 4 * 3 * 2 * 1 = 120                    


print("factorial using recursive method", factorial_recursive(num))
"""

                                        # 37 -- Anonymous/Lambda Functions In Python
"""
def add(a, b):
        return a + b

minus = lambda x, y: x - y    # a lamda function 
                                       
def minus(x, y):                                            #these boths will return same result 
        return x - y          # simple def function

print(minus(10,5))
"""

"""
def a_first(a):
        return a[1]

a = [[1,14], [5,6], [8,23]]
# a.sort(key = a_first)
a.sort(key = lambda x:x[1] )
print(a)
"""

                                          # 38 -- exercise 5 solution
                                          
                                          # 39 -- Using Python External & Built In Modules

"""
import random

randomnumber = random.randint(0,10)
# print(randomnumber)

randnum = random.random() * 100            # randum() takes no argument 😎
# print(randnum)

tvlst = ["Star Plus", "DD1", "Star Gold"]
randchoice = random.choice(tvlst)                
# randchoice = random.choices(tvlst)            # .choices gives output in list format              
print(randchoice)
"""

                                         # 40 -- Fstring & String formatting in Python

"""
me = "yash"
a1 = 5
# a = "this is %s %s"% (me, a1)
a = "this is my name thst is {} {}"
b = a.format(me,a1)
print(b)
"""

"""
import math

me = "yash"
a1 = 5
a = f"this is {me} {a1} {5 * 10} {math.sin(30)}"
print(a)
"""

                                        # 41 -- Exercise 6 - Game Development: Snake Water Gun

"""
import random

print("GAME NAME - Snake, Water and Gun")
print("GAME RULES :\n1. Choose s for Snake, w for Water and g for Gun\n2.If any game draws, it'll be counted")
ready = input("So, Be ready the game is starting\nPress Enter to start ")


totalchances = 10
user_score = 0
computer_score = 0
gameno = 0



lst = ['s', 'w', 'g']
print("[s] - Snake\n[w] - Water\n[g] - Gun\n")

while gameno < totalchances:
        
        gameno = gameno + 1
        print(f"Game {gameno} is starting...")
        
        user = input("Choose wisily:= ")
        computer = random.choice(lst)
        
        if user == "s" and computer == "s":
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("Match Draw" )
                print("Youe Score = ", user_score)
                print("Computer Score = ", computer_score )
        
        elif user == "s" and computer == "w":
                user_score = user_score + 1
                print(f"Your Choice = {user} and Computer choice = {computer}")
                print("You WON")
                print("Your Score = ", user_score)
                print("Computer Score = ", computer_score)
        
        elif user == "s" and computer == "g":
                computer_score = computer_score + 1
                print(f"Your Choice = {user} and Computer choice = {computer}")
                print("Computer WON")
                print("Your Score = ", user_score)
                print("COmputer Score = ", computer_score)

        elif user == "w" and computer == "w":
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("Match Draw" )
                print("Youe Score = ", user_score)
                print("Computer Score = ", computer_score )

        elif user == "w" and computer == "s":
                computer_score = computer_score + 1
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("Computer WON")
                print("Your Score = ", user_score)
                print("Computer Score = ", computer_score)
                
        elif user == "w" and computer == "g":
                user_score = user_score + 1
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("You WON")
                print("Your Score = ", user_score)
                print("Computer Score = ", computer_score)

        elif user == "g" and computer == "g":
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("Match Draw")
                print("Your Score = ", user_score)
                print("Computer Score ", computer_score)

        elif user == "g" and computer == "s":
                user_score = user_score + 1
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("You WON")
                print("Your Score = ", user_score)
                print("Computer Score = ", computer_score)

        elif user == "g" and computer == "w":
                computer_score = computer_score + 1
                print(f"Your Choice = {user} and Computer Choice = {computer}")
                print("Computer WON")
                print("Your Score = ", user_score)
                print("Computer Score = ", computer_score)

        else:
                print("Please choose correct option")

print("!!! GAME OVER !!!")

print(f"Your Total Score is : {user_score} and Computer's Total Score is : {computer_score}")
if user_score > computer_score:
        print("Hurrey!!! You Won the Series\nHere is a gift for you.... ❤❤❤🎂🎂🎂\nSee you next time.Bye......")
else:
        print("Sorry!!! You lose the series\nDon't worry you'll still get a gift.... 😝LOL😝 Come next time ")
"""

                                 # 42 == *args and **kwargs In Python 

#def function_name_print(a, b, c, d):
#        print(a, b, c,d)

#function_name_print["Yash", "Parwal", "cyber", "keton"]

""" if we want we add any other user in the list we have to add variable also.... to overcome this problem we use arguments....  """
"""
def funargs(*args):
        # print(type(args))
        # print(args[0]) # it will print Yash (although we have list but its class is always 'tuple')
        
        for items in args:
                print(items)
har = ["Yash", "Parwal", "cyber", "keton", "Harry"]
funargs(*har)

"" Now we can add more names in list and we dont need to add variables for new names like in privious method. Moreover
 we dont need to specify any vriables, only just a function ""
 """
"""
def funargs(normal, *args, **kwargs):
        print(normal)
        
        for item in args:
                print(item)
        print("\nNow i would like to introduce some more students : ")
        for key, value in kwargs.items():
                print(f"{key} is {value}")

ar = ["Yash", "Parwal", "cyber", "keton", "Harry"]
normal = "I am a normal argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Trainr", "Yash":"Hacker", "Shivam":"cook"}
funargs(normal, *ar, **kw)

"""

                                        #43 -- time moule in python

"""
import time
initial = time.time()

k = 0
while (k<45):
        print("This is yash parwal")
        time.sleep(2)              # it will stop the program foe 2 seconds and while printing This is yash parwal every time
        k += 1
print("while loop ran in :", time.time() - initial, "seconds")

initial2 = time.time()
for i in range(45):
        print("This is yash parwal")
print("for loop ran in :", time.time() - initial2, "seconds")


# time.localtimeasctime(time.localtime(time.time()))
# print(localtime)
"""

                                                #44 -- Virtual Environment and requirements.txt
                                                #45 -- Enumerate Function in Python
"""
list1 = ['Bhindi', 'Aaloo', 'Chopsticks', 'Chowmeine']

#i = 1
#for item in list1:
#        if i%2 != 0:
#                print(f" Please buy {item} ")
#
#        i += 1


for i, item in enumerate(list1):      #it gives both index(starting from 0) and name of the item)  
        if i%2==0:
                print(f"Please buy {item} ")
                
"""

                                                 #46 -- How imports works in Python