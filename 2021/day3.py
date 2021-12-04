"""
Advent of Code - Day 3 - 2021
Cherry
"""

from functools import reduce


def reduce_input(x, y):
    splited = [int(i) for i in y]
    if x == []:
        x = [{0: 0, 1: 0} for i in y]
    for i, v in enumerate(y):
        x[i][int(v)] += 1
    return x


def seperate_bits(value):
    if value[0] <= value[1]:
        return (1, 0)
    else:
        return (0, 1)


def scan_input(input):
    return [seperate_bits(i) for i in reduce(reduce_input, input, [])]


def oy(x): return [i for i, _ in x]
def c2(x): return [j for _, j in x]


def day3_part1(input):
    input = input.split('\n')
    values = scan_input(input)
    gamma = int(''.join([str(x) for x in oy(values)]), 2)
    epsilon = int(''.join([str(x) for x in c2(values)]), 2)
    return gamma * epsilon


def day3_part2(input):
    input = input.split('\n')
    values = [seperate_bits(i) for i in reduce(reduce_input, input, [])]
    oxygen = oy(values)
    co2 = c2(values)

    def get_rating(bits, get_input):
        def refine(bits, copy, i=0):
            copy = list(filter(lambda x: int(x[i]) == bits[i], copy))
            if len(copy) == 1:
                return int(copy.pop(), 2)
            bits = get_input(scan_input(copy))
            return refine(bits, copy, i+1)
        return refine(bits, input.copy())
    oxygen_rating = get_rating(oxygen, oy)
    co2_rating = get_rating(co2, c2)
    return oxygen_rating * co2_rating


with open('day3.test.txt') as f:
    input = f.read()
    assert day3_part1(input) == 198
    assert day3_part2(input) == 230
with open('day3.txt') as f:
    input = f.read()
    print(day3_part1(input))
    print(day3_part2(input))
