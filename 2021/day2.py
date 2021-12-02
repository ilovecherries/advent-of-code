"""
Advent of Code - Day 2 - 2022
Cherry
"""


def day2_part1(input):
    pos = (0, 0)
    for i in input:
        c, p = i.split(' ')
        p = int(p)
        if c == 'up':
            pos = tuple(map(sum, zip(pos, (0, -p))))
        elif c == 'down':
            pos = tuple(map(sum, zip(pos, (0, p))))
        elif c == 'forward':
            pos = tuple(map(sum, zip(pos, (p, 0))))
    x, y = pos
    return x * y

def day2_part2(input):
    aim = 0
    depth = 0
    x = 0
    for i in input:
        c, p = i.split(' ')
        p = int(p)
        if c == 'up':
            aim -= p
        elif c == 'down':
            aim += p
        elif c == 'forward':
            x += p
            depth += aim * p
    return x * depth


with open('day2.test.txt') as f:
    input = f.readlines()
    assert day2_part1(input) == 150
    assert day2_part2(input) == 900
with open('day2.txt') as f:
    input = f.readlines()
    print(day2_part1(input))
    print(day2_part2(input))
