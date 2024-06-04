from tkinter import *
from tkinter import messagebox
import mysql.connector
import re
import hashlib


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.create_widgets()

        self.root.favicon = PhotoImage(file="favicon.jpg")
        self.root.iconphoto(False, self.root.favicon)
        self.root.mainImg = PhotoImage(file="img.png")
        Label(root,image=self.root.mainImg,bg="#000000").place(x=10,y=0)
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = Label(self.root, text="User Registration", font=("Arial", 20), bg="#f0f0f0")
        title_label.pack(pady=10)

        # First Name
        self.first_name_var = StringVar()
        first_name_label = Label(self.root, text="First Name:", bg="#f0f0f0")
        first_name_label.pack(anchor="w", padx=20)
        self.first_name_entry = Entry(self.root, textvariable=self.first_name_var)
        self.first_name_entry.pack(pady=5, padx=20)

        # Last Name
        self.last_name_var = StringVar()
        last_name_label = Label(self.root, text="Last Name:", bg="#f0f0f0")
        last_name_label.pack(anchor="w", padx=20)
        self.last_name_entry = Entry(self.root, textvariable=self.last_name_var)
        self.last_name_entry.pack(pady=5, padx=20)

        # Email
        self.email_var = StringVar()
        email_label = Label(self.root, text="Email:", bg="#f0f0f0")
        email_label.pack(anchor="w", padx=20)
        self.email_entry = Entry(self.root, textvariable=self.email_var)
        self.email_entry.pack(pady=5, padx=20)

        # Password
        self.password_var = StringVar()
        password_label = Label(self.root, text="Password:", bg="#f0f0f0")
        password_label.pack(anchor="w", padx=20)
        self.password_entry = Entry(self.root, textvariable=self.password_var, show="*")
        self.password_entry.pack(pady=5, padx=20)

        # Confirm Password
        self.confirm_password_var = StringVar()
        confirm_password_label = Label(self.root, text="Confirm Password:", bg="#f0f0f0")
        confirm_password_label.pack(anchor="w", padx=20)
        self.confirm_password_entry = Entry(self.root, textvariable=self.confirm_password_var, show="*")
        # self.confirm_password_entry.insert(0,"Password")
        self.confirm_password_entry.pack(pady=5, padx=20)

        # Terms and Conditions
        self.terms_var = BooleanVar()
        terms_check = Checkbutton(self.root, text="I agree to the Terms and Conditions", variable=self.terms_var, bg="#f0f0f0")
        terms_check.pack(anchor="w", padx=20)

        # Register Button
        register_button = Button(self.root, text="Register", command=self.register_user)
        register_button.pack(pady=10)


    def hash_password(self, password):
        # Hash the password using SHA-256 algorithm
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        return hashed_password

    def register_user(self):
        # Get user inputs
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        email = self.email_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()
        agree_terms = self.terms_var.get()

        # Validation checks
        if not all([first_name, last_name, email, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required")
            return
        if not first_name.isalpha():
            messagebox.showerror("Error", "First name must contain only letters.")
            return
        if not last_name.isalpha():
            messagebox.showerror("Error", "Last name must contain only letters.")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email address.")
            return
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            messagebox.showerror("Error", "Password must contain at least 8 characters including one letter, one number, and one special character.")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        if not agree_terms:
            messagebox.showerror("Error", "Please agree to the Terms and Conditions.")
            return

        # Hash the password
        hashed_password = self.hash_password(password)

        # Database connection and registration
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="user_registration"
            )
            cursor = connection.cursor()

            sql = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, hashed_password)
            cursor.execute(sql, values)
            connection.commit()

            messagebox.showinfo("Success", "Registration successful!")
            self.clear_fields()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error: {error}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                cursor.close()
                connection.close()

    def clear_fields(self):
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.email_var.set("")
        self.password_var.set("")
        self.confirm_password_var.set("")
        self.terms_var.set(False)

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
