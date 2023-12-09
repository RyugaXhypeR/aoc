from functools import reduce

TEST_INPUT = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

is_final = True


def parse_input(aoc_raw_input: str) -> list[list[int]]:
    return [[*map(int, line.split())] for line in aoc_raw_input.splitlines()]


def to_zero_and_not_beyond(history: list[int], pos: int = -1) -> list[int]:
    predicted = history[pos]
    while any(history):
        history = [history[i + 1] - history[i]
                   for i in range(0, len(history) - 1)]
        predicted += history[pos]
    return predicted


def part1(aoc_input):
    return sum(map(to_zero_and_not_beyond, aoc_input))


def part2(aoc_input):
    return part1([num[::-1] for num in aoc_input])


def main() -> None:
    with open("../inputs/day_09.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
