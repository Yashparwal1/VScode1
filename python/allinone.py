# numbers = []

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num

# for num in numbers:
#     if num < smallest:
#         smallest = num
        
# print(f"The largest number is {largest}")
# print(f"The smallest number is {smallest}")


# def numb():
#     for i in range(5):
#         n = int(input("Enter number: "))
#         print(n)

# numb()

# ==================================================================================
'''
# QUESTION: Find the Looser - GfG

# win = []
# lose = []
# n = 5
# k = 2
# steps = k
# i = 1
# for f in range(1,n+1):                   # 1,  2,   3
#     if i >= n:                           #   7>5, 8>5
#         i=(i-n)
#         if i in win:
#             for l in range(1,n+1):
#                 if l not in win:
#                     lose.append(l)
#             break
#     ball = i                             # 1,  3,  2
#     win.append(ball)
#     k = steps*f                          # 2,  4,  6
#     i = i+k                              # 3,  7,  8

# print(win)
# print(lose)

# ball = 1
# ball = ball+k
# ball = ball+(k*2)

# ================================== IN GUI ========================================

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

def play_game(n, k):
    win = []
    lose = []
    steps = k
    i = 1

    for f in range(1, n + 1):
        if i >= n:
            i = i - n
            if i in win:
                for l in range(1, n + 1):
                    if l not in win:
                        lose.append(l)
                break
        ball = i
        win.append(ball)
        k = steps * f
        i = i + k

    return win, lose

def start_game():
    n = int(num_friends_entry.get())
    k = int(num_steps_entry.get())

    if n <= 0 or k <= 0:
        messagebox.showerror("Invalid Input", "Number of friends and steps must be positive integers.")
        return

    win_list, lose_list = play_game(n, k)
    win_str = ", ".join(str(ball) for ball in win_list)
    lose_str = ", ".join(str(ball) for ball in lose_list)

    result_label.config(text=f"Winners: {win_str}\nLosers: {lose_str}")

def show_image():
    image = Image.open("ball.jpg")
    image = image.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

# Create the main window
window = tk.Tk()
window.title("Passing Ball Game")

# Load and display image
image_label = tk.Label(window)
image_label.pack()
show_image()

# Create and place labels and entry fields
num_friends_label = tk.Label(window, text="Number of Friends:")
num_friends_label.pack()

num_friends_entry = tk.Entry(window)
num_friends_entry.pack()

num_steps_label = tk.Label(window, text="Number of Steps:")
num_steps_label.pack()

num_steps_entry = tk.Entry(window)
num_steps_entry.pack()

start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main GUI loop
window.mainloop()

# ======================================================================================
'''

# import tkinter as tk

# # Start the game loop.
# def start_game():
#     while True:
#         # Get the current player.
#         current_player = int(current_player_label.cget("text").replace("Current Player: ", ""))

#         # Move the ball to the next player.
#         next_player = (current_player + 2) % 5

#         # Update the label to display the current player.
#         current_player_label.config(text="Current Player: {}".format(next_player))

#         # Draw the ball at the new location.
#         canvas.coords(ball, 100 * next_player, 100)

#         # Wait for a key press.
#         key = window.wait_key()

#         # If the key is "q", then quit the game.
#         if key == "q":
#             break

# # Create the window.
# window = tk.Tk()

# # Create a canvas to draw the circle.
# canvas = tk.Canvas(window, width=200, height=200)
# canvas.pack()

# # Create a ball.
# ball = canvas.create_oval(100, 100, 110, 110, fill="red")

# # Create a label to display the current player.
# current_player_label = tk.Label(window, text="Current Player: 1")
# current_player_label.pack()

# # Create a button to start the game.
# start_button = tk.Button(window, text="Start", command=start_game)
# start_button.pack()

# # Run the main loop.
# window.mainloop()

# ------------------------------------------------------------
"""
import tkinter as tk

def start_game():
    while True:
        # Get the current player.
        current_player = int(current_player_label.cget("text"))

        # Move the ball to the next player.
        next_player = (current_player + 2) % 5

        # Update the label to display the current player.
        current_player_label.config(text="Current Player: {}".format(next_player))

        # Draw the ball at the new location.
        canvas.coords(ball, 100 * next_player, 100)

        # Wait for a key press.
        key = window.wait_key()

        # If the key is "q", then quit the game.
        if key == "q":
            break

# Create the window.
window = tk.Tk()

# Create a canvas to draw the circle.
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# Create a ball.
ball = canvas.create_oval(100, 100, 110, 110, fill="red")

# Create a label to display the current player.
current_player_label = tk.Label(window, text="Current Player: 1")
current_player_label.pack()

# Create a button to start the game.
start_button = tk.Button(window, text="Start", command=start_game)
start_button.pack()

# Run the main loop.
window.mainloop()
"""

# ---------------------------------------------------------------------------------------------


