from itertools import pairwise
from typing import Iterable

TEST_INPUT = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

is_final = True


def parse_input(aoc_raw_input: str) -> list[list[int]]:
    return [[*map(int, line.split())] for line in aoc_raw_input.splitlines()]


def to_zero_and_not_beyond(history: list[int]) -> list[int]:
    return history[-1] + sum(
        (history := [y - x for x, y in pairwise(history)])[-1]
        for _ in iter(lambda: any(history), False)
    )


def part1(aoc_input: Iterable[list[int]]) -> int:
    return sum(map(to_zero_and_not_beyond, aoc_input))


def part2(aoc_input: Iterable[list[int]]) -> int:
    return part1(num[::-1] for num in aoc_input)


def main() -> None:
    with open("../inputs/day_09.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
