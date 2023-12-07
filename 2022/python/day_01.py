TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

is_final = True


def parse_input(aoc_raw_input: str) -> list[list[int]]:
    return [
        [*map(int, meal_cals.splitlines())] for meal_cals in aoc_raw_input.split("\n\n")
    ]


def part1(aoc_input: list[list[int]]) -> int:
    return max(map(sum, aoc_input))


def part2(aoc_input: list[list[int]]) -> int:
    return sum(sorted([*map(sum, aoc_input)], reverse=True)[:3])


def main() -> None:
    with open("../inputs/day_01.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
