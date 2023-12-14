# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer
from copy import deepcopy


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14

    def get_grid_and_rocks(self):
        grid = list(map(list, self.input))

        round_rocks = set()

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "O":
                    round_rocks.add((r, c))

        return grid, round_rocks

    def get_grid_total(self, grid):
        total = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "O":
                    total += len(grid[0]) - r

        return total

    @answer(108918)
    def part_1(self) -> int:
        grid, round_rocks = self.get_grid_and_rocks()

        while 1:
            rocks_moved = 0
            new_rocks = set()
            for r, c in sorted(round_rocks, key=lambda x: x[0]):
                if r == 0:
                    continue

                if grid[r - 1][c] not in "O#":
                    grid[r - 1][c] = "O"
                    grid[r][c] = "."
                    new_rocks.add((r - 1, c))
                    rocks_moved += 1

            round_rocks.clear()
            round_rocks.update(new_rocks)
            if rocks_moved == 0:
                break

        return self.get_grid_total(grid)

    @answer(100310)
    def part_2(self) -> int:
        grid, rocks = self.get_grid_and_rocks()

        visited_configs = {}
        visited_configs[tuple(rocks)] = 0
        new_grid = deepcopy(grid)
        cycle_counter = 0
        total_cycle_length = 1_000_000_000

        while total_cycle_length > 0:
            for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                while 1:
                    rocks_moved = 0
                    new_rocks = set()
                    for r, c in rocks:
                        new_position = (r + direction[0], c + direction[1])

                        if new_position[0] < 0 or new_position[0] > len(grid) - 1 or new_position[1] < 0 or new_position[1] > len(grid[0]) - 1:
                            new_rocks.add((r, c))
                            continue

                        if grid[new_position[0]][new_position[1]] not in "O#":
                            new_grid[new_position[0]][new_position[1]] = "O"
                            new_grid[r][c] = "."
                            new_rocks.add((new_position[0], new_position[1]))
                            rocks_moved += 1
                        else:
                            new_rocks.add((r, c))

                    rocks.clear()
                    rocks.update(new_rocks)
                    grid = deepcopy(new_grid)
                    if rocks_moved == 0:
                        break

            cycle_counter += 1
            if tuple(rocks) in visited_configs:
                total_cycle_length = cycle_counter - \
                    visited_configs[tuple(rocks)]
                total_cycle_length = (
                    1_000_000_000 - cycle_counter) % total_cycle_length
            else:
                visited_configs[tuple(rocks)] = cycle_counter

        return self.get_grid_total(grid)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
