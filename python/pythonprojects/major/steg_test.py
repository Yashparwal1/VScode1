# from cProfile import label
# from cgitb import text
# from email import message
# import secrets
# from click import secho
from tkinter import * #type: ignore
from tkinter import filedialog,messagebox
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
from numpy import imag
from pyparsing import null_debug_action
from stegano import lsb
import hashlib

root = Tk()
root.title("Stego tool")
root.geometry("700x600")
root.resizable(False,False)
root.configure(bg="#000000")

def openImg():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                        filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All files","*.txt")))
    img = Image.open(filename) #open dialog
    img = ImageTk.PhotoImage(img) #select image
    lbl.configure(image=img,width=250,height=250) #and show in lable in app
    lbl.image=img #type: ignore

def hideData():
    global hide_message
    Key = key.get()
    print("key === ",Key)
    message = text1.get(1.0, END).strip()  # Retrieve the message from the text widget

    if Key:
        # Generate a hash of the user-provided key
        hashed_key = hashlib.sha256(Key.encode()).digest()
        length_of_hashed_key = len(hashed_key)
        print("hashed key === ",hashed_key)
        print("length: ",length_of_hashed_key)
        # # Encrypt the message using the hashed key
        # encrypted_message = lsb.hide(str(filename), message)

        # Embed the hashed key along with the encrypted message in the stego image
        combined_data = length_of_hashed_key.to_bytes(1, byteorder='big') + hashed_key + message.encode()
        # combined_data = str(hashed_key) + message
        print("combined === ", combined_data)
        hide_message = lsb.hide(filename, str(combined_data))
        
        messagebox.showinfo("Success", "Message Hidden Successfully. Save Your Image !!")
        key.set('')
        text1.delete(1.0, END)
    else:
        messagebox.showerror("Error", "Please enter Secret Key !!")

def saveImg():
    hide_message.save("hidden.png")
    messagebox.showinfo("Success","Image Saved with the name \"Hidden.png\"")
    lbl.config(image='',width=0,height=0)
    lbl.image=None # type: ignore
    
def showData():
    Key = key.get()

    if Key:
        # Generate a hash of the user-provided key
        hashed_key = hashlib.sha256(Key.encode()).digest()

        # Retrieve the combined data (hashed key + encrypted message) from the stego image
        combined_data = lsb.reveal(filename)
        print("combined in show === ", combined_data)
        # Extract the hashed key from the combined data
        stored_hashed_key = combined_data[:32]  # Assuming the length of the hashed key is 32 bytes (256 bits)
        print("stored === ", stored_hashed_key)
        # Verify if the provided key matches the stored hashed key
        if hashed_key == stored_hashed_key:
            # Decrypt the message using the hashed key
            encrypted_message = combined_data[32:]  # Extract the encrypted message
            decrypted_message = lsb.reveal(encrypted_message)
            
            # Display the decrypted message
            text1.delete(1.0, END)
            text1.insert(END, decrypted_message)
            key.set('')
        else:
            messagebox.showerror("Error", "Wrong Secret Key !!")
    else:
        messagebox.showerror("Error", "Please enter Secret Key !!")

# favicon
image_icon = PhotoImage(file="favicon.jpg")
root.iconphoto(False,image_icon)

# logo and heading
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#000000").place(x=10,y=0)
Label(root,text="CYBER K3TON", bg="#000000", fg="white",font="arial 25 bold").place(x=100,y=20)

# first frame 
f1 = Frame(root,bd=3,bg="#000000", width=330,height=295,relief=GROOVE)
f1.place(x=10,y=80)
lbl=Label(f1,bg="black")
lbl.place(x=40,y=10)

# seconf frame 
f2 = Frame(root,bd=3,width=330,height=295,bg="grey",relief=GROOVE)
f2.place(x=360,y=80)
text1=Text(f2,font="Robote 20", bg="white", fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=330,height=295)

# secret key
Label(root, text="SECRET KEY", font='5', bg='black', fg='red').place(x=285,y=380)
key = StringVar()
e = Entry(root,textvariable=key,bd=2,font="impact 10 bold",show='*')
e.place(x=265,y=410)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# thrid frame
f3 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=440)
Label(f3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)
Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",cursor='hand2',command=openImg).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",cursor='hand2',command=saveImg).place(x=180,y=30)

# fourth frame 
f4 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=440)
Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",cursor='hand2',command=hideData).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",cursor='hand2',command=showData).place(x=180,y=30)
Label(f4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()


