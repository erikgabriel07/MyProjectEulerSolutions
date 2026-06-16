def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for m in range(3, int(n**0.5) + 1, 2):
        if n % m == 0 and m != 1:
            return False

    return True

def same_digits(n1: str, n2: str):
    n1 = sorted([d for d in n1])
    n2 = sorted([d for d in n2])

    return n1 == n2

def solve():
    result = set()

    primes = list(filter(is_prime, [n for n in range(1001, 10000, 2)]))

    p_perm = []

    for prime in primes:
        perm = [prime]
        for pri in primes:
            if same_digits(str(prime), str(pri)) and prime != pri:
                perm.append(pri)
        
        if len(perm) != 1:
            p_perm.append(sorted(perm))

    for lst in p_perm:
        for p in range(len(lst)):
            for q in range(p + 1, len(lst)):
                dif = lst[q] - lst[p]

                if lst[p] + 2*dif in lst:
                    result.add(tuple(lst))

    print(list(result)[0])

    answer = ''.join(list(map(str, list(result)[0]))[1:])

    return answer

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)

