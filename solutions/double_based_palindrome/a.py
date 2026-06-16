def check_if_palindrome_in_base_2(palindrome):
    bin_palin = bin(palindrome)[2:]

    if bin_palin == bin_palin[::-1]:
        return True
    return False

def create_palindromes(start, end):
    palindromes = []

    for n in range(start, end):
        if str(n) == str(n)[::-1]:
            palindromes.append(n)

    return palindromes

def double_base_palindrome(start, end):
    result = []

    palindromes = create_palindromes(start, end)

    palindromes = list(filter(check_if_palindrome_in_base_2, palindromes))

    print(palindromes)

    return sum(palindromes)

if __name__ == '__main__':
    answer = double_base_palindrome(0, 1_000_000)

    print('Answer:', answer)
