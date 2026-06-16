from is_prime import is_prime, next_prime

def solve(n):
    i = 2

    prime_factors = []
    
    while n != 1:
        while n % i == 0:
            n = n // i
            prime_factors.append(i)
        i = next_prime(i)
    
    return prime_factors

if __name__ == '__main__':
    number = 600_851_475_143
    answer = solve(number)

    print('Number       :', number)
    print('Prime factors:\n', answer)
    print('Largest One  :', answer[-1])
