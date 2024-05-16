from pydoc import plain
from tkinter import * # type: ignore
from tkinter import filedialog,messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from numpy import imag
from pyparsing import null_debug_action
from stegano import lsb
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


root = Tk()
root.title("StegShielg")
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
    lbl.image=img # type: ignore

def enc_msg(public_key, message):
    cipher_text = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
    )
    print("****CIPHER TEXT****\n",cipher_text)
    return cipher_text

def dec_msg(output, private_key):
    plain_text = private_key.decrypt(
            output,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
    )
    print("****PLAIN TEXT****\n",plain)
    return plain_text

def hideData():
    global hide_message
    Key = key.get()
    # if Key=='0000':
    if Key:
        message=text1.get(1.0,END)
        with open("public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
        cipher_text = enc_msg(public_key, message)
        hide_message = lsb.hide(filename,cipher_text.decode('latin-1'))
        messagebox.showinfo("Success","Message Hidden Successfully. Save Your Image !!")
        key.set('')
        # print(type(hide_message)) #it is of PIL.Image type
        text1.delete(1.0,END)
        # lbl.destroy() #will destroy the complete lable 
    elif Key=='':
        messagebox.showerror("Error","Please enter Scrert Key !!")
    else:
        messagebox.showerror("Error","Wrong Scrert Key !!")
        key.set('')

def saveImg():
    hide_message.save("hidden.png")
    messagebox.showinfo("Success","Image Saved with the name \"Hidden.png\"")
    lbl.config(image='',width=0,height=0)
    lbl.image=None # type: ignore

def showData():
    Key = key.get()
    if Key=='0000':
        output = lsb.reveal(filename).encode('latin-1')
        with open("private_key.pem", "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), backend=default_backend(), password=None)
        plain_text = dec_msg(output, private_key)
        text1.delete(1.0,END)
        text1.insert(1.0,plain_text.decode())
        key.set('')
    elif Key=='':
        messagebox.showerror("Error","Please enter Scrert Key !!")
    else:
        messagebox.showerror("Error","Wrong Scrert Key !!")
        key.set('')
    
# favicon
image_icon = PhotoImage(file="favicon.jpg")
root.iconphoto(False,image_icon)

# logo and heading
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#000000").place(x=10,y=0)
Label(root,text="StegShield", bg="#000000", fg="white",font="arial 25 bold").place(x=100,y=20)

# first frame (image area)
f1 = Frame(root,bd=3,bg="#000000", width=330,height=295,relief=GROOVE)
f1.place(x=10,y=80)
lbl=Label(f1,bg="black")
lbl.place(x=40,y=10)

# seconf frame (text area)
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

# thrid frame (open and save image)
f3 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=440)
Label(f3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)
Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",cursor='hand2',command=openImg).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",cursor='hand2',command=saveImg).place(x=180,y=30)

# fourth frame (hide and show data buttons)
f4 = Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=440)
Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",cursor='hand2',command=hideData).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",cursor='hand2',command=showData).place(x=180,y=30)
Label(f4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()


