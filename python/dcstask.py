
""" sName = input("Enter the Name: ")
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

""" 
CLOCK IN PYTHON
"""

