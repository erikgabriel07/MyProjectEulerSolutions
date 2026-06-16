def get_abc(N, target):
    values = set()
    for c in range(3, N + 1):
        temp_c = c*c
        for a in range(1, c):
            if a*a > temp_c:
                break

            b = (temp_c - a*a)**0.5

            if b.is_integer():
                b = int(b)
                if b > a:
                    a, b = b, a
                if a + b + c == target:
                    values.add((a,b,c))
    return list(values)

def solution(N):
    value = 0
    maximised = 0
    for n in range(1, N + 1):
        res = get_abc(n,n)

        if res:
            print(n, res)

        if len(res) > maximised:
            maximised = len(res)
            value = n
    return value, maximised

if __name__ == '__main__':
    answer = solution(1000)

    print('\nAnswer:', answer)
