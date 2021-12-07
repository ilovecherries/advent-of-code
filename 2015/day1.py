"""
Advent of Code 2015 - Day 1
Cherry (ilovecherries@protonmail.com)
"""

from typing import Counter


def day1_part1(input):
    input = {i: c for i, c in Counter(input).items()}
    return input['('] - input[')']


def day1_part2(input):
    p = 0
    for i, j in enumerate(input):
        p += 1 if j == '(' else -1
        if p == -1:
            return i + 1
    return None


assert(day1_part1('(())')) == 0
assert(day1_part2('()())')) == 5

with open('day1.txt') as f:
    input = f.read()
    print(day1_part1(input))
    print(day1_part2(input))
