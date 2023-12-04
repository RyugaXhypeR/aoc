import re

DIGITS_RE = re.compile(r"(\d++)(?!:)\s*")

TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

is_final = True


def clean_input(aoc_input):
    return [
        len(
            {*DIGITS_RE.findall((parts := lines.split("|"))[0])}
            & {*DIGITS_RE.findall(parts[1])}
        )
        for lines in aoc_input.splitlines()
    ]


def part1(aoc_input):
    return sum(1 << num_matches >> 1 for num_matches in aoc_input)


def part2(aoc_input):
    factors = dict.fromkeys(range(len(aoc_input)), 1)
    for i, num_matches in enumerate(aoc_input):
        for j in range(num_matches):
            factors[i + j] += factors[i - 1]

    return sum(factors.values())


def main() -> None:
    with open("../inputs/day_04.txt") as file:
        aoc_input = file.read().strip()

    aoc_input = clean_input(aoc_input) if is_final else clean_input(TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
