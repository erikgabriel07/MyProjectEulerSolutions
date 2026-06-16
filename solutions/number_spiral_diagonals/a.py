def number_spiral_diagonals(limit):
    jump = 2
    steps = 0
    count = 0
    total_sum = 0

    for n in range(1,limit + 1):
        if count == 4:
            jump += 2
            count = 0
        if steps == jump:
            steps = 0
            count += 1
            total_sum += n
        steps += 1

    return total_sum + 1

if __name__ == '__main__':
    answer = number_spiral_diagonals(int(pow(1001,2)))

    print('Answer:', answer)

