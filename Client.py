import socket
import RSA

s = socket.socket()
s.connect(('127.0.0.1',12345))

def decrypt(cipher_text):
    
    plain_text = cipher_text
    
    return plain_text


while True:
    cipher = s.recv(1024)
    plain_text = decrypt(cipher.decode())
    print ("sender:",plain_text)
s.close()