def split_lst_k(lst, k, c, l):
    results = dict()
    
    for i in range(len(lst) - k + 1):
        prod = 1
        key_str = ''
        for j in range(i, k + i):
            prod *= int(lst[j])
            key_str += f'{lst[j]}x'
        results[key_str[:-1]] = prod

        if c*k+i < len(lst) + c:
            prod = 1
            key_str = ''
            for j in range(i, c * k + i, c):
                prod *= int(lst[j])
                key_str += f'{lst[j]}x'
            results[key_str[:-1]] = prod

        if l*k+i <= len(lst) + l - k:
            prod = 1
            key_str = ''
            for j in range(i, l * k + i, l + 1):
                prod *= int(lst[j])
                key_str += f'{lst[j]}x'
            results[key_str[:-1]] = prod

            prod = 1
            key_str = ''
            for j in range(k + i - 1, l * k + i - 1, l - 1):
                prod *= int(lst[j])
                key_str += f'{lst[j]}x'
            results[key_str[:-1]] = prod

    return results

def solve():
    with open('grid-20x20.txt', 'r') as f:
        lines = ' '.join([line.strip() for line in f.readlines()]).split(' ')

    r = split_lst_k(lines, 4, 20, 20)

    max_value = max(r.values())

    return max_value

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)
