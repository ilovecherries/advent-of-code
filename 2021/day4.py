"""
Advent of Code - 2021 - Day 4
Cherry (ilovecherries@protonmail.com)
"""

from itertools import chain


def transpose(l):
    return list(map(list, zip(*l)))


def parse_board(winning, boards):
    numbers = set()
    for i in winning:
        numbers.add(i)
        for j in boards:
            for k in j:
                if len(list(set(k) & numbers)) == len(k):
                    b = list(chain(*j))
                    b = [x for x in b if x not in list(numbers)]
                    score = sum([int(x) for x in b])
                    return score * int(i)
    return None


def parse_last_winning_board(winning, boards):
    numbers = []
    for i in winning:
        numbers.append(i)
        for x, j in enumerate(boards):
            for b, t in zip(j, transpose(j)):
                if all([l in numbers for l in b]) or all([l in numbers for l in t]):
                    if len(boards) > 1:
                        boards.pop(x)
                        return parse_last_winning_board(winning, boards)
                    b = list(chain(*j))
                    b = [x for x in b if x not in list(numbers)]
                    score = sum([int(x) for x in b])
                    return score * int(i)
    return None


def day4_part1(input):
    input = input.split('\n\n')
    top = input.pop(0)
    winning = [x for x in top.split(',')]
    boards = []
    transposed = []
    for i in input:
        board = [y.split() for y in [z for z in i.split('\n')]]
        boards.append(board)
        transposed.append(transpose(board))
    numbers = set()
    return parse_board(winning, boards) or parse_board(winning, transposed) or None


def day4_part2(input):
    input = input.split('\n\n')
    top = input.pop(0)
    winning = [x for x in top.split(',')]
    boards = []
    transposed = []
    for i in input:
        board = [y.split() for y in [z for z in i.split('\n')]]
        boards.append(board)
        transposed.append(transpose(board))
    numbers = set()
    b = parse_last_winning_board(winning, boards)
    return b


with open('day4.test.txt') as f:
    input = f.read()
    assert day4_part1(input) == 4512
    assert day4_part2(input) == 1924
with open('day4.txt') as f:
    input = f.read()
    print(day4_part1(input))
    print(day4_part2(input))
