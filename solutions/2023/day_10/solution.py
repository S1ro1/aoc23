# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/10

from ...base import StrSplitSolution, answer

from collections import deque


# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10**6)


class Solution(StrSplitSolution):
    _year = 2023
    _day = 10

    def flood(self, grid, start):
        r, c = start
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != ".":
            return

        grid[r][c] = "!"

        self.flood(grid, (r - 1, c))
        self.flood(grid, (r + 1, c))
        self.flood(grid, (r, c - 1))
        self.flood(grid, (r, c + 1))

    def get_loop(self):
        for r, row in enumerate(self.input):
            for c, col in enumerate(row):
                if col == "S":
                    start = (r, c)
                    break
            else:
                continue
            break

        queue = deque([start])
        visited = {start}

        while queue:
            curr_r, curr_c = queue.popleft()
            curr_char = self.input[curr_r][curr_c]

            if curr_r > 0 and curr_char in "SJL|" and self.input[curr_r - 1][curr_c] in "7F|" and (curr_r - 1, curr_c) not in visited:
                queue.append((curr_r - 1, curr_c))
                visited.add((curr_r - 1, curr_c))

            if curr_r < len(self.input) - 1 and curr_char in "S7F|" and self.input[curr_r + 1][curr_c] in "JL|" and (curr_r + 1, curr_c) not in visited:
                queue.append((curr_r + 1, curr_c))
                visited.add((curr_r + 1, curr_c))

            if curr_c > 0 and curr_char in "SJ7-" and self.input[curr_r][curr_c - 1] in "LF-" and (curr_r, curr_c - 1) not in visited:
                queue.append((curr_r, curr_c - 1))
                visited.add((curr_r, curr_c - 1))

            if curr_c < len(self.input[0]) - 1 and curr_char in "SLF-" and self.input[curr_r][curr_c + 1] in "J7-" and (curr_r, curr_c + 1) not in visited:
                queue.append((curr_r, curr_c + 1))
                visited.add((curr_r, curr_c + 1))

        return visited

    @answer(7173)
    def part_1(self) -> int:
        visited = self.get_loop()

        return len(visited) // 2

    @answer(291)
    def part_2(self) -> int:
        visited = self.get_loop()

        new_grid = []
        for r, row in enumerate(self.input):
            new_row = []
            for c, col in enumerate(row):
                if (r, c) in visited:
                    new_row.append(col)
                else:
                    new_row.append(".")
            new_grid.append(new_row)

        upsampled = []
        for _ in range(len(new_grid) * 3):
            upsampled_row = []
            for _ in range(len(new_grid[0]) * 3):
                upsampled_row.append(".")

            upsampled.append(upsampled_row)

        for r, row in enumerate(new_grid):
            for c, col in enumerate(row):
                if col == ".":
                    continue

                if col == "F":
                    chars = [[".", ".", "."], [".", "F", "-"], [".", "|", "."]]

                if col == "7":
                    chars = [[".", ".", "."], ["-", "7", "."], [".", "|", "."]]

                if col == "L":
                    chars = [[".", "|", "."], [".", "L", "-"], [".", ".", "."]]

                if col == "J":
                    chars = [[".", "|", "."], ["-", "J", "."], [".", ".", "."]]

                if col == "|":
                    chars = [[".", "|", "."], [".", "|", "."], [".", "|", "."]]

                if col == "-":
                    chars = [[".", ".", "."], ["-", "-", "-"], [".", ".", "."]]

                if col == "S":
                    chars = [[".", ".", "."], [".", "S", "."], [".", ".", "."]]
                    if r > 0 and new_grid[r-1][c] in "7F|":
                        chars[0][1] = "|"

                    if r < len(new_grid) - 1 and new_grid[r+1][c] in "JL|":
                        chars[2][1] = "|"

                    if c > 0 and new_grid[r][c-1] in "LF-":
                        chars[1][0] = "-"

                    if c < len(new_grid[0]) - 1 and new_grid[r][c+1] in "J7-":
                        chars[1][2] = "-"

                for ri, rc in enumerate(chars):
                    for ci, cc in enumerate(rc):
                        upsampled[r * 3 + ri][c * 3 + ci] = cc

        self.flood(upsampled, (0, 0))

        total = 0
        for r in range(0, len(upsampled), 3):
            for c in range(0, len(upsampled[0]), 3):
                if upsampled[r + 1][c + 1] == ".":
                    total += 1

        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
