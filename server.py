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

def encrypt(plain_text,n,e):
    str_encrypted = ""
    byte_plain = plain_text.encode()
    if len(byte_plain )% 4 != 0 :
        for x in range(0,4 - len(byte_plain)% 4 ):
                  byte_plain += bytes(0)      
    for x in range(0,len(byte_plain),4):
        if(x+4 <= len(byte_plain)) :
            str_encrypted += RSA.Encrypt( str(int.from_bytes(byte_plain[x:x+4],"big")), n, e)
    cipher_text = str_encrypted
    print(plain_text,cipher_text,n,e)
    return cipher_text


n_str = c.recv(1024)
n = RSA.ConvertToInt(n_str.decode())
e_str = c.recv(1024)
e = RSA.ConvertToInt(e_str.decode())


while True:
    plain_text = input("sender: ")
    cipher_text = encrypt(plain_text,n,e)
    c.send(cipher_text.encode())
    
c.close()