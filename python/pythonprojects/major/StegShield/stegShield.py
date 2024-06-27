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


class StegoTool:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Stego tool")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")

        # Load logo and favicon
        self.root.favicon = PhotoImage(file="favicon.jpg")
        self.root.iconphoto(False, self.root.favicon)
        self.root.logo = PhotoImage(file="logo.png")
        Label(root,image=self.root.logo,bg="#000000").place(x=10,y=0)
        Label(root,text="StegShield", bg="#000000", fg="white",font="arial 25 bold").place(x=100,y=20)

        self.create_widgets()

    def create_widgets(self):
        # First frame (image area)
        self.f1 = Frame(self.root, bd=3, bg="#000000", width=330, height=295, relief=GROOVE)
        self.f1.place(x=10, y=80)
        self.lbl = Label(self.f1, bg="black")
        self.lbl.place(x=40, y=10)

        # Second frame (text area)
        self.f2 = Frame(self.root, bd=3, width=330, height=295, bg="grey", relief=GROOVE)
        self.f2.place(x=360, y=80)
        self.text1 = Text(self.f2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=330, height=295)

        # Secret key entry
        Label(self.root, text="SECRET KEY", font='5', bg='black', fg='red').place(x=285, y=380)
        self.key = StringVar()
        self.e = Entry(self.root, textvariable=self.key, bd=2, font="impact 10 bold", show='*')
        self.e.place(x=265, y=410)

        # Scrollbar for text area
        self.scrollbar1 = Scrollbar(self.f2)
        self.scrollbar1.place(x=320, y=0, height=300)
        self.scrollbar1.configure(command=self.text1.yview)
        self.text1.configure(yscrollcommand=self.scrollbar1.set)

        # Third frame (open and save image)
        self.f3 = Frame(self.root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
        self.f3.place(x=10, y=440)
        Label(self.f3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)
        Button(self.f3, text="Open Image", width=10, height=2, font="arial 14 bold", cursor='hand2',
               command=self.openImg).place(x=20, y=30)
        Button(self.f3, text="Save Image", width=10, height=2, font="arial 14 bold", cursor='hand2',
               command=self.saveImg).place(x=180, y=30)

        # Fourth frame (hide and show data buttons)
        self.f4 = Frame(self.root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
        self.f4.place(x=360, y=440)
        Button(self.f4, text="Hide Data", width=10, height=2, font="arial 14 bold", cursor='hand2',
               command=self.hideData).place(x=20, y=30)
        Button(self.f4, text="Show Data", width=10, height=2, font="arial 14 bold", cursor='hand2',
               command=self.showData).place(x=180, y=30)
        Label(self.f4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

    def openImg(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                                   filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"),
                                                              ("All files", "*.txt")))
        img = Image.open(self.filename)
        img = ImageTk.PhotoImage(img)
        self.lbl.configure(image=img, width=250, height=250)
        self.lbl.image = img # type: ignore

    def enc_msg(self, public_key, message):
        cipher_text = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("****CIPHER TEXT****\n", cipher_text)
        return cipher_text

    def dec_msg(self, output, private_key):
        plain_text = private_key.decrypt(
                output,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
        )
        return plain_text

    def hideData(self):
        global hide_message
        Key = self.key.get()
        # if Key=='0000':
        if Key:
            message=self.text1.get(1.0,END)
            with open("public_key.pem", "rb") as f:
                public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
            cipher_text = self.enc_msg(public_key, message)
            hide_message = lsb.hide(self.filename,cipher_text.decode('latin-1'))
            messagebox.showinfo("Success","Message Hidden Successfully. Save Your Image !!")
            self.key.set('')
            # print(type(hide_message)) #it is of PIL.Image type
            self.text1.delete(1.0,END)
            # lbl.destroy() #will destroy the complete lable 
        elif Key=='':
            messagebox.showerror("Error","Please enter Scrert Key !!")
        else:
            messagebox.showerror("Error","Wrong Scrert Key !!")
            self.key.set('')

    def saveImg(self):
        hide_message.save("hidden.png")
        messagebox.showinfo("Success","Image Saved with the name \"Hidden.png\"")
        self.lbl.config(image='',width=0,height=0)
        self.lbl.image=None # type: ignore

    def showData(self):
        Key = self.key.get()
        if Key=='0000':
            output = lsb.reveal(self.filename).encode('latin-1')
            with open("private_key.pem", "rb") as f:
                private_key = serialization.load_pem_private_key(f.read(), backend=default_backend(), password=None)
            plain_text = self.dec_msg(output, private_key)
            self.text1.delete(1.0,END)
            self.text1.insert(1.0,plain_text.decode())
            self.key.set('')
        elif Key=='':
            messagebox.showerror("Error","Please enter Scrert Key !!")
        else:
            messagebox.showerror("Error","Wrong Scrert Key !!")
            self.key.set('')
    

if __name__ == "__main__":
    root = Tk()
    app = StegoTool(root)
    # root.title("StegShielg")
    # root.geometry("700x600")
    # root.resizable(False,False)
    # root.configure(bg="#000000")

    # image_icon = PhotoImage(file="favicon.jpg")
    # root.iconphoto(False,image_icon)

    # logo=PhotoImage(file="logo.png")
    # Label(root,image=logo,bg="#000000").place(x=10,y=0)
    # Label(root,text="StegShield", bg="#000000", fg="white",font="arial 25 bold").place(x=100,y=20)

    root.mainloop()