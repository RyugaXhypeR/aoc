with open("inputs/day_01.txt") as file:
    IN = file.read().strip().splitlines()

TEST1 = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".splitlines()

TEST2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()


UNIQUE_TABLE = {
    "o": ("one",),
    "t": ("two", "three"),
    "f": ("four", "five"),
    "s": ("six", "seven"),
    "e": ("eight",),
    "n": ("nine",),
}

DIG_TABLE = {
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


def part1(inp):
    return sum(int((x := [c for c in ln if c.isdigit()])[0] + x[-1]) for ln in inp)


def part2(inp):
    sums = 0
    for ln in inp:
        i = 0
        sbuf = ""
        while i < len(ln):
            if ln[i].isdigit():
                sbuf += ln[i]
                i += 1
                continue
            for d in UNIQUE_TABLE.get(ln[i], []):
                if ln[i: i + len(d)] == d:
                    sbuf += DIG_TABLE[d]
                    i += len(d) - 1
                    break
            else:
                i += 1
        sums += int(sbuf[0] + sbuf[-1])
    return sums


if __name__ == "__main__":
    print(part1(IN))
    print(part2(IN))
