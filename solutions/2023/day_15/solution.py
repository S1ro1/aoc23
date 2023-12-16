# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/15

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 15
    separator = ","

    def calculate_hash(self, input: str) -> int:
        total = 0

        for c in input:
            total += ord(c)
            total *= 17
            total = total % 256

        return total

    @answer(506891)
    def part_1(self) -> int:
        return sum(map(self.calculate_hash, self.input))

    @answer(230462)
    def part_2(self) -> int:
        split_input = self.input
        hashmap: list[dict[str, tuple(int, int)]] = [{} for _ in range(256)]

        for key in split_input:
            if "-" in key:
                chars = key.split('-')[0]
                hash = self.calculate_hash(chars)
                empty_space = hashmap[hash].get(chars, (0, 999))
                hashmap[hash].pop(chars, None)
                for k, v in hashmap[hash].items():
                    if v[1] > empty_space[1]:
                        hashmap[hash][k] = (v[0], v[1] - 1)
            else:
                k, v = key.split("=")
                hash = self.calculate_hash(k)

                if hashmap[hash].get(k, None) == None:
                    if len(hashmap[hash]) == 0:
                        hashmap[hash][k] = (v, 0)
                    else:
                        hashmap[hash][k] = (
                            v, max([x[1] for x in hashmap[hash].values()]) + 1)
                else:
                    hashmap[hash][k] = (v, hashmap[hash][k][1])

        total = 0
        for i in range(len(hashmap)):
            for k, (value, index) in hashmap[i].items():
                val = (i + 1) * (index + 1) * int(value)
                total += val

        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
