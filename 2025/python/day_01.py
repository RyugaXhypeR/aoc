from itertools import accumulate

type AocInputT = list[int]

TEST_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [_clean(inp) for inp in aoc_raw_input.splitlines()]


def _clean(n: str):
    return (-1 if n[0] == "L" else 1) * int(n[1:])


def part1(aoc_input: AocInputT) -> int:
    return sum(
        not x
        for x in accumulate(aoc_input, lambda x, n: (x + n) % 100, initial=50)
    )


def part2(aoc_input: AocInputT) -> int:
    start = 50
    result = 0

    for num in aoc_input:
        was_zero = start == 0
        r, start = divmod(start + num, 100)
        result += abs(r)
        if num < 0:
            result += (start == 0) - (was_zero)

    return result


def main() -> None:
    with open("../inputs/day_01.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
