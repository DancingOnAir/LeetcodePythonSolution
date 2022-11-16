class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = list()
        cur = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(cur)
                cur = 0
            else:
                cur = stk.pop() + max(1, cur * 2)
        return cur


def test_score_of_parentheses():
    solution = Solution()
    assert solution.scoreOfParentheses("(()(()))") == 6, 'wrong result'
    assert solution.scoreOfParentheses("()") == 1, 'wrong result'
    assert solution.scoreOfParentheses("(())") == 2, 'wrong result'
    assert solution.scoreOfParentheses("()()") == 2, 'wrong result'


if __name__ == '__main__':
    test_score_of_parentheses()
