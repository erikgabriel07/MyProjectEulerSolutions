from math import *

def comb_r(pool, r):
    n = len(pool)
    if n == 0 and r > 0:
        return
    
    indices = [0] * r
    
    while True:
        yield tuple(pool[i] for i in indices)
        
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        
        indices[i:] = [indices[i] + 1] * (r - i)

def fs(n):
    if isinstance(n, int):
        n = str(n)

    s = 0
    for d in n:
        s += int(d) ** 2
    return s

def count_p(n):
    s = factorial(len(n))

    c = 1
    for i in range(10):
        c *= factorial(n.count(f'{i}'))

    return s // c

def solve(d):
    c = 0
    for number in comb_r('0123456789',d):
        m = fs(''.join(number))

        while m != 1 and m != 0:
            m = fs(m)

            if m == 89:
                c += count_p(number)
                break

    return c

if __name__ == "__main__":
    answer = solve(7)

    print('Answer:', answer)
