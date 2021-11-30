def day1_part1(input):
    numbers = [int(x) for x in input.strip()]
    numbers.append(numbers[0])
    n1, n2 = iter(numbers), iter(numbers[1:])
    sum = 0
    for i, j in zip(n1, n2):
        if i == j:
            sum += i
    return sum


def day1_part2(input):
    numbers = [int(x) for x in input.strip()]
    l = len(numbers) // 2
    halfway = numbers[l:] + numbers[:l]
    n1, n2 = iter(numbers), iter(halfway)
    sum = 0
    for i, j in zip(n1, n2):
        if i == j:
            sum += i
    return sum


if __name__ == '__main__':
    assert day1_part1('1122') == 3
    assert day1_part1('1111') == 4
    assert day1_part1('1234') == 0
    assert day1_part1('91212129') == 9
    assert day1_part2('1212') == 6
    assert day1_part2('1221') == 0
    assert day1_part2('123425') == 4
    assert day1_part2('123123') == 12
    assert day1_part2('12131415') == 4
    print("test cases all work!")
    with open('day1.txt') as f:
        input = f.read()
        print("part 1:", day1_part1(input))
        print("part 2:", day1_part2(input))
