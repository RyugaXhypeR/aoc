from collections import defaultdict

type AocInputT = list[list[str]]

TEST_INPUT = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

is_final = True


def parse_input(aoc_raw_input: str) -> AocInputT:
    return list(map(list, aoc_raw_input.splitlines()))


def part1(aoc_input: AocInputT) -> int:
    M, N = len(aoc_input), len(aoc_input[0])
    sx, sy = next((x, y) for x in range(M) for y in range(N) if aoc_input[x][y] == "S")
    seen = {*()}

    for x, y in (beams := [(sx, sy)]):
        if x + 1 >= M or (x + 1, y) in seen:
            continue

        if aoc_input[x + 1][y] == "^":
            seen.add((x + 1, y))
            if y - 1 >= 0:
                beams.append((x + 1, y - 1))
            if y + 1 < N:
                beams.append((x + 1, y + 1))
        else:
            beams.append((x + 1, y))

    return len(seen)


def part2(aoc_input: AocInputT) -> int:
    M, N = len(aoc_input), len(aoc_input[0])
    sx, sy = next((x, y) for x in range(M) for y in range(N) if aoc_input[x][y] == "S")

    paths = [[0] * N for _ in range(M)]
    paths[sx][sy] = 1

    for x in range(M - 1):
        for y in range(N):
            if aoc_input[x + 1][y] == "^":
                if y - 1 >= 0:
                    paths[x + 1][y - 1] += paths[x][y]
                if y + 1 < N:
                    paths[x + 1][y + 1] += paths[x][y]
            else:
                paths[x + 1][y] += paths[x][y]
    return sum(paths[-1])


def main() -> None:
    with open("../inputs/day_07.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
