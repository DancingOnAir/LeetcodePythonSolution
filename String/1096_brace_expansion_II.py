from typing import List
from itertools import product


class Solution:
    # https://leetcode.com/problems/brace-expansion-ii/discuss/317623/Python3-Clear-and-Short-Recursive-Solution
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0

        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1

            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start: i]))

            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        print(groups)
        res = set()
        for group in groups:
            res |= set(map(''.join, product(*group)))

        return sorted(res)


def test_brace_expansion():
    solution = Solution()
    print(solution.braceExpansionII('{a{b,c},d{e,f}{g,{j,k}{h,i}}}'))
    # assert solution.braceExpansionII('{a{b,c}}') == ["ab", "ac"], 'wrong result'
    assert solution.braceExpansionII('{a,b}{c,{d,e}}') == ["ac", "ad", "ae", "bc", "bd", "be"], 'wrong result'
    assert solution.braceExpansionII('{{a,z},a{b,c},{ab,z}}') == ["a", "ab", "ac", "z"], 'wrong result'


if __name__ == '__main__':
    test_brace_expansion()
