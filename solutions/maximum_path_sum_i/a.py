def max_path_s(numbers, n_sum=0, pos=0, gap=2, results=None):
    if results is None:
        results = []

    if n_sum == 0:
        n_sum = numbers[0]

    left, right = pos + gap - 1, pos + gap

    if left >= len(numbers):
        return results.append(n_sum)

    max_path_s(numbers, n_sum + numbers[left], left, gap=gap+1, results=results)
    max_path_s(numbers, n_sum + numbers[right], right, gap=gap+1, results=results)

    return max(results)

def solve():
    with open('numbers.txt', 'r') as f:
        numbers = [int(n.replace('\n','')) for n in f.read().split()]

    r = max_path_s(numbers)
    
    return r

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)
