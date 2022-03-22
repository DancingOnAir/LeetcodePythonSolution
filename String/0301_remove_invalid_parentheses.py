from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def count_invalid_closing_bracket(ss):

        stk = list()
        closing_bracket = 0
        for ch in s:
            if ch == ')':
                if stk:
                   stk.pop()
                else:
                    closing_bracket += 1
            elif ch == '(':
                stk.append(ch)
        bracket = len(stk)


def test_remove_invalid_parentheses():
    solution = Solution()
    assert solution.removeInvalidParentheses("()())()") == ["(())()", "()()()"], 'wrong result'
    assert solution.removeInvalidParentheses("(a)())()") == ["(a())()", "(a)()()"], 'wrong result'
    assert solution.removeInvalidParentheses(")(") == [""], 'wrong result'


if __name__ == '__main__':
    test_remove_invalid_parentheses()

