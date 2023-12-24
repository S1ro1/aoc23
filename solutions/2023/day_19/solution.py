# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/19

from ...base import StrSplitSolution, answer

func_dict = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
}


class Solution(StrSplitSolution):
    _year = 2023
    _day = 19
    separator = "\n\n"

    def parse_workflows(self, workflows):
        parsed_workflows = {}

        for workflow in workflows.split('\n'):
            key, rules = workflow[:-1].split("{")
            *rules, fallback = rules.split(",")

            tmp = []
            for rule in rules:
                k, target = rule.split(":") # k is the rule

                x, cmp, val = k[0], k[1], int(k[2:])

                tmp.append((x, cmp, val, target))
            parsed_workflows[key] = (tmp, fallback)
        
        return parsed_workflows
    
    def parse_parts(self, parts):
        parsed_parts = []
        for part in parts.split('\n'):
            tmp = {}
            for x in part[1:-1].split(','):
                k, v = x.split('=')
            
                tmp[k] = int(v)
            
            parsed_parts.append(tmp)
            
        return parsed_parts
    
    def get_target(self, part, current_workflow):
        workflow, fallback = current_workflow
        for x, cmp, val, target in workflow:
            if func_dict[cmp](part[x], val):
                return target
        
        return fallback


    # @answer(1234)
    def part_1(self) -> int:
        workflows, parts = self.input

        workflows = self.parse_workflows(workflows)
        parts = self.parse_parts(parts)

        outputs = []
        for part in parts:
            current_workflow = 'in'
            while True:
                current_workflow = self.get_target(part, workflows[current_workflow])
                if current_workflow == 'R':
                    break
                elif current_workflow == 'A':
                    outputs.append(part)
                    break

        total = 0
        for out in outputs:
            total += sum(out.values())
        
        return total
    
    def _p2(self, rs, workflow_name, workflows):
        if workflow_name == 'R':
            return 0
        if workflow_name == 'A':
            tmp = 1
            for l, h in rs.values():
                tmp *= h - l + 1
            return tmp
        
        total = 0
        vals_left = True
        for key, cmp, val, target in workflows[workflow_name][0]:
            r = rs[key]
            true_half, false_half = None, None
            if cmp == "<":
                true_half = (r[0], val - 1)
                false_half = (val, r[1])
            else:
                true_half = (val + 1, r[1])
                false_half = (r[0], val)
        
            if true_half[0] <= true_half[1]:
                rs = dict(rs)
                rs[key] = true_half
                total += self._p2(rs, target, workflows)
            
            if false_half[0] <= false_half[1]:
                rs = dict(rs)
                rs[key] = false_half
            else:
                vals_left = False 

        if vals_left:
            total += self._p2(rs, workflows[workflow_name][1], workflows)
            
        return total

    # @answer(1234)
    def part_2(self) -> int:
        workflows, _ = self.input

        workflows = self.parse_workflows(workflows)

        t = self._p2({key: (1, 4000) for key in 'xmas'}, 'in', workflows)
        return t
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
