import socket
import RSA

print("trying to connect")
s = socket.socket()
port = 12345
s.bind(('127.0.0.1', port))
s.listen(5)
c, addr = s.accept()
print("connected successfully")
print ("Socket Up and running with a connection from",addr)

def encrypt(plain_text):
    cipher_text = plain_text
    return cipher_text


while True:
    plain_text = input("sender: ")
    cipher_text = encrypt(plain_text)
    c.send(cipher_text.encode())
    
c.close()