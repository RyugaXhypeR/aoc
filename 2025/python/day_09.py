from itertools import combinations

from shapely import Polygon

type AocInputT = list[tuple[int, int]]

TEST_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

is_final = True


def area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x, y = p1
    p, q = p2
    return (abs(x - p) + 1) * (abs(y - q) + 1)


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [tuple(map(int, line.split(","))) for line in aoc_raw_input.splitlines()]


def part1(aoc_input: AocInputT) -> int:
    return max(area(p1, p2) for p1, p2 in combinations(aoc_input, 2))


def part2(aoc_input: AocInputT) -> int:
    polygon = Polygon(aoc_input)
    return max(
        area(p1, p2)
        for p1, p2 in combinations(aoc_input, 2)
        if polygon.covers(Polygon([p1, (p2[0], p1[1]), p2, (p1[0], p2[1])]))
    )


def main() -> None:
    with open("../inputs/day_09.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
