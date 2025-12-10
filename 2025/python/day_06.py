from functools import reduce
from operator import add, mul

type AocInputT = list[str]

TEST_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return aoc_raw_input.splitlines()


def part1(aoc_input: AocInputT) -> int:
    rows = zip(
        *(
            (int(num) if num.isnumeric() else num for num in line.split())
            for line in aoc_input
        )
    )

    return sum(
        reduce({"+": add, "*": mul}[operator], operands) for *operands, operator in rows
    )


def part2(aoc_input: AocInputT) -> int:
    operators = aoc_input[-1].split()
    cols = zip(*aoc_input[:-1])

    operands = [[]]
    for c in cols:
        if s := "".join(c).strip():
            n = int(s)
            operands[-1].append(n)
        else:
            operands.append([])

    return sum(
        reduce({"+": add, "*": mul}[operator], operands)
        for operands, operator in zip(operands, operators)
    )


def main() -> None:
    with open("../inputs/day_06.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
