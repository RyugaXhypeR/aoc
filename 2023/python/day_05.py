TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()

is_final = True


def clean_input(aoc_input):
    return [
        [
            *map(
                lambda nums: [*map(int, nums.split())],
                line.split(":")[1].strip().splitlines(),
            )
        ]
        for line in aoc_input.split("\n\n")
    ]


def part1(aoc_input):
    (seeds,), *convertors = aoc_input
    locations = []

    for seed in seeds:
        for convertor in convertors:
            for src_start, dst_start, length in convertor:
                if dst_start <= seed < dst_start + length:
                    seed -= dst_start - src_start
                    break
        locations.append(seed)
    return min(locations)


def merge_overlaps(seeds, convertors):
    no_overlaps = []
    while seeds:
        start, stop = seeds.pop()
        for src, dst, length in convertors:
            dst_stop = dst + length
            start_diff = dst - src
            ov_start = max(start, dst)
            ov_stop = min(stop, dst_stop)

            if ov_start >= ov_stop:  # Empty range
                continue

            no_overlaps.append((ov_start - start_diff, ov_stop - start_diff))
            if start < ov_start:
                seeds.append((start, ov_start))
            if stop > ov_stop:
                seeds.append((ov_stop, stop))
            break
        else:
            no_overlaps.append((start, stop))

    seeds[:] = no_overlaps


def part2(aoc_input):
    (seeds,), *convertors = aoc_input
    seeds = [(seeds[i], seeds[i] + seeds[i + 1])
             for i in range(0, len(seeds), 2)]

    for convertor in convertors:
        merge_overlaps(seeds, convertor)
    return min(seeds)[0]


def main() -> None:
    with open("../inputs/day_05.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = clean_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
