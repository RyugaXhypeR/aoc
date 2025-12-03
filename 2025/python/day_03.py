from functools import reduce

type AocInputT = list[list[int]]

TEST_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

is_final = True


def find_max_n_digit_int(nums: list[int], n: int) -> int:
    n_removeable_digits = len(nums) - n
    stack = []

    for num in nums:
        while n_removeable_digits > 0 and stack and stack[-1] < num:
            stack.pop()
            n_removeable_digits -= 1
        stack.append(num)

    return reduce(lambda x, y: x * 10 + y, stack[:n])


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [[*map(int, line)] for line in aoc_raw_input.splitlines()]


def part1(aoc_input: AocInputT) -> int:
    return sum(find_max_n_digit_int(bank, 2) for bank in aoc_input)


def part2(aoc_input: AocInputT) -> int:
    return sum(find_max_n_digit_int(bank, 12) for bank in aoc_input)


def main() -> None:
    with open("../inputs/day_03.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
