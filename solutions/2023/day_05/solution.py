# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 5

    @answer(178159714)
    def part_1(self) -> int:
        seeds, *maps = self.input.split("\n\n")
        seeds = list(map(int, seeds.split(':')[1].split()))

        for m in maps:
            lines = m.split('\n')[1:]
            ranges = []
            for line in lines:
                ranges.append(list(map(int, line.split())))
            new_seeds = []
            for seed in seeds:
                for (dst, src, rng) in ranges:
                    if seed in range(src, src + rng):
                        new_seeds.append(seed - src + dst)
                        break
                else:
                    new_seeds.append(seed)
            seeds = new_seeds

        return min(seeds)

    # @answer(1234)
    def part_2(self) -> int:
        tmp, *maps = self.input.split("\n\n")
        tmp = list(map(int, tmp.split(':')[1].split()))

        seeds = []
        for i in range(0, len(tmp), 2):
            seeds.append((tmp[i], tmp[i] + tmp[i+1]))

        for m in maps:
            lines = m.split('\n')[1:]
            ranges = []
            for line in lines:
                ranges.append(list(map(int, line.split())))

            new_seeds = []

            while 1:
                if len(seeds) <= 0:
                    break

                seed_s, seed_e = seeds.pop()
                for (dst, src, rng) in ranges:
                    overlap_start = max(seed_s, src)
                    overlap_end = min(seed_e, src + rng)
                    if overlap_start < overlap_end:
                        new_seeds.append(
                            (overlap_start - src + dst, overlap_end - src + dst))
                        if overlap_start > seed_s:
                            seeds.append((seed_s, overlap_start))
                        if seed_e > overlap_end:
                            seeds.append((overlap_end, seed_e))
                        break
                else:
                    new_seeds.append((seed_s, seed_e))

            seeds = new_seeds

        return min(seeds)[0]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
