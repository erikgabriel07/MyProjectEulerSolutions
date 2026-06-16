def self_power(n):
    total = 0

    k = 0
    while k < n:
        total += (n - k) ** (n - k)
        k += 1

    return total

if __name__ == '__main__':
    answer = self_power(1000)

    print('Result:', answer, '\n')

    answer = str(answer)

    print('Answer:', answer[len(answer) - 10:])

