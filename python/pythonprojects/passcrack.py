import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Password Cracker")

# create a label for the password input
password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0)

# create a password entry field
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1)

# create a function to check the password
def check_password():
    input_password = password_entry.get()
    with open("pass.txt", "r") as f:
        for line in f:
            if line.strip() == input_password:
                result_label.config(text=f"Password found : {input_password}.")
                return
    result_label.config(text="Password not found in list of common passwords.")

# create a button to run the password check
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

# create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)

# run the main loop
root.mainloop()
