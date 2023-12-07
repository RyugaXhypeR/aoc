TEST_INPUT = """\
A Y
B X
C Z
"""
is_final = True

OPPONENT_MOVES: str = "ABC"
PLAYER_MOVES: str = "XYZ"
WINNING_MAP: dict[str, str] = dict(zip("ABC", "YZX"))
LOSING_MAP: dict[str, str] = dict(zip("ABC", "ZXY"))


def get_round_points(opponent: str, player: str) -> int:
    move_point = PLAYER_MOVES.index(player) + 1
    if OPPONENT_MOVES.index(opponent) == PLAYER_MOVES.index(player):
        return 3 + move_point
    return [0, 6][WINNING_MAP[opponent] == player] + move_point


def get_round_points_predicted(opponent: str, player: str) -> int:
    return get_round_points(
        opponent,
        WINNING_MAP[opponent]
        if player == "Z"
        else LOSING_MAP[opponent]
        if player == "X"
        else PLAYER_MOVES[OPPONENT_MOVES.index(opponent)],
    )


def parse_input(aoc_raw_input: str) -> list[list[str]]:
    return [round.split() for round in aoc_raw_input.splitlines()]


def part1(aoc_input) -> int:
    return sum(get_round_points(opponent, player) for opponent, player in aoc_input)


def part2(aoc_input) -> int:
    return sum(
        get_round_points_predicted(opponent, player) for opponent, player in aoc_input
    )


def main() -> None:
    with open("../inputs/day_02.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
