def compare(n1, n2):
    lst_1 = [digit for digit in str(n1)]
    lst_2 = [digit for digit in str(n2)]

    lst_1.sort()
    lst_2.sort()

    return lst_1 == lst_2

def permuted_multiples(x):
    r = compare(143, 143*2)

    i = 2
    n = 100
    number = None
    while not number:
        if compare(n, n*i):
            if i == x:
                number = n
            i += 1
        else:
            i = 2
            n += 1

    return number

if __name__ == '__main__':
    answer = permuted_multiples(6)

    print('Answer:', answer)

