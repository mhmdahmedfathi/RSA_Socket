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
    (b, _) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n  # we don't want -ve integers
    return b


def Encrypt(m, n, e):
    c = ConvertToStr(PowMod(ConvertToInt(m), e, n))
    return c


def Decrypt(c, n, d):
    m = ConvertToStr(PowMod(ConvertToInt(c), d, n))
    return m
