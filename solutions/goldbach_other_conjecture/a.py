def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for a in range(3, int(n**0.5) + 1, 2):
        if n % a == 0:
            return False
    return True

def solve():
    p, c = 0, 3
    while p >= 0:
        m = 0
        while is_prime(c):
            c += 2

        while (not is_prime(p) or c != p + 2*m*m) and p > -1:
            m += 1; p = 2 * (c//2 - m*m) + 1

        c += 2

    return c - 2

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)
