from itertools import combinations
import heapq
import math


type AocInputT = list[tuple[int, int, int]]

TEST_INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return [tuple(map(int, line.split(","))) for line in aoc_raw_input.splitlines()]


def part1(aoc_input: AocInputT) -> int:
    short_distances = []

    n = 1000 if is_final else 10

    for x, y in combinations(aoc_input, 2):
        d = math.dist(x, y)
        heapq.heappush(short_distances, (d, x, y))

    circuits = []

    for _ in range(n):
        d, x, y = heapq.heappop(short_distances)
        
        xi = next((i for i, c in enumerate(circuits) if x in c), None)
        yi = next((i for i, c in enumerate(circuits) if y in c), None)

        if xi is None and yi is None:
            circuits.append({x, y})
        elif xi is None:
            circuits[yi].add(x)
        elif yi is None:
            circuits[xi].add(y)
        else:
            circuits[xi] |= circuits[yi]
            if xi != yi:
                circuits.pop(yi)


    top_three = heapq.nlargest(3, map(len, circuits))
    return math.prod(top_three)


def part2(aoc_input: AocInputT) -> int:
    short_distances = []

    for x, y in combinations(aoc_input, 2):
        d = math.dist(x, y)
        heapq.heappush(short_distances, (d, x, y))

    circuits = []

    while short_distances:
        d, x, y = heapq.heappop(short_distances)
        
        xi = next((i for i, c in enumerate(circuits) if x in c), None)
        yi = next((i for i, c in enumerate(circuits) if y in c), None)

        if xi is None and yi is None:
            circuits.append({x, y})
        elif xi is None:
            last = (x, y) # bruhhh
            circuits[yi].add(x)
        elif yi is None:
            circuits[xi].add(y)
        else:
            circuits[xi] |= circuits[yi]
            if xi != yi:
                circuits.pop(yi)

    return last[0][0] * last[1][0]


def main() -> None:
    with open("../inputs/day_08.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
