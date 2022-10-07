# HEALTH MAMANGEMENT SYSTEM
def getdate():
        import datetime
        return datetime.datetime.now()

print("[1]- log the value\n[2]- retrieve\nchoose an option : ")
a = int(input())
if a == 1:
        clients = int(input("your clients are :\n[1]. Harry\n[2]. Rohan\n[3]. Hammad\n choose your option:"))
        #c = Categoury = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
        if clients is 1:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))

                if c == 1:
                        f = open("harry-ex.txt", "w")
                        k = 'y'
                        while (k is not "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                elif c == 2:
                        f = open("harry-food.txt", "w")
                        k = 'y'
                        while (k is not "n"):
                                print("Food name : ")
                                foodname = input()
                                f.write(str([str(getdate())]) + ": " + foodname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                else:
                        print("please choose correct option")

        elif clients is 2:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        f = open("rohan-ex.txt", "w")
                        k = 'y'
                        while (k is not "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                elif c == 2:
                        f = open("rohan-food.txt", "w")
                        k = 'y'
                        while (k is not "n"):
                                print("Food name : ")
                                foodname = input()
                                f.write(str([str(getdate())]) + ": " + foodname + "\n")
                                k = input("Add more : y/n\n")
                                continue
                else:
                        print("please choose correct option")
        elif clients is 3:
                c = int(input("Categouries are :\n[1]- Exercise\n[2]- Food\nchoose your option:"))
                if c == 1:
                        f = open("hammad-ex.txt", "w")
                        k = 'y'
                        while (k is not "n"):
                                print("Exercise name : ")
                                exname = input()
                                f.write(str([str(getdate())]) + ": " + exname + "\n")
                                k = input("Add more : y/n\n")
                               
                                continue
                elif c == 2:
                        f = open("hammad-food.txt", "w")
                        k = 'y'
                        while (k is not "n"):
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
        if clients is 1:
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
        if clients is 2:
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
        if clients is 3:
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