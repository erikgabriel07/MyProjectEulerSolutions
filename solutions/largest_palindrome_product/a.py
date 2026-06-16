def largest_palindrome_product(digits = 3):
    m, n = 0, 0
    largest = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            if str(i * j) == str(i * j)[::-1]:
                print(i, 'x', j, '=', i*j)

                if i*j > largest:
                    largest = i*j
                    m, n = i, j

    return largest, m, n

if __name__ == '__main__':
    answer = largest_palindrome_product()

    print('Answer:', answer)

