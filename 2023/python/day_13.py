from typing import Callable, Iterable

type AocInputT = list[list[str]]


TEST_INPUT = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

is_final = False


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [*map(str.splitlines, aoc_raw_input.split("\n\n"))]


def get_num_mis_matches[str](iterable1: Iterable[str], iterable2: Iterable[str]) -> int:
    return sum(x != y for sub1, sub2 in zip(iterable1, iterable2) for x, y in zip(sub1, sub2))


def find_perfect_reflective_point(
    grid: list[str], pred: Callable[(int, int), bool]
) -> int:
    len_grid = len(grid)

    for i in range(1, len_grid):
        top_half, bottom_half = grid[:i][::-1], grid[i:]
        min_len = min(len(top_half), len(bottom_half))
        top_half, bottom_half = top_half[:min_len], bottom_half[:min_len]

        if pred(top_half, bottom_half):
            return i * 100

    # Should not go into infinite recursion
    return find_perfect_reflective_point(list(zip(*grid)), pred) // 100


def part1(aoc_input: AocInputT) -> int:
    return sum(
        find_perfect_reflective_point(grid, lambda x, y: x == y) for grid in aoc_input
    )


def part2(aoc_input) -> int:
    return sum(
        find_perfect_reflective_point(grid, lambda x, y: get_num_mis_matches(x, y) == 1)
        for grid in aoc_input
    )


def main() -> None:
    with open("../inputs/day_13.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
