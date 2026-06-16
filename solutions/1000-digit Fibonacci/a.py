def fibonacci(n):
    n1 = 1
    n2 = 1
    n3 = n1 + n2

    i = 2

    if n == 1:
        return n1
    if n == 2:
        return n2

    terms = [n1, n2]
    while True:
        n1 = n2
        n2 = n3
        terms.append(n3)
        n3 = n1 + n2
        i += 1

        if len(str(n3)) == n:
            return i + 1

if __name__ == '__main__':
    s = fibonacci(1000)

    print(s)

