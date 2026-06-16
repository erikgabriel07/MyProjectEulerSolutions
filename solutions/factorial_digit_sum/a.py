def factorial(n = 1) -> int:
    result = 1
    for i in range(1, n):
        result *= i
    return result

def solve(n):
    f = str(factorial(n))

    total_sum = 0

    for i in f:
        total_sum += int(i)

    return total_sum

if __name__ == '__main__':
    answer = solve(100)

    print('Answer:', answer)
