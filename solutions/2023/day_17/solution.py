# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/17

from ...base import StrSplitSolution, answer
from heapq import heappop, heappush


class Solution(StrSplitSolution):
    _year = 2023
    _day = 17

    def _parse(self):
        return [list(map(int, line)) for line in self.input]

    @answer(956)
    def part_1(self) -> int:
        g = self._parse()

        # cost, r, c, dr, dc, num_steps
        q = [(0, 0, 0, 0, 0, 0)]

        seen = set()

        least_loss = 0

        while q:
            cost, r, c, dr, dc, num_steps = heappop(q)

            if r == len(g) - 1 and c == len(g[0]) - 1:
                least_loss = cost
                break

            if (r, c, dr, dc, num_steps) in seen:
                continue

            seen.add((r, c, dr, dc, num_steps))

            if num_steps < 3 and (dr, dc) != (0, 0):
                nr, nc = r + dr, c + dc
                if not (r < 0 or c < 0 or nr >= len(g) or nc >= len(g[0])):
                    heappush(q, (cost + g[nr][nc], nr,
                             nc, dr, dc, num_steps + 1))

            for ddr, ddc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ddr, ddc) == (-dr, -dc) or (ddr, ddc) == (dr, dc):
                    continue
                nr, nc = r + ddr, c + ddc
                if not (r < 0 or c < 0 or nr >= len(g) or nc >= len(g[0])):
                    heappush(q, (cost + g[nr][nc], nr, nc, ddr, ddc, 1))

        return least_loss

    @answer(1106)
    def part_2(self) -> int:
        g = self._parse()

        # cost, r, c, dr, dc, num_steps
        q = [(0, 0, 0, 0, 0, 0)]

        seen = set()

        least_loss = 0

        while q:
            cost, r, c, dr, dc, num_steps = heappop(q)

            if r == len(g) - 1 and c == len(g[0]) - 1 and num_steps >= 4:
                least_loss = cost
                break

            if (r, c, dr, dc, num_steps) in seen:
                continue

            seen.add((r, c, dr, dc, num_steps))

            if num_steps < 10 and (dr, dc) != (0, 0):
                nr, nc = r + dr, c + dc
                if not (r < 0 or c < 0 or nr >= len(g) or nc >= len(g[0])):
                    heappush(q, (cost + g[nr][nc], nr,
                             nc, dr, dc, num_steps + 1))

            if num_steps >= 4 or (dr, dc) == (0, 0):
                for ddr, ddc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ddr, ddc) == (-dr, -dc) or (ddr, ddc) == (dr, dc):
                        continue
                    nr, nc = r + ddr, c + ddc
                    if not (r < 0 or c < 0 or nr >= len(g) or nc >= len(g[0])):
                        heappush(q, (cost + g[nr][nc], nr, nc, ddr, ddc, 1))

        return least_loss

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
