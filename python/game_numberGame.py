print("So lets start the game \n you have to find the right code which is hidden between the numbers 0 and 50 ")
print("note that you have only 10 lives")
print("no. of lives remaining = 10")
i = 0

while(1):
        if i < 10:
                i = i+1
                
                print("enter the code to proceed: ")
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


import tkinter as tk
from tkinter import messagebox

def check_code():
    global i
    code = int(entry.get())
    
    if 0 <= code <= 17:
        messagebox.showinfo("Try Again", "Try again with a bigger number")
    elif 19 <= code <= 50:
        messagebox.showinfo("Try Again", "Try again with a smaller number")
    elif code > 50:
        messagebox.showinfo("Invalid Entry", "Invalid entry! Please choose between 0 and 50")
    elif code == 18:
        messagebox.showinfo("Congratulations!", f"You WON!\nLives spent: {i + 1}")
        root.destroy()
    else:
        messagebox.showinfo("Invalid Entry", "Invalid entry! Please choose between 0 and 50")
    
    i += 1
    lives_label.config(text=f"No. of lives remaining: {10 - i}")

    if i == 10:
        messagebox.showinfo("Game Over", "GAME OVER")
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Initialize variables
i = 0

# Create and place widgets
label1 = tk.Label(root, text="So let's start the game\nYou have to find the right code which is hidden between the numbers 0 and 50")
label1.pack()

label2 = tk.Label(root, text="Note that you have only 10 lives")
label2.pack()

lives_label = tk.Label(root, text="No. of lives remaining: 10")
lives_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=check_code)
button.pack()

# Start the GUI event loop
root.mainloop()
