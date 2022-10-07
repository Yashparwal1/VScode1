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