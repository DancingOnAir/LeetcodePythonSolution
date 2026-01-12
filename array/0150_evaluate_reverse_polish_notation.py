from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stk = list()

        def helper(a, b, c):
            if c == '+':
                return a + b
            if c == '-':
                return b - a
            if c == '*':
                return a * b
            if c == '/':
                return int(b / a)

        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                stk.append(helper(stk.pop(), stk.pop(), t))
            else:
                stk.append(int(t))
        return stk[-1]


def test_eval_rpn():
    solution = Solution()
    assert solution.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]) == -7, 'wrong result'
    assert solution.evalRPN(["4", "3", "/"]) == 1, 'wrong result'
    assert solution.evalRPN(["3", "11", "+", "5", "-"]) == 9, 'wrong result'
    assert solution.evalRPN(["18"]) == 18, 'wrong result'
    assert solution.evalRPN(["4", "3", "-"]) == 1, 'wrong result'
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9, 'wrong result'
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6, 'wrong result'
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, 'wrong result'


if __name__ == '__main__':
    test_eval_rpn()
