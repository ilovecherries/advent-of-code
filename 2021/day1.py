"""
Advent of Code - Day 1 - 2021
Cherry
"""

from itertools import tee


def day1_part1(input):
    n, n2 = tee(iter(input))
    next(n2, None)
    larger = 0
    for i, j in zip(n, n2):
        if j > i:
            larger += 1
    return larger


def day1_part2(input):
    n, n2, n3 = tee(iter(input), 3)
    next(n2, None)
    next(n3, None)
    next(n3, None)
    larger = 0
    old_sum = None
    for i, j, k in zip(n, n2, n3):
        sum = i + j + k
        if not (old_sum == None or sum <= old_sum):
            larger += 1
        old_sum = sum
    return larger


with open('day1_part1_test.txt') as f:
    input = [int(x) for x in f.readlines()]
    assert day1_part1(input) == 7
    assert day1_part2(input) == 5
with open('day1.txt') as f:
    input = [int(x) for x in f.readlines()]
    print(day1_part1(input))
    print(day1_part2(input))
