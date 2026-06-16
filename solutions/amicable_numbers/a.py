def d(n): # função d(n) que retorna a soma dos divisores próprios de n 
    m = n
    s, i = 1, 2

    while n % i == 0:
        n //= 2
        s *= i
    s = s * i - 1
    
    i += 1
    while n != 1:
        c = 0
        while n % i == 0:
            n //= i
            c += 1

        if c != 0:
            s = s * (i ** (c + 1) - 1) // (i - 1)

        i += 2

    return s - m

def solution(n):
    result = []

    while n > 1:
        b = d(n)
        a = d(b)

        if n == a and n != b:
            result.append(a)
        
        n -= 1

    return result

if __name__ == '__main__':
    answer = solution(10_000)

    print('Answer:', sum(answer))
