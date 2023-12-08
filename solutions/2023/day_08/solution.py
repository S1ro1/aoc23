# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

import math
from ...base import TextSolution, answer

idx_mapping = {
    'L': 0,
    'R': 1,
}


def lcm_of_list(numbers):
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)

    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)

    return lcm_result


class Solution(TextSolution):
    _year = 2023
    _day = 8

    def parse(self):
        instructions, rest = self.input.split("\n\n")

        places = rest.split("\n")
        map = {}
        for place in places:
            start, x = place.split(" = (")
            l, r = x[:-1].split(", ")
            map[start] = (l, r)

        return instructions, map

    @answer(20659)
    def part_1(self) -> int:
        instructions, map = self.parse()

        current_place = 'AAA'
        i = 0
        total = 0
        while current_place != 'ZZZ':
            current_place = map[current_place][idx_mapping[instructions[i]]]
            i = (i + 1) % len(instructions)
            total += 1

        return total

    @answer(15690466351717)
    def part_2(self) -> int:
        instructions, map = self.parse()

        lengths = []

        for key in map.keys():
            if key[2] != 'A':
                continue

            current_place = key

            i = 0
            total = 0
            while current_place[2] != 'Z':
                current_place = map[current_place][idx_mapping[instructions[i]]]
                i = (i + 1) % len(instructions)
                total += 1

            lengths.append(total)

        return lcm_of_list(lengths)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
