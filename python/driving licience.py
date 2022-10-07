print("what is your age?")
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
        print("bye")
k = (input("press enter key to quit"))