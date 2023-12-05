# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import StrSplitSolution, answer
import re


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(21919)
    def part_1(self) -> int:

        g_total = 0
        for line in self.input:
            game_data = line.split(': ')[1]
            my_nums, winning_nums = game_data.split(' | ')

            total = 0

            for num in map(int, re.split(r'\s+', my_nums.strip())):
                if num in map(int, re.split(r'\s+', winning_nums.strip())):
                    total += 1

            if total > 0:
                g_total += 2 ** (total - 1)

        return g_total

    # @answer(1234)
    def part_2(self) -> int:
        from collections import defaultdict
        winning_cards = defaultdict(lambda: 1)

        for i, line in enumerate(self.input, start=1):
            game_data = line.split(': ')[1]
            my_nums, winning_nums = game_data.split(' | ')

            total = 0

            for num in map(int, re.split(r'\s+', my_nums.strip())):
                if num in map(int, re.split(r'\s+', winning_nums.strip())):
                    total += 1

            if total > 0:
                for j in range(1, total + 1):
                    winning_cards[i + j] += winning_cards[i] * 1

            self.debug(winning_cards[i])

        return sum(winning_cards.values())

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
