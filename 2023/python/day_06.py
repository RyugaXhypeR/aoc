from math import prod

TEST_INPUT = """\
Time:      7  15   30
Distance:  9  40  200
"""

is_final = True


def clean_input(aoc_input: str) -> list[list[str]]:
    return [line.split(":")[1].split() for line in aoc_input.splitlines()]


def part1(aoc_input: list[list[str]]) -> int:
    return prod(
        sum((time - i) * i > distance for i in range(time + 1))
        for time, distance in map(lambda x, y: (int(x), int(y)), *aoc_input)
    )


def part2(aoc_input: list[list[str]]) -> int:
    # Brute force, executes in ~5s
    time, distance = map(int, map("".join, aoc_input))
    return sum((time - i) * i > distance for i in range(time + 1))


def main() -> None:
    with open("../inputs/day_06.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = clean_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
