from tkinter import *
import tkinter.messagebox
board = Tk()
board.title("Tic Tac Toe")
p1_score = StringVar()
p2_score = StringVar()

pt1 = 0
pt2 = 0
flag = True
counter = 1

def play(btn):
    global flag, counter
    if btn["text"] == " " and flag == True:
        flag=False 
        btn["text"] = "X"
        counter+=1
        Check()
    elif btn["text"] == " " and flag == False:
        flag = True
        btn["text"] = "O"
        counter+=1
        Check()
    else:
        tkinter.messagebox.showinfo("Learn TicTacToe", "Not allowed")

def ClearButton():
    bt1["text"] = " "
    bt2["text"] = " "
    bt3["text"] = " "
    bt4["text"] = " "
    bt5["text"] = " "
    bt6["text"] = " "
    bt7["text"] = " "
    bt8["text"] = " "
    bt9["text"] = " "

def Check():
    global pt1, pt2, p1_score, p2_score, counter
    
    if (bt1['text'] == 'X' and bt2['text'] == 'X' and bt3['text'] == 'X' or 
        bt4['text'] == 'X' and bt5['text'] == 'X' and bt6['text'] == 'X' or 
        bt7['text'] == 'X' and bt8['text'] == 'X' and bt9['text'] == 'X' or 
        bt1['text'] == 'X' and bt4['text'] == 'X' and bt7['text'] == 'X' or 
        bt2['text'] == 'X' and bt5['text'] == 'X' and bt8['text'] == 'X' or 
        bt3['text'] == 'X' and bt6['text'] == 'X' and bt9['text'] == 'X' or 
        bt1['text'] == 'X' and bt5['text'] == 'X' and bt9['text'] == 'X' or 
        bt3['text'] == 'X' and bt5['text'] == 'X' and bt7['text'] == 'X' or 
        bt1['text'] == 'X' and bt2['text'] == 'X' and bt3['text'] == 'X'):
        ClearButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 1 won")
        pt1+=1
        counter = 0
        p1_score.set(pt1)
        
    elif (bt1['text'] == 'O' and bt2['text'] == 'O' and bt3['text'] == 'O' or 
        bt4['text'] == 'O' and bt5['text'] == 'O' and bt6['text'] == 'O' or 
        bt7['text'] == 'O' and bt8['text'] == 'O' and bt9['text'] == 'O' or 
        bt1['text'] == 'O' and bt4['text'] == 'O' and bt7['text'] == 'O' or 
        bt2['text'] == 'O' and bt5['text'] == 'O' and bt8['text'] == 'O' or 
        bt3['text'] == 'O' and bt6['text'] == 'O' and bt9['text'] == 'O' or 
        bt1['text'] == 'O' and bt5['text'] == 'O' and bt9['text'] == 'O' or 
        bt3['text'] == 'O' and bt5['text'] == 'O' and bt7['text'] == 'O' or 
        bt1['text'] == 'O' and bt2['text'] == 'O' and bt3['text'] == 'O'):
        ClearButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Player 2 won")
        pt2+=1
        counter = 0
        p2_score.set(pt2)

    elif (counter == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Its a TIE")
        ClearButton()


bt1 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt1))
bt1.grid(row=1, column=0)

bt2 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt2))
bt2.grid(row=1, column=1)

bt3 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt3))
bt3.grid(row=1, column=2)

bt4 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt4))
bt4.grid(row=2, column=0)

bt5 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt5))
bt5.grid(row=2, column=1)

bt6 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt6))
bt6.grid(row=2, column=2)

bt7 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt7))
bt7.grid(row=3, column=0)

bt8 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt8))
bt8.grid(row=3, column=1)

bt9 = Button(board, text=" ", font='Times 15 bold', bg='black', fg='lime', bd=10, height=7, width=14, command=lambda: play(bt9))
bt9.grid(row=3, column=2)

label = Label(board, text="Score of Player 1 :", font='Times 15 bold', bg='red', fg='white')
label.grid(row=4, column=0, columnspan=2)
p1 = Entry(board, textvariable=p1_score, bd=15, width=15, bg='yellow', fg='red' )
p1.grid(row=4, column=2)
label = Label(board, text="Score of Player 2 :", font='Times 15 bold', bg='red', fg='white')
label.grid(row=5, column=0, columnspan=2)
p2 = Entry(board, textvariable=p2_score, bd=15, width=15, bg='yellow', fg='red')
p2.grid(row=5, column=2)

board.mainloop()
