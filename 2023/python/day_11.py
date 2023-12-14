TEST_INPUT = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

EXPANDED = """\
....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
"""

is_final = True


def real_position_galaxies(
    galaxies: list[list[str]], expansion_rate: int
) -> list[tuple[int, int]]:
    rows_with_no_galaxies = [
        i for i, row in enumerate(galaxies) if not row.count("#")
    ]
    cols_with_no_galaxies = [
        i for i, col in enumerate(zip(*galaxies)) if not col.count("#")
    ]

    expansion_rate -= 1
    return [
        (
            x + expansion_rate * sum(x > row for row in rows_with_no_galaxies),
            y + expansion_rate * sum(y > col for col in cols_with_no_galaxies),
        )
        for x, row in enumerate(galaxies)
        for y, space in enumerate(row)
        if space == "#"
    ]


def parse_input(aoc_raw_input: str):
    return [*map(list, aoc_raw_input.splitlines())]


def make_pairs(galaxies: list[tuple[int, int]]):
    return {tuple(sorted((g1, g2))) for g1 in galaxies for g2 in galaxies if g1 != g2}


def shortest_path(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    x1, y1 = galaxy1
    x2, y2 = galaxy2

    return abs(x2 - x1) + abs(y2 - y1)


def part1(aoc_input) -> int:
    galaxies = real_position_galaxies(aoc_input, 2)
    pairs = make_pairs(galaxies)
    return sum(shortest_path(*pair) for pair in pairs)


def part2(aoc_input) -> int:
    galaxies = real_position_galaxies(aoc_input, 1000000)
    pairs = make_pairs(galaxies)
    return sum(shortest_path(*pair) for pair in pairs)


def main() -> None:
    with open("../inputs/day_11.txt") as file:
        aoc_raw_input = file.read().strip()

    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
