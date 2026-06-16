from math import *

def sort(array):
    a, b, c = array

    min_v = min(a, min(b, c))
    max_v = max(a, max(b, c))
    mid_v = (a + b + c) - max_v - min_v

    array = [int(min_v), int(mid_v), int(max_v)]

    return array

def tripletos(m, n, S):
    if m <= n:
        raise ValueError(f'm <= n => {m} <= {n}')

    k = S / (2*m*(m + n))

    a = k*(m**2 - n**2)
    b = k*(2*m*n)
    c = k*(m**2 + n**2)

    return sort([a,b,c])

def solve(S):
    m, n = 2, 0

    a, b, c = 0, 0, 0

    while a + b + c < S:
        n = 1
        while m > n:
            a, b, c = tripletos(m,n,S)

            if a + b + c == S:
                break
            n += 1
        m += 1

    return a, b, c

if __name__ == '__main__':
    pass

