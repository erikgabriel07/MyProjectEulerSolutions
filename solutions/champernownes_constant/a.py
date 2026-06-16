def solution(N):
    n = ''.join(map(str, list(range(1,N))))

    a = n[0], n[9], n[99], n[999], n[9999], n[99999], n[999999]

    p = 1

    for m in a:
        if m != '0':
            p *= int(m)

    return p

if __name__ == '__main__':
    answer = solution(int(1e6))

    print('Answer:', answer)
