# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

from ...base import StrSplitSolution, answer
import re
from functools import reduce


class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    # @answer(1234)
    def part_1(self) -> int:
        time, distance = self.input[0].split(
            ":")[1].strip(), self.input[1].split(":")[1].strip()

        times = list(map(int, re.split(r"\s+", time)))
        distances = list(map(int, re.split(r"\s+", distance)))

        num_ways = []
        for time, dist in zip(times, distances):
            valid_times = 0
            for current_speed in range(0, time):
                remaining_time = time - current_speed

                distance_traveled = current_speed * remaining_time
                if distance_traveled > dist:
                    valid_times += 1

            num_ways.append(valid_times)

        return reduce(lambda x, y: x*y, num_ways)

    # @answer(1234)
    def part_2(self) -> int:
        time, distance = self.input[0].split(
            ":")[1].strip(), self.input[1].split(":")[1].strip()

        time = int("".join(time.replace(" ", "")))
        distance = int("".join(distance.replace(" ", "")))

        valid_times = 0
        for current_speed in range(0, time):
            remaining_time = time - current_speed

            distance_traveled = current_speed * remaining_time
            if distance_traveled > distance:
                valid_times += 1

        return valid_times

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
