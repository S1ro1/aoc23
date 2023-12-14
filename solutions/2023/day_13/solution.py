# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/13

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 13
    separator = "\n\n"

    def get_reflection(self, grid, p2=False):
        for r in range(1, len(grid)):
            top = grid[:r][::-1]
            bottom = grid[r:]

            if not p2:
                top = top[:len(bottom)]
                bottom = bottom[:len(top)]

                if top == bottom:
                    return r
            else:
                if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(top, bottom)) == 1:
                    return r

        return 0

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)

    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
        total = 0
        total2 = 0
        for grid in self.input:
            g = grid.splitlines()
            total += self.get_reflection(g) * 100
            total += self.get_reflection(list(zip(*g)))

            total2 += self.get_reflection(g, True) * 100
            total2 += self.get_reflection(list(zip(*g)), True)

        return total, total2
