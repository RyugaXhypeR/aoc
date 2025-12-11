import math
from functools import cache
from itertools import pairwise, permutations, starmap

type AocInputT = dict[str, list[str]]

TEST_INPUT1 = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

TEST_INPUT2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return {
        source: dest.split()
        for source, dest in (line.split(":") for line in aoc_raw_input.splitlines())
    }


def part1(aoc_input: AocInputT) -> int:
    @cache
    def _num_paths(source: str, dest: str) -> int:
        return source == dest or sum(
            _num_paths(node, dest) for node in aoc_input.get(source, [])
        )

    return _num_paths("you", "out")


def part2(aoc_input: AocInputT) -> int:
    @cache
    def _num_paths(source, dest):
        return source == dest or sum(
            _num_paths(node, dest) for node in aoc_input.get(source, [])
        )

    def _path_contains(source: str, dest: str, *intermediary: str) -> int:
        return sum(
            math.prod(starmap(_num_paths, pairwise([source, *inter, dest])))
            for inter in permutations(intermediary)
        )

    return _path_contains("svr", "out", "fft", "dac")


def main() -> None:
    with open("../inputs/day_11.txt") as file:
        aoc_raw_input = file.read().strip()

    print(part1(parse_input(aoc_raw_input if is_final else TEST_INPUT1)))
    print(part2(parse_input(aoc_raw_input if is_final else TEST_INPUT2)))


if __name__ == "__main__":
    main()
