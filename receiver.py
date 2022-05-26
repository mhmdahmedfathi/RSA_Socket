from cmath import isnan
from Crypto.Util import number
from math import log2
from RSA import *
import socket
import sympy

s = socket.socket()
s.connect(('127.0.0.1', 1234))


def Auto_key_generation(n_length=64):
    p = number.getPrime(n_length // 2)
    q = number.getPrime(n_length // 2)

    while p == q:
        q = number.getPrime(n_length // 2)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = number.getPrime(int(log2(phi_n)))
    while GCD(phi_n, e) != 1:
        e = number.getPrime(int(log2(phi_n)))

    d = InvertModulo(e, phi_n)
    bits_needed = n_length // 8

    return e, d, n, p, q, bits_needed


def Manual_key_generation(string):
    p, q, e = (string.replace(" ", "").split(","))

    if not p.isnumeric():
        print("p must be a number")
        return 1, 1, 1, 1, 1, 1
    
    if not q.isnumeric():
        print("q must be a number")
        return 1, 1, 1, 1, 1, 1
    
    if not e.isnumeric():
        print("e must be a number")
        return 1, 1, 1, 1, 1, 1

    p = int(p)
    q = int(q)
    e = int(e)

    phi_n = (p - 1) * (q - 1)

    
    if not sympy.isprime(p):
        print("p must be a prime number")
        return 1, 1, 1, 1, 1, 1
    
    if not sympy.isprime(q):
        print("q must be a prime number")
        return 1, 1, 1, 1, 1, 1
    
    if not sympy.isprime(e):
        print("e must be a prime number")
        return 1, 1, 1, 1, 1, 1
    
    if p == q:
        print("p and q must be different")
        return 1, 1, 1, 1, 1, 1
    
    if p == 1:
        print("p must be greater than 1")
        return 1, 1, 1, 1, 1, 1
    
    if q == 1:
        print("q must be greater than 1")
        return 1, 1, 1, 1, 1, 1
    
    if GCD(phi_n, e) != 1:
        print("e must be coprime to phi_n")
        return 1, 1, 1, 1, 1, 1
    
    if e > phi_n:
        print("e must be less than phi_n")
        return 1, 1, 1, 1, 1, 1
    
    if e < 2:
        print("e must be greater than 1")
        return 1, 1, 1, 1, 1, 1

    n = p * q
    d = InvertModulo(e, phi_n)
    bits_needed = p.bit_length() // 4

    return e, d, n, p, q, bits_needed


def decrypt(cipher_text, n, d, bits_needed):
    decrypt = ""
    str_plain = ""

    for x in range(0, len(cipher_text), bits_needed):
        decrypt = Decrypt(cipher_text[x:x+bits_needed], n, d)
        str_plain += decrypt

    plain_text = str_plain

    return plain_text


# start sending
e = d = n = q = p = 1

while p == 1:
    try:
        Auto_Or_Manual = int(input("Do you want key generation to be (1) automatic or (2) manual?\n"))
        if Auto_Or_Manual == 1:
            e, d, n, p, q, bits_needed = Auto_key_generation()
        elif Auto_Or_Manual == 2:
            e, d, n, p, q, bits_needed = Manual_key_generation(input("Please enter p, q, e separated by comma:\n"))
    except KeyboardInterrupt:
        print("\nExiting...")
        s.send(b"exit")
        s.close()
        exit(0)

# Send acknowledgement to sender
s.send(b"ok")

# Send the public key to the sender
s.send(ConvertToStr(n).encode())
s.send(ConvertToStr(e).encode())

print("-------------------------------------------------------")
print("PUBLIC KEY:", "n =", n, "\te =", e)
print("-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("PRIVATE KEY:", "n =", n, "\td =", d)
print("-------------------------------------------------------")

while True:
    try:
        cipher = s.recv(1024)

        if cipher == b"exit":
            raise KeyboardInterrupt
        
        plain_text = decrypt(cipher.decode('utf-8', 'ignore'), n, d, bits_needed)
        print("Received:", plain_text)
    except KeyboardInterrupt:
        print("\nExiting...")
        break

s.close()
