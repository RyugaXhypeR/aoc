from collections.abc import Generator
from functools import reduce

type AocInputT = list[list[str]]

TEST_INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

is_final = True


def get_eight_neighbors(grid: list[list[str]], i: int, j: int) -> Generator[str]:
    for x, y in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ):
        if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
            yield grid[x + i][y + j]


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [list(line) for line in aoc_raw_input.splitlines()]


def part1(aoc_input: AocInputT) -> int:
    m, n = len(aoc_input), len(aoc_input[0])
    return sum(
        1
        for i in range(m)
        for j in range(n)
        if aoc_input[i][j] == "@"
        and list(get_eight_neighbors(aoc_input, i, j)).count("@") < 4
    )


def part2(aoc_input: AocInputT) -> int:
    m, n = len(aoc_input), len(aoc_input[0])
    n_removed = 0

    while True:
        to_remove = [
            (i, j)
            for i in range(m)
            for j in range(n)
            if aoc_input[i][j] == "@"
            and list(get_eight_neighbors(aoc_input, i, j)).count("@") < 4
        ]

        n_removed += len(to_remove)
        if not to_remove:
            break

        for i, j in to_remove:
            aoc_input[i][j] = "x"

    return n_removed


def main() -> None:
    with open("../inputs/day_04.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
