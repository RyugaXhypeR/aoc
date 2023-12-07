from collections import Counter
from dataclasses import dataclass
from typing import Self

TEST_INPUT = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

is_final = True


@dataclass()
class CamelCard:
    hand: str
    bid_amount: int

    def __post_init__(self) -> None:
        if len(self.hand) != 5:
            raise ValueError(f"Invalid hand size: expected 5 got {
                             len(self.hand)}")

        self.CARD_PRECEDENCE = "23456789TJQKA"
        self.counter = Counter(self.hand)
        self.precedence = (*map(self.CARD_PRECEDENCE.index, self.hand),)

    def __gt__(self, other: Self) -> bool:
        return (
            self.rank() > other.rank()
            if self.rank() != other.rank()
            else self.precedence > other.precedence
        )

    def rank(self) -> int:
        match sorted(self.counter.items(), key=lambda c: c[1]):
            case ((_, 5),):  # Five of a kind
                return 6
            case ((_, 1), (_, 4)):  # Four of a kind
                return 5
            case ((_, 2), (_, 3)):  # Full house
                return 4
            case ((_, 1), (_, 1), (_, 3)):  # Three of a kind
                return 3
            case ((_, 1), (_, 2), (_, 2)):  # Two pairs
                return 2
            case ((_, 1), (_, 1), (_, 1), (_, 2)):  # One pair
                return 1
            case _:  # High card
                return 0

    def get_precedence(self, card: str, wildcard: bool = False) -> int:
        if wildcard and card == "J":
            return -1
        return self.CARD_PRECEDENCE.index(card)

    def best_replacement_wildcard(self) -> str:
        if "J" not in self.hand:
            return self.hand
        best_replacement, *_rest = sorted(
            self.counter.items(),
            key=lambda c: (c[1], self.get_precedence(c[0], wildcard=True)),
            reverse=True,
        )
        if best_replacement[0] != "J":
            return self.hand.replace("J", best_replacement[0])

        if _rest:
            return self.hand.replace("J", _rest[0][0])
        return self.hand.replace("J", self.CARD_PRECEDENCE[-1])

    @classmethod
    def from_text(cls, text: str) -> Self:
        hand, bid_amount = text.strip().split()
        return cls(hand, int(bid_amount))


def parse_input(aoc_raw_input: str):
    return [*map(CamelCard.from_text, aoc_raw_input.splitlines())]


def part1(aoc_input):
    return sum(card.bid_amount * i for i, card in enumerate(sorted(aoc_input), start=1))


def part2(aoc_input):
    return part1(
        [
            CamelCard(card.best_replacement_wildcard(), card.bid_amount)
            for card in aoc_input
        ]
    )


def main() -> None:
    with open("../inputs/day_07.txt") as file:
        aoc_raw_input = file.read().strip()
    aoc_input = parse_input(aoc_raw_input if is_final else TEST_INPUT)

    print(part1(aoc_input))
    print(part2(aoc_input))


if __name__ == "__main__":
    main()
