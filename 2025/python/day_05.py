type AocInputT = tuple[list[range], list[int]]

TEST_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

is_final = True


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()

    mr = []
    for r in ranges:
        if not mr or mr[-1][1] < r[0]:
            mr.append(r)
        elif r[0] <= mr[-1][1]:
            mr[-1] = (mr[-1][0], max(mr[-1][1], r[1]))
    return mr


def parse_input(aoc_raw_input: str) -> AocInputT:
    ranges, ids = aoc_raw_input.split("\n\n")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges.splitlines()]

    mr = merge_ranges(ranges)

    return [(start, stop) for start, stop in mr], [*map(int, ids.split())]


def bsearch(ranges: list[tuple[int, int]], id_: int) -> bool:
    lo = 0
    hi = len(ranges)

    while lo < hi:
        mid = lo + hi >> 1

        rlo, rhi = ranges[mid]
        if rlo <= id_ <= rhi:
            return True
        elif rlo > id_:
            hi = mid
        else:
            lo = mid + 1
    return False


def part1(aoc_input: AocInputT) -> int:
    merged_ranges, ids = aoc_input
    return sum(bsearch(merged_ranges, id_) for id_ in ids)


def part2(aoc_input: AocInputT) -> int:
    merged_ranges, _ = aoc_input
    return sum(stop - start + 1 for start, stop in merged_ranges)


def main() -> None:
    with open("../inputs/day_05.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
