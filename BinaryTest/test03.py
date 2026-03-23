# BinaryTest/test03.py

# 비트연산 or, xor, not
a = 0b1100
b = 0b1010

# or 연산
print(bin(a|b))

# xor 연산
print(bin(a^b))

# not 연산
print(bin(~a))
print(bin(~a & 0xF))