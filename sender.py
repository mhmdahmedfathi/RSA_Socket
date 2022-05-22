import socket
import RSA

print("Trying to connect...")
s = socket.socket()
port = 12345
s.bind(('127.0.0.1', port))
s.listen(5)
c, addr = s.accept()
print("connected successfully")
print("Socket Up and running with a connection from", addr)


def encrypt(plain_text, n, e):
    str_encrypted = ""
    for x in range(0, len(plain_text)):
        str_encrypted += RSA.Encrypt(plain_text[x], n, e)
    cipher_text = str_encrypted
    return cipher_text


n_str = c.recv(1024)
e_str = c.recv(1024)

n = RSA.ConvertToInt(n_str.decode())
e = RSA.ConvertToInt(e_str.decode())


try:
    while True:
        plain_text = input("Sender: ")
        cipher_text = encrypt(plain_text, n, e)
        c.send(cipher_text.encode())
except KeyboardInterrupt:
    c.close()
    exit(0)
