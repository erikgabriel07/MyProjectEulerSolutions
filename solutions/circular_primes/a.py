def prime(N):
    if N < 2:
        return False

    bases = [2,3,5,7,11,13,17,19,23,29,31]

    if N in bases:
        return True

    if N % 2 == 0:
        return False

    s = 0
    d = N - 1

    while d % 2 == 0:
        s += 1
        d //= 2
    
    for a in bases:
        x = pow(a, d, N)

        if x == 1 or x == N - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % N
            if x == N - 1:
                break

        else:
            return False
    return True

def next_prime(N):
    if N < 2:
        return 2

    N += 1

    if N % 2 == 0:
        N += 1

    while not prime(N):
        N += 2

    return N

def solution(N = int(1e6)):
    values = []

    p = next_prime(0)
    while p < N:
        valid = True
        arr = [c for c in str(p)]

        for i in range(len(arr)):
            arr.append(arr[0])
            arr = arr[1:]
            
            if not prime(int(''.join(arr))):
                valid = False
                break

        if valid:
            values.append(p)

        p = next_prime(p)

    return values

if __name__ == '__main__':
    answer = solution()

    print('Answer:', answer, len(answer))
