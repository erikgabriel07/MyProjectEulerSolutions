def sum_square_difference(N):
    return (N * (N + 1) // 2) ** 2 - (N * (N + 1) * (2 * N + 1) // 6)
 
if __name__ == '__main__': 
    answer = sum_square_difference(100)

    print('Answer:', answer)

