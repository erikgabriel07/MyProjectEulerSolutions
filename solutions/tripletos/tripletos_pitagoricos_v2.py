from math import *

def b_F(S, a):
    return (S * (S - 2*a)) / (2 * (S - a))

def c_F(S, a, b):
    return int(S - a - b)

def is_natural(n):
    return n > 0 and float(n) == int(n)

def solve(S):
    a, b, c = 1, 0, 0

    while a + b + c < S and a**2 + b**2 != c**2:
        a += 1
        b = b_F(S, a)
        
        if is_natural(b):
            c = c_F(S, a, b)
        else:
            continue

    return a, int(b), c

if __name__ == '__main__':
    pass

