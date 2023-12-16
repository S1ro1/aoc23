# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/16

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2023
    _day = 16

    def calculate_energizement(self, start: tuple) -> int:
        visited = set()

        beam = [start]
        q = deque(beam)

        while q:
            r, c, dr, dc = q.popleft()

            r += dr
            c += dc

            if r < 0 or c < 0 or r >= len(self.input) or c >= len(self.input[0]):
                continue

            mirror = self.input[r][c]

            if mirror == '.' or (dr != 0 and mirror == '|') or (dc != 0 and mirror == '-'):
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            elif mirror == '/':
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            elif mirror == '\\':
                dr, dc = dc, dr
                if (r, c, dr, dr) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

            elif mirror == '|':
                if (r, c, -1, 0) not in visited:
                    visited.add((r, c, -1, 0))
                    q.append((r, c, -1, 0))

                if (r, c, 1, 0) not in visited:
                    visited.add((r, c, 1, 0))
                    q.append((r, c, 1, 0))

            elif mirror == '-':
                if (r, c, 0, -1) not in visited:
                    visited.add((r, c, 0, -1))
                    q.append((r, c, 0, -1))

                if (r, c, 0, 1) not in visited:
                    visited.add((r, c, 0, 1))
                    q.append((r, c, 0, 1))

        coords = set()
        for r, c, dr, dc in visited:
            coords.add((r, c))

        return len(coords)

    @answer(7860)
    def part_1(self) -> int:
        return self.calculate_energizement((0, -1, 0, 1))

    @answer(8331)
    def part_2(self) -> int:
        lengths = []
        width = len(self.input[0])
        height = len(self.input)
        for y in range(width):
            lengths.append(self.calculate_energizement((-1, y, 1, 0)))
            lengths.append(self.calculate_energizement((height, y, -1, 0)))
        
        for x in range(height):
            lengths.append(self.calculate_energizement((x, -1, 0, 1)))
            lengths.append(self.calculate_energizement((x, width, 0, -1)))
        
        return max(lengths)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
