import re
from functools import reduce
from itertools import combinations, count
from operator import xor

import z3

type AocInputT = list[tuple[set[int], list[set[int]], list[int]]]

TEST_INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    aoc_input = []

    for line in aoc_raw_input.splitlines():
        indicators, *buttons, joltages = line.split()
        buttons = [set(map(int, re.findall(r"\d+", button))) for button in buttons]
        indicators = {
            i for i, indicator in enumerate(indicators[1:-1]) if indicator == "#"
        }
        joltages = list(map(int, re.findall(r"\d+", joltages)))

        aoc_input.append((indicators, buttons, joltages))

    return aoc_input


def part1(aoc_input: AocInputT) -> int:
    return sum(
        next(
            k
            for k in count(1)
            for button_combination in combinations(buttons, k)
            if reduce(xor, button_combination) == indicators
        )
        for indicators, buttons, _ in aoc_input
    )


def find_min_steps(buttons: list[set[int]], joltages: list[int]) -> int:
    optimizer = z3.Optimize()

    # To minimize: number of total presses, so we keep track of presses on each button
    button_presses = [z3.Int(f"press_{btn}") for btn in buttons]
    for button_press in button_presses:
        optimizer.add(button_press >= 0)

    for i, joltage in enumerate(joltages):
        pressable_buttons = [
            presses for presses, button in zip(button_presses, buttons) if i in button
        ]
        optimizer.add(sum(pressable_buttons) == joltage)

    optimizer.minimize(sum(button_presses))
    assert optimizer.check() == z3.sat

    model = optimizer.model()
    presses = [model[press_var].as_long() for press_var in button_presses]

    return sum(presses)


def part2(aoc_input: AocInputT) -> int:
    return sum(find_min_steps(buttons, joltages) for _, buttons, joltages in aoc_input)


def main() -> None:
    with open("../inputs/day_10.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
