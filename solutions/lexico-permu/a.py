# MINHA SOLUÇÃO:
#
# def solve(initial: str | list[int | str], index: int) -> list[int | str] | None:
#     from math import perm
#
#     copy = initial[:]
#     if not 1 <= index <= perm(len(copy)):
#         return
#
#     p = []
#     while copy:
#         gap = perm(len(copy) - 1)
#
#         element_index = (index - 1) // gap
#
#         index = index - gap * element_index
#
#         p.append(copy.pop(element_index))
#
#     return p

# IMPLEMENTAÇÃO COM FACTORADIC (base fatorial)

def solve(initial: str | list[int | str], length: int, index: int) -> list[int | str] | None:
    from math import factorial as f

    if not 0 <= index <= f(length):
        return

    answer = []
    while initial:
        block, index = divmod(index, f(length - 1))

        answer.append(initial.pop(block))

        length = len(initial)
    
    return answer

if __name__ == '__main__':
    n = [x for x in range(0,10)]

    r = solve(n[:], len(n), 999_999)

    print('Answer:', ''.join([str(x) for x in r]))

