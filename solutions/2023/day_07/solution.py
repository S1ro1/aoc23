# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from ...base import StrSplitSolution, answer

STRENGTH = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

STRENGTH2 = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}

LETTERS = '23456789TQKA'


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    def _parse(self, input_line: str):
        card, rank = input_line.split(' ')
        return card, int(rank)

    def _rank(self, rank):
        letters = set(rank[0])
        ranking = rank[0]

        value = [0, 0, 0, 0, 0, 0]

        for letter in letters:
            if ranking.count(letter) == 5:
                value[0] = 6
            elif ranking.count(letter) == 4:
                value[0] = 5
            elif ranking.count(letter) == 3:
                for l2 in letters - {letter}:
                    if ranking.count(l2) == 2:
                        value[0] = 4
                        break
                else:
                    if value[0] == 0:
                        value[0] = 3
            elif ranking.count(letter) == 2:
                for l2 in letters - {letter}:
                    if ranking.count(l2) == 2:
                        value[0] = 2
                        break
                else:
                    if value[0] == 0:
                        value[0] = 1

        for index, letter in enumerate(ranking):
            value[index + 1] = STRENGTH[letter]

        return tuple(value)

    def get_hand_value(self, ranking):
        counts = [ranking.count(card) for card in ranking]
        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def all_hands(self, hand):
        if hand == "":
            return [""]
        return [x + y for x in (LETTERS if hand[0] == 'J' else hand[0]) for y in self.all_hands(hand[1:])]

    def _rank22(self, hand):
        return max(map(self.get_hand_value, self.all_hands(hand)))

    def _rank2(self, hand):
        return (self._rank22(hand), [STRENGTH2[x] for x in hand])

    @answer(251287184)
    def part_1(self) -> int:
        m = list(map(self._parse, self.input))
        x = sorted(m, key=self._rank)
        return sum([(i + 1) * x[1] for i, x in enumerate(x)])

    @answer(250757288)
    def part_2(self) -> int:
        m = list(map(self._parse, self.input))
        self.debug(m)

        x = sorted(m, key=lambda hand: self._rank2(hand[0]))

        return sum([(i + 1) * x[1] for i, x in enumerate(x)])


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
