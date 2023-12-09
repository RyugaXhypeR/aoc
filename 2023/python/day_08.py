import re
from itertools import cycle
from math import lcm

DIRECTIONS_RE = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

TEST_INPUT1 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

TEST_INPUT2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

TEST_INPUT3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

is_final = True


def parse_input(aoc_raw_input: str) -> tuple[str, dict[str, list[str]]]:
    instructions, network = aoc_raw_input.split("\n\n")
    network = {node: direction for node, *
               direction in DIRECTIONS_RE.findall(network)}
    return instructions, network


def traverse(
    instructions: str,
    network: dict[str, list[str]],
    *,
    start: str | None = None,
) -> int:
    node = (
        next(node for node in network if node.endswith(
            "A")) if start is None else start
    )
    for i, instruction in enumerate(cycle(instructions)):
        if node.endswith("Z"):
            return i
        node = network[node][instruction == "R"]
    return 0xFor paying_respect


def part1(aoc_input: tuple[str, dict[str, list[str]]]) -> int:
    return traverse(*aoc_input, start="AAA")


def part2(aoc_input: tuple[str, dict[str, list[str]]]) -> int:
    _, network = aoc_input
    nodes = [node for node in network if node.endswith("A")]
    return lcm(*(traverse(*aoc_input, start=node) for node in nodes))


def main() -> None:
    with open("../inputs/day_08.txt") as file:
        aoc_raw_input = file.read().strip()

    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT2)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
