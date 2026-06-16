def is_pandigital(number):
    return len(set(number)) == len(number)

def constraints_g():
    constraints = [17, 13, 11, 7, 5, 3, 2, 1]
    for c in constraints:
        yield c

def pandigitals(initial, constraints, start):
    initial_c = []

    try:
        c = next(constraints)
    except StopIteration:
        return initial

    if c == 17:
        for n in initial:
            if n % c == 0:
                initial_c.append(n)
        initial = pandigitals(initial_c, constraints, start + 1)
    else:
        for n in initial:
            for i in range(10):
                number = str(i) + str(n)[:-start]
                if int(number) % c == 0 and is_pandigital(number[0] + str(n)):
                    initial_c.append(number[0] + str(n))
        initial = pandigitals(initial_c, constraints, start + 1)
    return initial

def solve():
    constraints = constraints_g()

    pan_lst = pandigitals([_ for _ in range(100,1000)], constraints, 0)

    return sum(map(int, pan_lst))

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)

