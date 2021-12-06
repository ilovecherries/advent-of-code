"""
Advent of Code - 2021 - Day 6
Cherry
"""

def day6_part1(input, days=80):
    input = [int(i) for i in input.split(',')]
    iterations = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in input:
        iterations[i] += 1
    for i in range(days):
        x = iterations.pop(0)
        iterations[6] += x
        iterations.append(x)
    return sum(iterations)


with open('day6.test.txt') as file:
    input = file.read()
    assert day6_part1(input) == 5934
    assert day6_part1(input, 256) == 26984457539
with open('day6.txt') as file:
    input = file.read()
    print(day6_part1(input))
    print(day6_part1(input, 256))
