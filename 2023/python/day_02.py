from collections import defaultdict
from math import prod

TEST_INPUT: list[
    str
] = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

is_final: bool = True


def clean_input(aoc_input: list[str]) -> list[dict[str, list[int]]]:
    games = []
    for line in aoc_input:
        color_map: dict[str, list[int]] = defaultdict(list)

        for game in line.split(":")[1].split(";"):
            for num_balls, color in map(str.split, game.split(", ")):
                color_map[color].append(int(num_balls))
        games.append(color_map)
    return games


def part1(aoc_input: list[dict[str, list[int]]]) -> int:
    return sum(
        i
        for i, game in enumerate(aoc_input, start=1)
        if all(map((12).__ge__, game["red"]))
        and all(map((13).__ge__, game["green"]))
        and all(map((14).__ge__, game["blue"]))
    )


def part2(aoc_input: list[dict[str, list[int]]]) -> int:
    return sum(prod(map(max, game.values())) for game in aoc_input)


def main() -> None:
    with open("../inputs/day_02.txt") as file:
        aoc_raw_input = file.read().strip().splitlines()

    aoc_input = clean_input(aoc_raw_input if is_final else TEST_INPUT)
    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
