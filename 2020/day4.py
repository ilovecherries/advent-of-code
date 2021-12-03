"""
Advent of Code - 2020 - Day 4
Cherry (ilovecherries@protonmail.com)
"""

import re

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional = 'cdi'


def valid_keys(keys):
    try:
        keys.remove(optional)
    except ValueError:
        pass
    intersection = list(set(keys) & set(required))
    return len(intersection) == len(required)


def day4_part1(input):
    valid = 0
    input = input.split('\n\n')
    for passport in input:
        pairs = passport.split()
        keys = [key for key, _ in [pair.split(':') for pair in pairs]]
        if valid_keys(keys):
            valid += 1
    return valid


# this is used for 'hgt'
measurements = {
    'cm': lambda x: 150 <= x <= 192,
    'in': lambda x: 59 <= x <= 76
}

colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: measurements[x[-2:]](int(x[:-2])),
    'hcl': lambda x: re.match(r'#[0-9a-f]{6}', x) is not None,
    'ecl': lambda x: x in colors,
    'pid': lambda x: re.match(r'[0-9]{9}', x) is not None
}


def day4_part2(input):
    valid = 0
    input = input.split('\n\n')
    for passport in input:
        pairs = passport.split()
        keys, values = list(zip(*[pair.split(':') for pair in pairs]))
        keys = list(keys)
        values = list(values)
        if not valid_keys(keys):
            continue

        def run_validator(k, v):
            if k not in validators:
                return True
            try:
                return validators[k](v)
            except:
                return False
        if all([run_validator(k, v) for k, v in zip(keys, values)]):
            valid += 1
    return valid


if __name__ == '__main__':
    with open('day4.test.txt') as f:
        input = f.read()
        assert day4_part1(input) == 2
    with open('day4.test.invalid.txt') as f:
        input = f.read()
        assert day4_part2(input) == 0
    with open('day4.test.valid.txt') as f:
        input = f.read()
        assert day4_part2(input) == 4
    with open('day4.txt') as f:
        input = f.read()
        print(day4_part1(input))
        print(day4_part2(input))
