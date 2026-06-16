def is_prime(n):
    if n < 4:
        return n == 2 or n == 3

    bases = [2,3,5,7,11,13,17,19,23,29,31]

    if n in bases:
        return True

    s = 0
    d = n - 1

    while d % 2 == 0:
        d //= 2
        s = s + 1

    for a in bases:
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break

        if not x == n - 1:
            return False

    return True

def next_prime(n):
    if n < 2:
        return 2

    n += 1

    if n % 2 == 0:
        n += 1

    while not is_prime(n):
        n += 2

    return n

def summation_of_primes(n):
    p = 0
    total = 0
    
    while True:
        p = next_prime(p)

        if p > n:
            break

        total += p

    return total

if __name__ == '__main__':
    answer = summation_of_primes(2_000_000)

    print('Answer:', answer)

