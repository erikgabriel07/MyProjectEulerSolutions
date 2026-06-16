def digit_fifith_power(start, end, exp):
    result = []
    for number in range(start, end + 1):
        total = 0
        for digit in str(number):
            total += int(digit) ** exp
        if total == number:
            result.append(number)
    
    return result

if __name__ == '__main__':
    answer = digit_fifith_power(0, 1_000_000, 5)

    print('Answer:', sum(answer), answer)

