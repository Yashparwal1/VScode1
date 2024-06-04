from tkinter import * # type: ignore
from tkinter import messagebox
import re
import mysql.connector
import hashlib
import credentials as cred
# from login_class import Login


class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title('Signup')
        self.root.geometry("925x600")
        self.root.configure(bg='#fff')
        self.root.resizable(False,False)
        
        self.root.img = PhotoImage(file='login2.png')
        Label(root,image=self.root.img, bg='white').place(x=50,y=120)
        self.create_widgets()

    def on_Fenter(self,e):  # type: ignore
        if self.fname.get() == 'First Name':
            self.fname.delete(0,'end')
    def on_Fleave(self,e): # type: ignore
        if not self.fname.get():
            self.fname.insert(0,'First Name') 

    def on_Lenter(self,e): # type: ignore
        if self.lname.get() == "Last Name":
            self.lname.delete(0,'end')
    def on_Lleave(self,e): # type: ignore
        if not self.lname.get():
            self.lname.insert(0,'Last Name')
    
    def on_Menter(self,e): # type: ignore
        if self.mail.get() == "Email":
            self.mail.delete(0,'end')
    def on_Mleave(self,e): # type: ignore
        if not self.mail.get():
            self.mail.insert(0,'Email')

    def on_Penter(self,e): # type: ignore
        if self.passwd.get() == "Password":
            self.passwd.delete(0,'end')
    def on_Pleave(self,e): # type: ignore
        if not self.passwd.get():
            self.passwd.insert(0,'Password')

    def on_CPenter(self,e): 
        if self.cnf_passwd.get() == "Confirm Password":
            self.cnf_passwd.delete(0,'end')
    def on_CPleave(self,e):
        if not self.cnf_passwd.get():
            self.cnf_passwd.insert(0,"Confirm Password")

    def create_widgets(self):
        self.frame = Frame(self.root,width=350,height=500,bg='white')
        self.frame.place(x=480,y=60)
        self.heading = Label(self.frame,text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=100,y=0)
        #First Name Frame
        self.fname = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.fname.place(x=30,y=80)
        self.fname.insert(0,'First Name')
        self.fname.bind('<FocusIn>',self.on_Fenter)
        self.fname.bind('<FocusOut>',self.on_Fleave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=107)
        #Second Name Frame
        self.lname = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.lname.place(x=30,y=150)
        self.lname.insert(0,'Last Name')
        self.lname.bind('<FocusIn>',self.on_Lenter)
        self.lname.bind('<FocusOut>',self.on_Lleave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=177)
        #Email Frame
        self.mail = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.mail.place(x=30,y=220)
        self.mail.insert(0,'Email')
        self.mail.bind('<FocusIn>',self.on_Menter)
        self.mail.bind('<FocusOut>',self.on_Mleave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=247)
        #Password Frame
        self.passwd = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.passwd.place(x=30,y=290)
        self.passwd.insert(0,'Password')
        self.passwd.bind('<FocusIn>',self.on_Penter)
        self.passwd.bind('<FocusOut>',self.on_Pleave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=317)
        #Confirm Password Frame
        self.cnf_passwd = Entry(self.frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        self.cnf_passwd.place(x=30,y=360)
        self.cnf_passwd.insert(0,'Confirm Password')
        self.cnf_passwd.bind('<FocusIn>',self.on_CPenter)
        self.cnf_passwd.bind('<FocusOut>',self.on_CPleave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=387)

        # # Add toggle buttons for showing and hiding passwords
        # toggle_button_passwd = Button(frame, text='Show', command=lambda: toggle_password_visibility(passwd, toggle_button_passwd), bg='white', border=0, fg='blue', font=('Microsoft YaHei UI Light', 9))
        # toggle_button_passwd.place(x=295, y=290)

        # toggle_button_cnf_passwd = Button(frame, text='Show', command=lambda: toggle_password_visibility(cnf_passwd, toggle_button_cnf_passwd), bg='white', border=0, fg='blue', font=('Microsoft YaHei UI Light', 9))
        # toggle_button_cnf_passwd.place(x=295, y=360)
        
        Button(self.frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=self.signup).place(x=35,y=424)
        self.label = Label(self.frame,text="I have an account.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        self.label.place(x=75,y=470)
        self.sign_in=Button(self.frame,width=6,text='Sign In',bg='white',fg='#57a1f8',border=0,cursor='hand2',command=self.open_login_page).place(x=215,y=470)

    def open_login_page(self):
        self.root.destroy()
        # root = Tk()
        # login = Login(root)
        # root.mainloop()
        pass

    def hash_password(self,password):
            # Hash the password using SHA-256 algorithm
            hash_object = hashlib.sha256(password.encode())
            hashed_password = hash_object.hexdigest()
            return hashed_password

    def signup(self):
        fn = self.fname.get()
        ln = self.lname.get()
        email = self.mail.get()
        password = self.passwd.get()
        cnf_password = self.cnf_passwd.get()

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
        
        hashed_password = self.hash_password(password)

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
                self.reset_fields()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()

    def reset_fields(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.mail.delete(0, END)
        self.passwd.delete(0, END)
        self.cnf_passwd.delete(0, END)
        self.fname.insert(0, 'First Name')
        self.lname.insert(0, 'Last Name')
        self.mail.insert(0, 'Email')
        self.passwd.insert(0, 'Password')
        self.cnf_passwd.insert(0, 'Confirm Password')


if __name__ == "__main__":
    root = Tk()
    app = Signup(root)
    root.mainloop()




















