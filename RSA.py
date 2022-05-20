# -*- coding: utf-8 -*-

import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]




def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod


def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n  # we don't want -ve integers
    return b


def Encrypt(m, n, e):
    c = ConvertToStr(PowMod(ConvertToInt(m), e, n))
    return c


def Decrypt(c, p, q, e):
    d = InvertModulo(e, (p - 1) * (q - 1))
    m = ConvertToStr(PowMod(ConvertToInt(c), d, p * q))
    return m




def DecipherSimple(c, n, e, potential_messages):
    decipheredtext = ''
    for msg in potential_messages:
        if c == Encrypt(msg, n, e):
            return msg
    return decipheredtext

def DecipherSmallPrime(c, n, e):
    p = 0
    q = 0
    for p in range(2, n):
        q = n // p
        if p * q == n:
            break
    decipheredtext = Decrypt(c, p, q, e)
    return decipheredtext


def DecipherSmallDiff(c, n, e):
    N = int(n ** 0.5)
    p = 0
    q = 0
    for p in range(N - 5000, N + 1):
        q = n // p
        if p * q == n:
            break
    decipheredtext = Decrypt(c, p, q, e)
    return decipheredtext

def DecipherCommonDivisor(c1, n1, e1, c2, n2, e2):
    p = GCD(n1, n2)
    firstdecipheredtext = Decrypt(c1, p, n1 // p, e1)
    seconddecipheredtext = Decrypt(c2, p, n2 // p, e2)
    return firstdecipheredtext, seconddecipheredtext


def DecipherHastad(c1, n1, c2, n2, e):
    N1 = n1 * InvertModulo(n1, n2)
    N2 = n2 * InvertModulo(n2, n1)
    c = (ConvertToInt(c1) * N2 + ConvertToInt(c2) * N1) % (n1 * n2)
    broadcastmessage = ConvertToStr(round(c ** (1/e)))
    return broadcastmessage
