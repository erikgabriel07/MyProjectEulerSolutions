if __name__ == '__main__':
    with open('numbers.txt', 'r') as f:
        numbers = f.readlines()

    numbers = map(int, numbers)
    total = sum(numbers)

    print('Sum:',total)
    print(f'The first ten digits: {str(total)[:10]}')

