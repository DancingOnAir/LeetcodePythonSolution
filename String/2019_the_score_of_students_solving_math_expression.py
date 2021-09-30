from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:


    # short dfs
    def scoreOfStudents2(self, s: str, answers: List[int]) -> int:
        op = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

        @lru_cache(None)
        def dfs(s):
            if len(s) == 1:
                return {s[0]}

            return set([op[s[i]](a, b) for i in range(1, len(s), 2) for a in dfs(s[:i]) for b in dfs(s[i+1:]) if op[s[i]](a, b) <= 1000])

        d = defaultdict(int)
        t = tuple(c if c in ('+', '*') else int(c) for c in s)
        for x in dfs(t):
            d[x] = 2
        d[eval(s)] = 5
        return sum(d[x] for x in answers)

    # TLE
    def scoreOfStudents1(self, s: str, answers: List[int]) -> int:
        def cal(digits, ops, correct_cal_seq):
            if len(digits) == 1:
                if correct_cal_seq:
                    nonlocal correct_result
                    correct_result = digits[0]

                results.add(digits[0])
                return

            for i in range(len(ops)):
                if ops[i] == '+':
                    res = digits[i] + digits[i + 1]
                else:
                    res = digits[i] * digits[i + 1]

                new_pops = ops[:]
                new_pops.pop(i)
                new_digits = digits[:i] + [res] + digits[i + 2:]

                if new_pops.count('*') == 0:
                    if len(new_pops) == add_op or correct_cal_seq:
                        cal(new_digits, new_pops, True)
                    else:
                        cal(new_digits, new_pops, False)
                else:
                    cal(new_digits, new_pops, False)

        ops = list()
        digits = list()
        add_op = multiply_op = 0
        for c in s:
            if c.isdigit():
                digits.append(int(c))
            else:
                if c == '+':
                    add_op += 1
                else:
                    multiply_op += 1
                ops.append(c)

        results = set()
        correct_result = -1

        cal(digits, ops, False)

        res = 0
        for ans in answers:
            if ans == correct_result:
                res += 5
            elif ans in results:
                res += 2
        return res


def test_score_of_students():
    solution = Solution()

    assert solution.scoreOfStudents("7+3*1*2", [20, 13, 42]) == 7, 'wrong result'
    assert solution.scoreOfStudents("3+5*2", [13, 0, 10, 13, 13, 16, 16]) == 19, 'wrong result'
    assert solution.scoreOfStudents("6+0*1", [12, 9, 6, 4, 8, 6]) == 10, 'wrong result'
    assert solution.scoreOfStudents("1+2*3+4", [13, 21, 11, 15]) == 11, 'wrong result'


if __name__ == '__main__':
    test_score_of_students()

