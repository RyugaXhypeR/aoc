from collections.abc import Generator

type AocInputT = list[tuple[int, int]]

TEST_INPUT = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

is_final = False


def gen_mirrors(lo: int, hi: int) -> Generator[int, None, None]:
    n_lo_digits = len(str(lo))

    if n_lo_digits & 1:
        lo = 10**n_lo_digits
        n_lo_digits += 1

    first_half = int(str(lo)[: n_lo_digits // 2])

    for n in range(first_half, hi):
        n_mirror = int(f"{n}{n}")
        if n_mirror > hi:
            break
        if n_mirror >= lo:
            yield n_mirror


def gen_reps(lo: int, hi: int) -> Generator[int, None, None]:
    slo = str(lo)
    shi = str(hi)

    llo = len(slo)
    lhi = len(shi)

    if llo < lhi:
        yield from gen_reps(lo, 10**llo-1)
        yield from gen_reps(10**llo, hi)

    for i in range(1, llo // 2 + 1):
        for n in range(int(slo[:i]), hi):
            n_rep = int(str(n) * (llo // i))
            if n_rep > hi:
                break
            if n_rep >= lo:
                yield n_rep


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [tuple(map(int, inp.split("-"))) for inp in aoc_raw_input.split(",")]


def part1(aoc_input: AocInputT) -> int:
    return sum(sum(gen_mirrors(lo, hi)) for lo, hi in aoc_input)


def part2(aoc_input: AocInputT) -> int:
    return sum(sum(set(gen_reps(lo, hi))) for lo, hi in aoc_input)


def main() -> None:
    with open("../inputs/day_02.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
