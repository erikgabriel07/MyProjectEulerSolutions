def longest_collatz_sequence(limit):
    n = limit - 1

    longest = 0
    counter, previous = 0, 0
    while n != 1:
        m = n

        while m != 1:
            if m % 2 == 0:
                m //= 2
            else:
                m = 3*m + 1
            counter += 1

        if counter > previous:
            longest = n
            previous = counter

        counter = 0
        n -= 1

    return longest

if __name__ == '__main__':
    answer = longest_collatz_sequence(1_000_000)

    print('Answer:', answer)

