from cmath import isnan
from Crypto.Util import number
from math import log2
from RSA import *
import socket
import sympy

n_length = 16
s = socket.socket()
s.connect(('127.0.0.1', 12345))


def Auto_key_generation():
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

    return e, d, n, p, q


def Manual_key_generation(string):
    p, q, e = (string.replace(" ", "").split(","))

    p = int(p)
    q = int(q)
    e = int(e)

    phi_n = (p - 1) * (q - 1)

    if (isnan(p) or isnan(q) or not(sympy.isprime(p)) or not(sympy.isprime(q)) or (GCD(phi_n, e) != 1) or e >= phi_n or e <= 1 or p == q or p == 1 or q == 1):
        print("Invalid inputs")
        return 1, 1, 1, 1, 1

    n = p * q
    d = InvertModulo(e, phi_n)

    return e, d, n, p, q


def decrypt(cipher_text, n, d):
    decrypt = ""
    str_plain = ""

    for x in range(0, len(cipher_text), 2):
        decrypt = Decrypt(cipher_text[x:x+2], n, d)
        str_plain += decrypt

    plain_text = str_plain

    return plain_text

# start sending
e = d = n = q = p = 1

while p == 1:
    Auto_Or_Manual = int(input("Do you want key generation to be (1) automatic or (2) manual?\n"))
    if Auto_Or_Manual == 1:
        e, d, n, p, q = Auto_key_generation()
    elif Auto_Or_Manual == 2:
        e, d, n, p, q = Manual_key_generation(input("Please enter p, q, e separated by comma:\n"))

s.send(ConvertToStr(n).encode())
s.send(ConvertToStr(e).encode())


while True:
    try:
        cipher = s.recv(1024)
        plain_text = decrypt(cipher.decode('utf-8', 'ignore'), n, d)
        print("Received:", plain_text)
    except KeyboardInterrupt:
        break

s.close()