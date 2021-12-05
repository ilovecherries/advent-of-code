"""
Advent of Code 2021 - Day 5
Cherry
"""


def destructure_coord(i):
    return tuple([int(x) for x in i.split(',')])


def is_horizontal(i): return i[0][0] != i[1][0]


def is_vertical(i): return i[0][1] != i[1][1]


def is_diagonal(i): return (i[0][1] != i[1][1]) and (i[0][0] != i[1][0])


def sort_segment(x):
    index = 1 if is_vertical(x) else 0
    return (x[1], x[0]) if x[0][index] > x[1][index] else x


def generate_points(i):
    if is_diagonal(i):
        xstep = -1 if i[0][0] > i[1][0] else 1
        ystep = -1 if i[0][1] > i[1][1] else 1
        return [(x, y) for x, y in zip(range(i[0][0], i[1][0]+xstep, xstep),
                                       range(i[0][1], i[1][1]+ystep, ystep))]
    i = sort_segment(i)
    if is_horizontal(i):
        return [(x, i[0][1]) for x in range(i[0][0], i[1][0]+1)]
    elif is_vertical(i):
        return [(i[0][0], x) for x in range(i[0][1], i[1][1]+1)]

    return []


# test if generate points works for diagonals correctly
assert generate_points(((9, 7), (7, 9))) == [(9, 7), (8, 8), (7, 9)]


def intersection_points(x, y):
    if x == y:
        return set()
    return set(x) & set(y)


def day5_part1(input, filter_diagonal=True):
    input = input.split('\n')
    input = [tuple([destructure_coord(x[0]),
                    destructure_coord(x[1])])
             for x in [i.split(' -> ') for i in input]]
    # remove diagonal lines
    if filter_diagonal:
        input = [x for x in input if not is_diagonal(x)]
    input = [hash(i)
             for i in sum([generate_points(x) for x in input], [])]
    matches = {}
    for i in input:
        if i not in matches:
            matches[i] = 0
        matches[i] += 1
    result = [i for i, c in matches.items() if c > 1]

    return len(result)


with open('day5.test.txt') as f:
    input = f.read()
    assert day5_part1(input) == 5
    assert day5_part1(input, False) == 12

with open('day5.txt') as f:
    input = f.read()
    print(day5_part1(input))
    print(day5_part1(input, False))
