from math import *

def is_natural(n):
    return n > 0 and float(n) == int(n)

def find_square(g_value, l_value):
    return sqrt(pow(g_value, 2) - pow(l_value, 2))

def solve(target):
    elements = []

    i, j, n = 2, 0, 0

    while i + j + n < target:
        j = 1
        while i > j:
            n = find_square(i, j)

            if is_natural(n):
                if i + j + n == target:
                    elements.append([i, j, int(n)])
                    break
            j += 1
        i += 1
    return sorted(elements[0])

    

if __name__ == '__main__':
    pass

