def prime(N):
    if N < 2:
        return False

    bases = [2,3,5,7,11,13,17,19,23,29,31]

    if N in bases:
        return True

    if N % 2 == 0:
        return False

    s = 0
    d = N - 1

    while d % 2 == 0:
        s += 1
        d //= 2

    for a in bases:
        x = pow(a, d, N)

        if x == 1 or x == N - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % N
            if x == N - 1:
                break
        else:
            return False

    return True

def next_prime(N):
    if N < 2:
        return 2

    N += 1

    if N % 2 == 0:
        N += 1

    while not prime(N):
        N += 2

    return N

def solution(N):
    primes = []

    n = next_prime(N)
    while len(primes) != 11:
        truncatable = True

        while '0' in str(n):
            n = next_prime(n)

        n_str = str(n)

        for i in range(len(n_str)):
            left = n_str[i:]
            right = n_str[:-i] if i > 0 else n_str[:]

            if not prime(int(left)):
                truncatable = False
                break
            if not prime(int(right)):
                truncatable = False
                break

        if truncatable:
            primes.append(n)

        n = next_prime(n)

    return primes

if __name__ == '__main__':
    answer = solution(7)

    print('Answer:', answer, sum(answer))
