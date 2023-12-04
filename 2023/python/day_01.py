TEST1: list[
    str
] = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".splitlines()

TEST2: list[
    str
] = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()

is_final: bool = True


DIG_TABLE: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_digits(line: str) -> str:
    return (dig := list(filter(str.isdigit, line)))[0] + dig[-1]


def part1(aoc_input: list[str]) -> int:
    return sum(int(get_digits(line)) for line in aoc_input)


def part2(aoc_input: list[str]) -> int:
    return sum(
        int(
            (
                dig := "".join(
                    line[i] if line[i].isdigit() else digit
                    for i in range(len(line))
                    for digit_str, digit in DIG_TABLE.items()
                    if line[i].isdigit() or line[i:].startswith(digit_str)
                )
            )[0]
            + dig[-1]
        )
        for line in aoc_input
    )


def main() -> None:
    with open("../inputs/day_01.txt") as file:
        aoc_raw_input = file.read().strip().splitlines()
    aoc_input = aoc_raw_input if is_final else TEST1

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
