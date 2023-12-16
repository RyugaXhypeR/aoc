from collections import defaultdict
from functools import reduce

TEST_INPUT = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

is_final = True


def parse_input(aoc_raw_input: str):
    return aoc_raw_input.split(",")


def hash_string(string: str) -> int:
    return reduce(lambda x, y: (x + ord(y)) * 17, string, 0) % 256


def get_boxes(aoc_input: list[str]) -> list[list[tuple[str, int]]]:
    boxes = [{} for _ in range(256)]
    for string in aoc_input:
        label = string[: string.find("=")]
        hashed_value = hash_string(label)

        if "-" in string:
            if label in boxes[hashed_value]:
                boxes[hashed_value].pop(label)
        else:
            focal_length = int(string[-1])
            boxes[hashed_value][label] = focal_length

    return boxes


def part1(aoc_input) -> int:
    return sum(map(hash_string, aoc_input))


def part2(aoc_input) -> int:
    boxes = get_boxes(aoc_input)
    return sum(
        box_num * slot * focal_length
        for box_num, box in enumerate(boxes, start=1)
        for slot, (_, focal_length) in enumerate(box.items(), start=1)
    )


def main() -> None:
    with open("../inputs/day_15.txt") as file:
        aoc_raw_input = file.read().strip()

    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
