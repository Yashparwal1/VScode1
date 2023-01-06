import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number , message):
    url='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':'QKVco4hHnpdwIGOlqsDL29v5EUF7au3CBmJZgfYMr0AykjSbP183OZMwvGo97FPKTJaqzRNLgf6HVj2Q',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route': 'p',
        'numbers':number
    }

    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


#creating GUI
def btnclick():
    num = tonumber.get()
    msg = tomsg.get("1.0",END)
    sent = send_sms(num,msg)
    if sent == True:
        showinfo("Sent Success", "Message Successfully Sent")
    else:
        showerror("Error", "Something went wrong")


admin = Tk()
admin.title("Message sender")
admin.geometry("450x600")
font = ("Verdana",24,"bold")

tonumber=Entry(admin, font=font)
tonumber.pack(fill=X,pady=25)

tomsg = Text(admin)
tomsg.pack(fill=X)

btnsend = Button(admin, text="Send Message",command=btnclick)
btnsend.pack()

admin.mainloop()
