def solve(start, end):
    stored = set()

    def powers(n, k):
        for i in range(2, k + 1):
            yield pow(n,i)

    i, c = start, 0
    while i <= end:
        for n in powers(i, end):
            if not n in stored:
                c += 1
                stored.add(n)
        i += 1

    return c

if __name__ == "__main__":
    answer = solve(2, 100)

    print('Answer:', answer)
