from math import *
from time import sleep

def solve(n):
    i, j = 0, 0

    primes = []
    numbers = list(range(2, n))

    while i < len(numbers):
        p = numbers[i]

        primes.append(p)

        while j < len(numbers):
            if numbers[j] % p == 0:
                numbers.pop(j)
            j += 1 
        j = 0
    
    return primes

if __name__ == '__main__':
    answer = solve(100)

    print(answer, len(answer))

