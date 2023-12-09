# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/9

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    def parse(self):
        return [list(map(int, line.split())) for line in self.input]

    def calculate_differences(self, num_list):
        lists = []
        while 1:
            new_list = []
            for i in range(len(num_list) - 1):
                new_list.append(num_list[i + 1] - num_list[i])

            num_list = new_list
            lists.append(num_list)
            if len(set(num_list)) == 1:
                break

        return lists

    @answer(1637452029)
    def part_1(self) -> int:
        nums = self.parse()

        values = []

        for num in nums:
            tree = self.calculate_differences(num)
            stack = [0]
            for level in tree[::-1]:
                stack.append(stack[-1] + level[-1])

            result = num[-1] + stack[-1]
            values.append(result)

        return sum(values)

    @answer(908)
    def part_2(self) -> int:
        nums = self.parse()

        values = []

        for num in nums:
            tree = self.calculate_differences(num)
            stack = [0]
            for level in tree[::-1]:
                stack.append(level[0] - stack[-1])

            result = num[0] - stack[-1]
            values.append(result)

        return sum(values)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
