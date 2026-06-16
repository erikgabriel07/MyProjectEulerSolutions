from math import isqrt

def is_triangle(n):
    x = 8*n + 1
    s = isqrt(x)
    return s*s == x

def coded_triangle_numbers(words):
    char_values = dict(zip([chr(a) for a in range(65, 91)], [a for a in range(1,27)]))

    result = []
    for word in words:
        s = 0
        for c in word:
            s += char_values[c]
        if is_triangle(s):
            result.append(word)

    return len(result)

if __name__ == '__main__':
    with open('words.txt', 'r') as f:
        words = [s.replace('"', '').strip() for s in f.readlines()[0].split(',')]

    answer = coded_triangle_numbers(words)

    print('Answer:', answer)

