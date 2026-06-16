def count_divisors(N):
    from is_prime import next_prime

    d = 0
    factors = []
    while N != 1:
        d = next_prime(d)

        while N % d == 0:
            N //= d
            factors.append(d)

    Q = 1
    for f in set(factors):
        Q *= factors.count(f) + 1

    return Q - 1

def hi_divisible_tri(N):
    i = 2
    triangle = 0

    c = 0
    while True:
        triangle = i * (i + 1) // 2

        Q = count_divisors(triangle)

        if c == 2000 or Q >= N:
            print(f'INFO LOG:\nTriangle: {triangle}\nD Qty: {Q}\ni = {i}\n')
            c = 0

        if Q >= N:
            return triangle

        i += 1
        c += 1
 
if __name__ == '__main__':
    answer = hi_divisible_tri(500)

    print('Answer:', answer)

