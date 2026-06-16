def sort_names(names_lst, start=0, end=None):
    end = end if end is not None else len(names_lst)

    def partition_lst(names_lst_n, start_n, end_n):
        pivot = names_lst_n[end_n - 1]

        for i in range(start_n, end_n):
            if names_lst_n[i] <= pivot:
                names_lst_n[i], names_lst_n[start_n] = names_lst_n[start_n], names_lst_n[i]
                start_n += 1

        return start_n - 1

    if start < end:
        partition = partition_lst(names_lst, start, end)
        sort_names(names_lst, start, partition)
        sort_names(names_lst, partition + 1, end)

    return names_lst

def names_scores(names):
    keys = [chr(a) for a in range(65, 91)]
    values = [a for a in range(1, 27)]

    c_values = dict(zip(keys, values))

    total_scores = 0

    for position, name in enumerate(names):
        total = 0
        for char in name:
            total += c_values[char]
        total_scores += total * (position + 1)

    return total_scores

if __name__ == '__main__':
    with open('names.txt', 'r') as f:
        names = [name.replace('"', '') for name in f.read().split(',')]

    names = sort_names(names)

    answer = names_scores(names)

    print('Answer:', answer)

