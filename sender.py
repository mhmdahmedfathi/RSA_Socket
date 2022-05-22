from RSA import *
import socket

print("Trying to connect...")
s = socket.socket()
port = 1234
s.bind(('127.0.0.1', port))
s.listen(5)
c, addr = s.accept()
print("Connected successfully!")
print("Socket is up and running with a connection from", addr)


def encrypt(plain_text, n, e):
    str_encrypted = ""
    for x in range(0, len(plain_text)):
        str_encrypted += Encrypt(plain_text[x], n, e)
    cipher_text = str_encrypted
    return cipher_text


# Receive the public key from the receiver
n_str = c.recv(1024)
e_str = c.recv(1024)

n = ConvertToInt(n_str.decode())
e = ConvertToInt(e_str.decode())

print("-------------------------------------------------------")
print("PUBLIC KEY:", "n =", n, "e =", e)
print("-------------------------------------------------------")

try:
    while True:
        plain_text = input("Sender: ")
        cipher_text = encrypt(plain_text, n, e)
        c.send(cipher_text.encode())
except KeyboardInterrupt:
    c.close()
    exit(0)
