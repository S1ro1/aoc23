# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer

_directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
               (1, 1), (1, -1), (-1, -1), (-1, 1)]


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(539590)
    def part_1(self) -> int:

        nums = []
        validNum = False

        for line_index, line in enumerate(self.input):
            if validNum:
                nums.append(int(curr_num))
            validNum = False
            curr_num = ''
            for char_index, char in enumerate(line):

                if char.isdigit():
                    curr_num += char
                    inNum = True
                else:
                    if validNum:
                        nums.append(int(curr_num))
                    curr_num = ''
                    inNum = False
                    validNum = False
                    continue

                if inNum:
                    for direction in _directions:
                        try:
                            new_line_idx = direction[0] + line_index
                            new_char_idx = direction[1] + char_index

                            if not self.input[new_line_idx][new_char_idx].isdigit() and self.input[new_line_idx][new_char_idx] != '.':
                                validNum = True
                        except IndexError:
                            continue
        if validNum:
            nums.append(int(curr_num))
        return sum(nums)

    @answer(80703636)
    def part_2(self) -> int:
        nums = {}
        key = None
        curr_num = ''

        for line_index, line in enumerate(self.input):
            if key:
                if key in nums:
                    curr_val = nums[key][0]
                    curr_count = nums[key][1]
                    nums[key] = (curr_val * int(curr_num), curr_count + 1)
                else:
                    nums[key] = (int(curr_num), 0)

            inNum = False
            key = None
            curr_num = ''
            for char_index, char in enumerate(line):
                if char.isdigit():
                    curr_num += char
                    inNum = True
                else:
                    if key:
                        if key in nums:
                            curr_val = nums[key][0]
                            curr_count = nums[key][1]
                            nums[key] = (curr_val * int(curr_num),
                                         curr_count + 1)
                        else:
                            nums[key] = (int(curr_num), 0)

                    inNum = False
                    key = None
                    curr_num = ''
                    continue

                if inNum:
                    for direction in _directions:
                        try:
                            new_line_idx = direction[0] + line_index
                            new_char_idx = direction[1] + char_index

                            if self.input[new_line_idx][new_char_idx] == "*":
                                key = (new_line_idx, new_char_idx)

                        except IndexError:
                            continue
        if key:
            if key in nums:
                curr_val = nums[key][0]
                curr_count = nums[key][1]
                nums[key] = (curr_val * int(curr_num), curr_count + 1)
            else:
                nums[key] = (int(curr_num), 0)
        return sum([x[0] for x in nums.values() if x[1] == 1])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
