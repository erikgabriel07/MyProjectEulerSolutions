from math import factorial as f

def permutation(initial, ind):
    d = len(initial)

    if not 0 <= ind < f(d):
        return initial

    p = []
    while initial:
        block, ind = divmod(ind, f(d - 1))
        p.append(initial.pop(block))
        d -= 1
    return p

def permutations(d):
    initial = [f'{_}' for _ in range(d, 0, -1)]
    for i in range(f(d)):
        yield ''.join(permutation(initial[:],i))

def solve():
    perm = []
    for p in permutations(9):
        perm.append(p)
        if p == '918273645':
            break
    
    for p in perm:
        if int(p[:4]) * 2 == int(p[4:]):
            return p

if __name__ == "__main__":
    answer = solve()

    print('Answer:', answer)
