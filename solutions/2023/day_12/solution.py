# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/12

from functools import lru_cache
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 12

    def part_1(self) -> int:
        total = 0
        self.memo = {}
        for row in self.input:
            puzzle, constraints = row.strip().split(' ')
            constraints = list(map(int, constraints.split(',')))
            total += self.f(puzzle, constraints)

        return total

    def f(self, r, c):
        if (r, tuple(c)) in self.memo:
            return self.memo[(r, tuple(c))]

        curr = 0
        groups = []
        last_dot = 0

        for i in range(len(r)):
            if r[i] == ".":
                if curr != 0:
                    groups.append(curr)
                    if groups != c[:len(groups)]:
                        self.memo[(r, tuple(c))] = 0
                        return 0
                    curr = 0
                last_dot = i

            elif r[i] == "#":
                curr += 1
            else:
                t1 = self.f(r[last_dot:i] + "#" + r[i+1:], c[len(groups):])
                t2 = self.f(r[last_dot:i] + "." + r[i+1:], c[len(groups):])
                self.memo[(r, tuple(c))] = t1 + t2
                return t1 + t2

        if curr != 0:
            groups.append(curr)

        if groups == c:
            self.memo[r, tuple(c)] = 1
            return 1
        else:
            self.memo[(r, tuple(c))] = 0
            return 0

    def part_2(self) -> int:
        total = 0
        self.memo = {}
        for row in self.input:
            puzzle, constraints = row.strip().split(' ')
            constraints = list(map(int, constraints.split(',')))
            puzzle = "?".join([puzzle for _ in range(5)])
            constrains = constraints * 5

            total += self.f(puzzle, constrains)

        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
