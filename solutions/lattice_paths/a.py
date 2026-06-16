def solve_1(n):
    initial, target = [1]*n, [_+1 for _ in range(n)]

    steps = []

    m = n
    while True:
        steps.append(initial[:])
        if target in steps:
            break
        if initial[-1] == n:
            p = 1
            while initial[-p] == m:
                p += 1
                m -= 1
            initial[-p] += 1
            while p > 1:
                p -= 1
                initial[-p] = initial[-p-1]
            steps.append(initial[:])
            m = n
        initial[-1] += 1

    return len(steps) * (n + 1)

def solve(n):
    from math import factorial

    return factorial(2*n) // (factorial(n) * factorial(2*n - n))

if __name__ == "__main__":
    answer = solve(20)

    print('Answer:', answer)
