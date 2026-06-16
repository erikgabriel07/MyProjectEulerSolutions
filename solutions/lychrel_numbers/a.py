def palindrome(n: str):
    return n == n[::-1]

def reverse(n: str):
    return int(n[::-1])

def solve(n):
    m = n
    while m > 0:
        s = m + reverse(str(m))

        for _ in range(50):

            if palindrome(str(s)):
                n -= 1
                break

            s += reverse(str(s))

        m -= 1

    return n

if __name__ == "__main__":
    answer = solve(10_000)

    print('Answer:', answer)

