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


def day3_part1(input):
    input = input.split('\n')
    values = scan_input(input)
    gamma = int(''.join([str(x) for x, _ in values]), 2)
    epsilon = int(''.join([str(y) for _, y in values]), 2)
    return gamma * epsilon


def day3_part2(input):
    input = input.split('\n')
    values = [seperate_bits(i) for i in reduce(reduce_input, input, [])]
    # oxygen generator rating and co2 rating
    # oh this filtering
    # so we must do a pass for each value and match it against the input
    # and see if each bit is true
    def oxy_lambda(x): return [i for i, _ in x]
    def co2_lambda(x): return [j for _, j in x]
    oxygen = oxy_lambda(values)
    co2 = co2_lambda(values)
    # so filter out the oxygen first i guess

    def get_rating(bits, get_input):
        inputcopy = input.copy()
        i = 0
        while i < len(bits):
            inputcopy = list(filter(lambda x: int(x[i]) == bits[i], inputcopy))
            if len(inputcopy) == 1:
                break
            bits = get_input(scan_input(inputcopy))
            i += 1
        return int(inputcopy.pop(), 2)
    oxygen_rating = get_rating(oxygen, oxy_lambda)
    co2_rating = get_rating(co2, co2_lambda)
    return oxygen_rating * co2_rating


with open('day3.test.txt') as f:
    input = f.read()
    assert day3_part1(input) == 198
    assert day3_part2(input) == 230
with open('day3.txt') as f:
    input = f.read()
    print(day3_part1(input))
    print(day3_part2(input))
