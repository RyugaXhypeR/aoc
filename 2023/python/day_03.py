import re
from collections import defaultdict
from functools import reduce

with open("../inputs/day_03.txt") as file:
    IN = file.read().strip().splitlines()

TEST1 = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()

TEST2 = """\
"""

SYMS = [
    (i, j)
    for i, ln in enumerate(IN)
    for j, c in enumerate(ln)
    if not c.isalnum() and c != "."
]

STARS = [(i, j) for i, ln in enumerate(IN)
         for j, c in enumerate(ln) if c == "*"]


def is_adj(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    if abs(x1 - x2) > 1:
        return False
    if abs(y1 - y2) < 2:
        return True
    return False


def part1(inp):
    sm = 0
    for i, ln in enumerate(inp):
        for it in re.finditer(r"\d+", ln):
            adj = False
            for j in range(*it.span()):
                if any(is_adj((i, j), x) for x in SYMS):
                    adj = True
                    break

            if adj:
                sm += int(it.group())
    return sm


def part2(inp):
    d = defaultdict(list)
    for i, ln in enumerate(inp):
        for it in re.finditer(r"\d+", ln):
            adj = False
            for coord in STARS:
                if any(is_adj((i, j), coord) for j in range(*it.span())):
                    adj = True
                    break

            if adj:
                d[coord].append(int(it.group()))

    for v in d.values():
        if len(v) == 2:
            print(v)
    return sum(v[0] * v[1] for v in d.values() if len(v) == 2)


if __name__ == "__main__":
    print(part1(IN))
    print(part2(IN))
