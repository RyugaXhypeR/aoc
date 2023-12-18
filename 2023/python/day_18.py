DIR_TO_POS_MAP = dict(zip("UDLR", (-1j, 1j, -1, 1)))

type AocInputT = list[str]

TEST_INPUT = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [
        (
            DIR_TO_POS_MAP[direction],
            int(step),
            int(color[2:-2], 16),
            DIR_TO_POS_MAP["RDLU"[int(color[-2])]],
        )
        for direction, step, color in map(str.split, aoc_raw_input.splitlines())
    ]


def shoelace(points: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return abs(
        sum(
            coord1.real * coord2.imag - coord1.imag * coord2.real
            for coord1, coord2 in zip(points, points[1:] + points[:1])
        )
        // 2
    )


def part1(aoc_input: AocInputT) -> int:
    coords = 0j
    points = [
        coords := coords + step * direction_factor
        for direction_factor, step, *_ in aoc_input
    ]

    num_walls = sum(step for _, step, *_ in aoc_input)
    return int(shoelace(points) + num_walls // 2 + 1)


def part2(aoc_input: AocInputT) -> int:
    coords = 0j
    points = [
        coords := coords + step * direction_factor
        for *_, step, direction_factor in aoc_input
    ]

    num_walls = sum(step for *_, step, _ in aoc_input)
    return int(shoelace(points) + num_walls // 2 + 1)


def main() -> None:
    with open("../inputs/day_18.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
