from math import isqrt, prod

TEST_INPUT = """\
Time:      7  15   30
Distance:  9  40  200
"""

is_final = True


def clean_input(aoc_input: str) -> list[list[str]]:
    return [line.split(":")[1].split() for line in aoc_input.splitlines()]


def num_winning_runs(time: int, distance: int) -> int:
    # Brute Force::
    #   Slight optimization, iterating over [time // 2, time).
    #   Itertate until the run ((time - i) * i) is less than `distance`,
    #   then multiply by two (because multiplication is commutative) and
    #   add 1 if time is even (~time & 1).
    #
    #   return len(
    #       list(takewhile(lambda i: (time - i) * i >
    #            distance, range(time // 2 + 1, time)))
    #   ) * 2 + (~time & 1)

    # Quadratic formula::
    #
    #   distance > ith * (time - ith)
    #   ith**2 - ith*time + distance = 0
    #
    #   ith = (time [+-] √time**2 - 4*distance) / 2
    _d = isqrt(time**2 - 4 * distance) + 1
    return (time + _d) // 2 - (time - _d) // 2


def part1(aoc_input: list[list[str]]) -> int:
    return prod(
        num_winning_runs(time, distance)
        for time, distance in map(lambda x, y: (int(x), int(y)), *aoc_input)
    )


def part2(aoc_input: list[list[str]]) -> int:
    # Brute force, executes in ~5s
    time, distance = map(int, map("".join, aoc_input))
    return num_winning_runs(time, distance)


def main() -> None:
    with open("../inputs/day_06.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = clean_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
