# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/11

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    # @answer(1234)

    def get_empty_rows_and_cols(self):
        empty_rows = [r for r, row in enumerate(
            self.input) if all(c == "." for c in row)]

        empty_cols = [c for c, col in enumerate(
            zip(*self.input)) if all(x == "." for x in col)]

        return empty_rows, empty_cols

    def get_distances(self, multiplier):
        empty_rows, empty_cols = self.get_empty_rows_and_cols()

        visited = set()
        galaxies = set()
        distances = []

        for r, row in enumerate(self.input):
            for c, col in enumerate(row):
                if col == "#":
                    galaxies.add((r, c))

        for r1, c1 in galaxies:
            for r2, c2 in galaxies - visited - {(r1, c1)}:
                dist = abs(r1 - r2) + abs(c1 - c2)

                min_c, min_r = min(c1, c2), min(r1, r2)
                max_c, max_r = max(c1, c2), max(r1, r2)

                add_vertically = [c for c in range(
                    min_c + 1, max_c) if c in empty_cols]

                add_horizontally = [r for r in range(
                    min_r + 1, max_r) if r in empty_rows]

                distances.append(dist + len(add_vertically) * multiplier +
                                 len(add_horizontally) * multiplier)

            visited.add((r1, c1))

        return sum(distances)

    @answer(10490062)
    def part_1(self) -> int:
        return self.get_distances(1)

    @answer(382979724122)
    def part_2(self) -> int:
        return self.get_distances(1_000_000-1)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
