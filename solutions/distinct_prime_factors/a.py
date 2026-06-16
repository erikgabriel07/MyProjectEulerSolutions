def linear_sieve(n):
    lp = [0] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)

        for p in primes:
            if p > lp[i] or i * p > n:
                break

            lp[i * p] = p

    return primes, lp

def distinct_prime_factors(n, spf):
    c = 0
    l = 0

    while n > 1:
        p = spf[n]

        if p != l:
            c += 1
            l = p

        n //= p

    return c

def solve(target):
    ls = linear_sieve(int(1e6))[1]

    n = 0
    c = target
    while c > 0:
        n += 1
        if distinct_prime_factors(n, ls) == target:
            c -= 1
            continue
        c = target

    return n - target + 1

if __name__ == "__main__":
    answer = solve(4)

    print('Answer:', answer)
