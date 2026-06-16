def tri_pen_hex(start):
    hexagons, pentagons = set(), set()

    h, p = start, start

    while True:
        hexagons.add(h * (2*h - 1))
        pentagons.add(p * (3*p - 1)//2)

        common = hexagons.intersection(pentagons)

        if common:
            return common
        
        h += 1
        p += 1

    return hexagons, pentagons

if __name__ == '__main__':
    answer = tri_pen_hex(144)

    print('Answer:', answer)

