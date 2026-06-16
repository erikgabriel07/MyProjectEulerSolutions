from math import factorial as f

def permutation(initial, index):
    d = len(initial)
    
    if not 0 <= index < f(d):
        return None

    p, initial_c = [], initial[:]
    while initial_c:
        block, index = divmod(index, f(d - 1))

        p.append(initial_c.pop(block))

        d -= 1

    return ''.join(map(str, p))

def permutations(d):
    initial = [_ for _ in range(1, d + 1)]
    for index in range(f(d)):
        yield permutation(initial, index)

def solve(d):
    total = 0
    stored = set()

    all_permutations = permutations(d)
    for p in all_permutations:
        for i in range(d):
            if i <= 3:
                multiplicand, multiplier = p[:i+1], p[i+1:d-4]

                if multiplicand == '1' or multiplier == '1':
                    continue

                product = int(multiplicand) * int(multiplier)

                compare = p[d-4:]
                if str(product) == compare and not compare in stored:
                    total += int(compare)
                    stored.add(compare)
            else:
                break
    return total

if __name__ == "__main__":
    answer = solve(9)

    print('Answer:', answer)
