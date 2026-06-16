from math import factorial as f

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1 if i == 2 else 2
    return True

def factoradic(initial, d, index):
    if not 0 <= index < f(d):
        return

    number = []
    while initial:
        block, index = divmod(index, f(d - 1))

        number.append(initial.pop(block))

        d = len(initial)
    return int(''.join(map(str, number)))

def solve(n):
    digits = [_ for _ in range(1,n+1)]
    while n > 1:
        while n * (n + 1) // 2 % 3 == 0:
            n -= 1
            digits.pop()

        for i in range(f(n)):
            number = factoradic(digits[::-1], n, i)
            if is_prime(number):
                return number
        n -= 1

if __name__ == "__main__":
    answer = solve(9)

    print('Answer:', answer)
