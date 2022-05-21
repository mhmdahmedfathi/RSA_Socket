import socket
import RSA
from Crypto.Util import number
from math import log2
import os
n_length = 32
s = socket.socket()
s.connect(('127.0.0.1',12345))


def Auto_key_generation():
    p = number.getPrime(n_length//2)
    q = number.getPrime(n_length//2)
    while p == q :
        q = number.getPrime(n_length//2)
     
    n = p * q
    phi_n = (p-1)*(q-1)
    e = number.getPrime(int(log2(phi_n)))
    while(RSA.GCD(phi_n, e) != 1):
        e = number.getPrime(int(log2(phi_n)))
    d = RSA.InvertModulo(e, phi_n)
    return e,d,n,p,q


def Manual_key_generation(string):
    
    p,q,e = string.split(",")
    n = p * q
    phi_n = (p-1)*(q-1)
    d = RSA.InvertModulo(e, phi_n)
    return e,d,n,p,q

def decrypt(cipher_text,p,q,e):
    
    
    plain_text = RSA.Decrypt(int(cipher_text).decode("ascii"), p, q, e)
    
    return plain_text

#start sendingg

Auto_Or_Manual = input("Do you want key generation to be automatic or manual ? 1 for auto , 2 for manual    ")
if int(Auto_Or_Manual) == 1 :
    e,d,n,p,q = Auto_key_generation()
elif int(Auto_Or_Manual) == 2 :
    e,d,n,p,q = Manual_key_generation(input("Please enter p,q,e saperated by comma"))
s.send(RSA.ConvertToStr(n).encode())
s.send(RSA.ConvertToStr(e).encode())

while True:
    cipher = s.recv(1024)
    plain_text = decrypt(cipher.decode(),p,q,e)
    print ("sender:",plain_text)
    

s.close()