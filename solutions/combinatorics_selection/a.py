def f(n):
    r = n
    for a in range(1, n):
        r *= a
    return r

def solution(N):
    values = []

    for n in range(N, 1, -1):
        for m in range(1, n):
            c = f(n) // (f(m) * f(n - m))

            if c > 1e6:
                values.append(c)
    
    return values

if __name__ == '__main__':
    answer = solution(100)

    print('Answer:', len(answer))
