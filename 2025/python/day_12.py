import math

import numpy as np
from numpy.typing import ArrayLike

type AocInputT = tuple[dict[int, ArrayLike], tuple[tuple[int, int], tuple[int, ...]]]

TEST_INPUT = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


def parse_input(aoc_raw_input: str) -> AocInputT:
    *raw_shapes, raw_regions = aoc_raw_input.split("\n\n")

    shapes = {}

    for raw_shape in raw_shapes:
        index, raw_shape = raw_shape.split(":")

        shapes[int(index)] = np.array(
            [[int(col == "#") for col in row] for row in raw_shape.split()]
        )

    regions = []
    for raw_region in raw_regions.splitlines():
        raw_region_dims, raw_shape_frequencies = raw_region.split(": ")
        regions.append(
            (
                tuple(map(int, raw_region_dims.split("x"))),
                tuple(map(int, raw_shape_frequencies.split())),
            )
        )

    return shapes, regions


def generate_shape_combinations(shape: ArrayLike, dims: tuple[int, int]):
    x, y = dims
    p, q = shape.shape

    for i in range(x - p + 1):
        for j in range(y - q + 1):
            grid = np.zeros(dims, np.uint8)
            grid[i : i + p, j : j + q] = shape
            yield grid


def rotate_shape(shape: ArrayLike):
    for _ in range(4):
        yield (shape := np.rot90(shape))


def do_shapes_fit(
    shapes: dict[int, ArrayLike], dims: tuple[int, int], frequencies: tuple[int, ...]
) -> bool:
    to_fit = [shapes[i] for i, f in enumerate(frequencies) for _ in range(f)]

    # TODO: make this work somehow (for both cases)
    #
    # x, y = dims
    #
    # def _fit_them(region: ArrayLike, i):
    #     cprint(region)
    #     if i >= len(to_fit):
    #         return True
    #
    #     shape = to_fit[i]
    #     for shape in rotate_shape(shape):
    #         for broad_shape in generate_shape_combinations(shape, dims):
    #             if np.any(broad_shape & region):
    #                 continue
    #
    #             if _fit_them(broad_shape | region, i + 1):
    #                 return True
    #
    #     return False
    #
    # return _fit_them(np.zeros(dims, np.uint8), 0)

    return np.sum(to_fit) <= math.prod(dims)  # bruhh


def part1(aoc_input: AocInputT) -> int:
    shapes, region_info = aoc_input
    return sum(do_shapes_fit(shapes, *r) for r in region_info)


def main() -> None:
    is_final = True

    with open("../inputs/day_12.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))


if __name__ == "__main__":
    main()
