# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    _digit_map = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }

    def sum_first_and_last(self, input: list[str]) -> int:
        return sum(map(lambda digits: int(digits[0] + digits[-1]), [list(filter(lambda c: c.isdigit(), line)) for line in input]))

    @answer(54304)
    def part_1(self) -> int:
         return self.sum_first_and_last(self.input)


    @answer(54418)
    def part_2(self) -> int:
        outputs = []
        for line in self.input:
            new_line = ""

            for i in range(0, len(line)):
                replaced = False
                if line[i].isdigit():
                    new_line += line[i]
                    break

                for k, v in self._digit_map.items():
                    if line[i:].startswith(k):
                        new_line += v
                        replaced = True
                        break
                
                if replaced:
                    break
        
            for i in range(len(line), 0, -1):
                replaced = False
                if line[i-1].isdigit():
                    new_line += line[i-1]
                    break
                else:
                    for k, v in self._digit_map.items():
                        if line[i-1-len(v):].startswith(k):
                            new_line += v
                            replaced = True
                            break
                
                if replaced:
                    break
            outputs.append(new_line)
        
        return self.sum_first_and_last(outputs)


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
