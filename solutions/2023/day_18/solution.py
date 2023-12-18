# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/18

from ...base import StrSplitSolution, answer


dir_mapping = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

hex_dir_mapping = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}


class Solution(StrSplitSolution):
    _year = 2023
    _day = 18

    def shoelace(self, points):
        A = sum(points[i][0] * (points[i - 1][1] - points[(i + 1) %
                len(points)][1]) for i in range(len(points)))

        return int(abs(A) / 2)
    
    def picks(self, A, np):
        return A - np//2 + 1

    @answer(53300)
    def part_1(self) -> int:
        curr = (0, 0)
        trench = []
        trench.append(curr)
        total_points = 0
        for row in self.input:
            d, l, _ = row.split()
            total_points += int(l)
            dr, dc = dir_mapping[d][0] * int(l), dir_mapping[d][1] * int(l)
            curr = (curr[0] + dr, curr[1] + dc)
            trench.append(curr)

        a = self.shoelace(list(trench))
        interior = self.picks(a, total_points)
        return interior + total_points

    @answer(64294334780659)
    def part_2(self) -> int:
        curr = (0, 0)
        trench = []
        trench.append(curr)
        total_points = 0
        for row in self.input:
            _, _, hex = row.split()

            hex = hex[2:-1]

            d = int(hex[-1])
            l = int(hex[:-1], 16)

            total_points += int(l)
            dr, dc = hex_dir_mapping[d][0] * int(l), hex_dir_mapping[d][1] * int(l)
            curr = (curr[0] + dr, curr[1] + dc)
            trench.append(curr)

        a = self.shoelace(list(trench))
        interior = self.picks(a, total_points)
        return interior + total_points

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
