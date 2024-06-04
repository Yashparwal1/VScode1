from tkinter import *  # type: ignore
from tkinter import messagebox
import mysql.connector
import credentials as cred
import hashlib

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    user_email = mail.get()
    user_password = passwd.get()
    if user_email=='' and user_password=='':
        messagebox.showerror("Error!","All fields are required")
    else:
        try:
            connection = mysql.connector.connect(
                host=cred.host,
                user=cred.user,
                password=cred.password,
                database=cred.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE email=%s",(user_email,))
                row = cursor.fetchone()
                if row:
                    stored_password = row[4] # type: ignore
                    hashed_password = hashlib.sha256(user_password.encode()).hexdigest()
                    if hashed_password == stored_password:
                        messagebox.showinfo("Success", "Login Successful")
                    else:
                        messagebox.showerror("Error!", "Invalid Password")
                else:
                    messagebox.showerror("Error!", "User not found")
                cursor.close()
                connection.close()
        except mysql.connector.Error as error:
            print(cred.user)
            messagebox.showerror("Error", f"Error: {error}")
        
    
img = PhotoImage(file='login2.png')
Label(root,image=img, bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e): # type: ignore
    if mail.get() == "Email":
        mail.delete(0,'end')
def on_leave(e): # type: ignore
    if not mail.get():
        mail.insert(0,'Email')

mail = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
mail.place(x=30,y=80)
mail.insert(0,'Email')
mail.bind('<FocusIn>',on_enter)
mail.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_Penter(e):
    if passwd.get() == "Password":
        passwd.delete(0,'end')
def on_Pleave(e):
    if not passwd.get():
        passwd.insert(0,'Password')

passwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
passwd.place(x=30,y=150)
passwd.insert(0,'Password')
passwd.bind('<FocusIn>',on_Penter)
passwd.bind('<FocusOut>',on_Pleave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='Sign up',bg='white',fg='#57a1f8',border=0,cursor='hand2').place(x=215,y=270)
root.mainloop()
