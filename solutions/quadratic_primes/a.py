def solution(n):
    p = 0

    while p * p - p + 41 < n:
        p += 1

    p -= 1

    return -(2*p - 1), p * p - p + 41 # a, b

if __name__ == '__main__':
    answer = solution(1000)

    print('Answer:', answer, '=>', answer[0] * answer[1])
