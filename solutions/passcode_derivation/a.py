def sort(digits, attempts):
    for constraint in attempts:
        stop = False
        while not stop:
            previous = None

            for a in constraint:
                if previous:
                    index_1 = digits.index(a)
                    index_2 = digits.index(previous)

                    if index_1 < index_2:
                        digits[index_1], digits[index_2] = previous, a
                    else:
                        stop = True

                previous = a

def solve():
    with open('keylog.txt', 'r') as f:
        attempts = [line.strip() for line in f.readlines()]

    digits = sorted(list(set(''.join(attempts))))

    sort(digits, attempts)
    
    return ''.join(digits)

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)
