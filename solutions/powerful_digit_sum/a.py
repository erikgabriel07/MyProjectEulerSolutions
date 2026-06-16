def solution():
    maximum, previous = 0, 0

    for i in range(1, 100):
        for j in range(1, 100):
            a = i**j

            previous = 0
            for s in str(a):
                previous += int(s)

            if maximum < previous:
                maximum = previous

    return maximum

if __name__ == '__main__':
    answer = solution()

    print('Answer:', answer)
