"""
Advent of Code - 2021 - Day 7
Cherry
"""


def day7_part1(input):
    input = [int(i) for i in input.split(',')]
    min_fuel = None
    for i in range(0, max(input)):
        fuel = 0
        for j in input:
            fuel += abs(j - i)
        if min_fuel == None:
            min_fuel = fuel
        else:
            min_fuel = min(fuel, min_fuel)
    return min_fuel


def day7_part2(input):
    input = [int(i) for i in input.split(',')]
    min_fuel = None
    for i in range(0, max(input)):
        fuel = 0
        for j in input:
            fuel += sum([k for k in range(abs(j - i) + 1)])
        if min_fuel == None:
            min_fuel = fuel
        else:
            min_fuel = min(fuel, min_fuel)
    return min_fuel


with open('day7.test.txt') as f:
    input = f.read()
    assert day7_part1(input) == 37
    assert day7_part2(input) == 168
with open('day7.txt') as f:
    input = f.read()
    print(day7_part1(input))
    print(day7_part2(input))
