def smallest_multiple(*integers):
    length = len(integers)

    i, a = 1, integers[0]

    while i < length:
        b = integers[i]

        P = a * b

        while b:
            a %= b
            a, b = b, a

        a = P // a

        i += 1

    return a

if __name__ == '__main__':
    answer = smallest_multiple(*[n for n in range(1,100)])

    print('Answer:', answer)