# alice_card = "2 Heart"
# bob_card = "2 Heart"
# greatness_order = ["2", "3", "4", "5", "6", "7", "8", "9"]
# alice_number, alice_color = alice_card.split()
# bob_number, bob_color = bob_card.split()

# if alice_number != bob_number:
#     if greatness_order.index(alice_number) < greatness_order.index(bob_number):
#         print("Alice")
#     else:
#         print("Bob")
# else:
#     color_order = ["Spade", "Heart", "Diamond", "Club"]
#     if color_order.index(alice_color) < color_order.index(bob_color):
#         print("Alice")
#     elif color_order.index(alice_color) > color_order.index(bob_color):
#         print("Bob")
#     else:
#         print("Draw")


# -------------------------------------------------------------------

# T = 5
# N = 6
# K = 3

# for x in range(T):
#     A = [1, 2, 3, 4, 5, 6]

#     count = 0
#     for i in range(N):
#         for j in range(i+1, N):
#             if (i<j and (A[i] * A[j]) % K ) == 0:
#                 count += 1

#     print(count)

# -----------------------------------------------------------------------

# ary = [6,5,4,8,9,10,2,4,3]
# small = ary[0]
# for i in ary:
#     if small <= i:
#         # print(f"right now small is {small}")
#         continue
#     else:
#         small = i
#         # print(f"small changed to {small}")
# print(small)

# ----------------------------------------------------------------
"""
# this code is the python verison of anew tool written in go by tomnomnom 
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Append unique lines from stdin to a file')
    parser.add_argument('-q', action='store_true', help='quiet mode (no output at all)')
    parser.add_argument('-d', action='store_true', help="don't append to file, print new lines to stdout")
    parser.add_argument('-t', action='store_true', help='trim leading and trailing whitespace before comparison')
    parser.add_argument('filename', nargs='?', help='file to read and append to')
    args = parser.parse_args()

    lines = set()

    if args.filename:
        # read the whole file into a set if it exists
        try:
            with open(args.filename, 'r') as file:
                for line in file:
                    if args.t:
                        lines.add(line.strip())
                    else:
                        lines.add(line)
        except FileNotFoundError:
            pass

        if not args.d:
            # open the file for appending new stuff
            try:
                f = open(args.filename, 'a')
            except IOError as e:
                print(f"failed to open file for writing: {e}")
                return

    # read the lines, append and output them if they're new
    for line in sys.stdin:
        line = line.strip() if args.t else line
        if line in lines:
            continue

        # add the line to the set so we don't get any duplicates from stdin
        lines.add(line)

        if not args.q:
            print(line)
        if not args.d:
            if args.filename:
                f.write(line + '\n')

    if not args.d and args.filename:
        f.close()

if __name__ == "__main__":
    main()
"""

"""
ans = []

a = [2,4]
b = [16,32,96]
for i in range(4,17):
    if all(i%e == 0 for e in a) and all(e%i==0 for e in b): # all e's should be divisible by i, that i will be printed
        ans.append(i)
print(len(ans))
    
    # if all(e%i==0 for e in b):
    #     ans.append(i)
# for i in range(4,17): # either e divisible by i, that i will be printed
#     for e in a:
#         if i%e == 0:
#             print(i)
"""
# -----------------------------------------------------------------------
# s = "5 1 2 4 4 2 4 2 2 5 1 4 3 1 1 1 2 1 4 1"
# s = s.replace(" ",",")
# print(s)

# -----------------------------------------------------------------------
# def climbingLeaderboard(ranked, player):
#     unique_ranked = sorted(set(ranked), reverse=True)
#     rankings = []
#     i = len(unique_ranked) - 1  # Start from the last rank
    
#     for score in player:
#         while i >= 0 and score >= unique_ranked[i]:
#             i -= 1
#         rankings.append(i + 2)  # Add 2 because ranks are 1-based
        
#     return rankings

# # Example usage
# ranked = [100, 100, 50, 40, 40, 20, 10]
# player = [5, 25, 50, 120]
# result = climbingLeaderboard(ranked, player)
# print(result)  # Output: [4, 3, 1]

# -----------------------------------------------------------------------

# import os

# # Directory containing the files
# directory = r"C:\Users\Yash\Documents\Bca2_images\Life_updated"

# # List all files in the directory
# files = os.listdir(directory)

# # Iterate through the files and rename them
# for file in files:
#     if file.startswith("Slide"):
#         # Split the filename into two parts: "Slide" and the number
#         parts = file.split("Slide")
        
#         if len(parts) == 2:
#             # Extract the number
#             number = parts[1].split(".")[0]
            
#             # Rename the file with a space
#             new_name = f"Slide {number}.png"
            
#             # Construct the full paths for renaming
#             old_path = os.path.join(directory, file)
#             new_path = os.path.join(directory, new_name)
            
#             # Rename the file
#             os.rename(old_path, new_path)

# print("Files renamed successfully.")

# -------------------------------------------------------------------------------