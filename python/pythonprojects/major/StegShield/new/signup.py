from tkinter import * # type: ignore
from tkinter import messagebox
import re
import mysql.connector
import hashlib
import credentials as cred

root = Tk()
root.title('Signup')
root.geometry("925x600")
root.configure(bg='#fff')
root.resizable(False,False)

def hash_password(password):
        # Hash the password using SHA-256 algorithm
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        return hashed_password

def signup():
    fn = fname.get()
    ln = lname.get()
    email = mail.get()
    password = passwd.get()
    cnf_password = cnf_passwd.get()

    if not all([fn, ln, email, password, cnf_password]):
            messagebox.showerror("Error", "All fields are required")
            return
    if not fn.isalpha():
        messagebox.showerror("Error", "First name must contain only letters.")
        return
    if not ln.isalpha():
        messagebox.showerror("Error", "Last name must contain only letters.")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email address.")
        return
    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
        messagebox.showerror("Error", "Password must contain at least 8 characters including one letter, one number, and one special character.")
        return
    if password != cnf_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    
    hashed_password = hash_password(password)

    try:
        connection = mysql.connector.connect(
            host=cred.host,
            user=cred.user,
            password=cred.password,
            database=cred.database
        )
        cursor = connection.cursor()
        cursor.execute("select * from users where email=%s",(email,)) #pass email as tuple,list or dict, not directly
        row=cursor.fetchone()
        # print(row)
        # print(type(row))
        if row!=None:
            messagebox.showerror("Error!","The email id is already exists, please try again with another email id")
        else:
            sql = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            values = (fn, ln, email, hashed_password)
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Registration successful!")
            # clear_fields()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error: {error}")

    finally:
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()

img = PhotoImage(file='login2.png')
Label(root,image=img, bg='white').place(x=50,y=120)

frame = Frame(root,width=350,height=500,bg='white')
frame.place(x=480,y=60)

heading = Label(frame,text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=0)

def on_enter(e):  # type: ignore
    if fname.get() == 'First Name':
        fname.delete(0,'end')
def on_leave(e): # type: ignore
    if not fname.get():
        fname.insert(0,'First Name') 

fname = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
fname.place(x=30,y=80)
fname.insert(0,'First Name')
fname.bind('<FocusIn>',on_enter)
fname.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e): # type: ignore
    if lname.get() == "Last Name":
        lname.delete(0,'end')
def on_leave(e): # type: ignore
    if not lname.get():
        lname.insert(0,'Last Name')

lname = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
lname.place(x=30,y=150)
lname.insert(0,'Last Name')
lname.bind('<FocusIn>',on_enter)
lname.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def on_enter(e): # type: ignore
    if mail.get() == "Email":
        mail.delete(0,'end')
def on_leave(e): # type: ignore
    if not mail.get():
        mail.insert(0,'Email')

mail = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
mail.place(x=30,y=220)
mail.insert(0,'Email')
mail.bind('<FocusIn>',on_enter)
mail.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

def on_enter(e): # type: ignore
    if passwd.get() == "Password":
        passwd.delete(0,'end')
def on_leave(e): # type: ignore
    if not passwd.get():
        passwd.insert(0,'Password')

passwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
passwd.place(x=30,y=290)
passwd.insert(0,'Password')
passwd.bind('<FocusIn>',on_enter)
passwd.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)

def on_enter(e): 
    if cnf_passwd.get() == "Confirm Password":
        cnf_passwd.delete(0,'end')
def on_leave(e):
    if not cnf_passwd.get():
        cnf_passwd.insert(0,"Confirm Password")

cnf_passwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
cnf_passwd.place(x=30,y=360)
cnf_passwd.insert(0,'Confirm Password')
cnf_passwd.bind('<FocusIn>',on_enter)
cnf_passwd.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=387)

# # Add toggle buttons for showing and hiding passwords
# toggle_button_passwd = Button(frame, text='Show', command=lambda: toggle_password_visibility(passwd, toggle_button_passwd), bg='white', border=0, fg='blue', font=('Microsoft YaHei UI Light', 9))
# toggle_button_passwd.place(x=295, y=290)

# toggle_button_cnf_passwd = Button(frame, text='Show', command=lambda: toggle_password_visibility(cnf_passwd, toggle_button_cnf_passwd), bg='white', border=0, fg='blue', font=('Microsoft YaHei UI Light', 9))
# toggle_button_cnf_passwd.place(x=295, y=360)

Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=424)
label = Label(frame,text="I have an account.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=470)
sign_up=Button(frame,width=6,text='Sign In',bg='white',fg='#57a1f8',border=0,cursor='hand2').place(x=215,y=470)

root.mainloop()
