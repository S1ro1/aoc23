# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    def _parse_input(self) -> list[tuple[int, list[str]]]:
        return list(map(lambda line: (int(line.split(': ')[0].split()[1]), line.split(': ')[1].split('; ')), self.input))

    @answer(2105)
    def part_1(self) -> int:
        colors = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        game_turns = self._parse_input()
        valid_ids = []

        for id, game in game_turns:
            valid = True

            for turn in game:
                cubes = turn.split(', ')

                for cube in cubes:
                    num, color = cube.split(' ')
                    num = int(num)
                    if num > colors[color]:
                        valid = False
            
            if valid:
                valid_ids.append(id)

        return sum(valid_ids) 


    @answer(72422)
    def part_2(self) -> int:
        game_turns = self._parse_input()

        powers = []

        for id, game in game_turns:
            max_r, max_g, max_b = 0, 0, 0
            for turn in game:
                cubes = turn.split(', ')

                for cube in cubes:
                    num, color = cube.split(' ')
                    num = int(num) 

                    if color == 'red':
                        max_r = max(max_r, num)
                    elif color == 'green':
                        max_g = max(max_g, num)
                    elif color == 'blue':
                        max_b = max(max_b, num)
            
            powers.append(max_r * max_g * max_b)
        
        return sum(powers)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
