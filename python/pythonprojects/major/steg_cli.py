from email import message
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from stegano import lsb
from PIL import Image
class Asymmetric:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def save_keys(self):
        with open('private_key.pem', 'wb') as f:
            f.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )
        with open("public_key.pem", 'wb') as f:
            f.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )
    
    #reveiver send its public key to the sender bu any means, but since we are both the sender and receiver here, so we will load both public and private keys
    def load_public_key(self, file_path):
        with open(file_path, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
        return public_key
    def load_private_key(self, file_path):
        with open(file_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), backend=default_backend(), password=None)
        return private_key
    """
    def print_public_key(self):
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(pem.decode()) #Prints the public key in PEM format.
    def print_private_key(self):
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        print(pem.decode()) #Prints the private key in PEM format.
    """
    
    def enc_msg(self, message, public_key):
        cipher_text = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return cipher_text
    
    def dec_msg(self, cipher_text, private_key):
        plain_text = private_key.decrypt(
            cipher_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plain_text
    
    def hide(self, imgFile, cipher_text):
        hidden = lsb.hide(imgFile, cipher_text.decode('latin-1'))
        hidden.save("stego.png")
        return "Successfully hidden !!"
    def extract(self, imgFile):
        extracted_data = lsb.reveal(imgFile)
        return extracted_data.encode('latin-1')

if __name__ == "__main__":
    key_sys = Asymmetric()
    key_sys.save_keys()
    public_key = key_sys.load_public_key("public_key.pem")
    private_key = key_sys.load_private_key("private_key.pem")

    message = "Test message"
    cipher_text = key_sys.enc_msg(message,public_key)
    print("Encrypted: ",cipher_text)

    hide_data = key_sys.hide("test.png", cipher_text)
    print(hide_data)
    
    show_data = key_sys.extract("stego.png")
    print("Data extracted: ",show_data)
    print("Decrypting data....")

    plain_text = key_sys.dec_msg(show_data, private_key)
    print("Decrypted: ", plain_text.decode())

    
