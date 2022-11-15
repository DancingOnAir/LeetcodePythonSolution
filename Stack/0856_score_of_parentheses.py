class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = list()
        res = 0

        for ch in s:
            if ch == ')':

            stk.append(ch)
        pass


def test_score_of_parentheses():
    solution = Solution()
    assert solution.scoreOfParentheses("()") == 1, 'wrong result'
    assert solution.scoreOfParentheses("(())") == 2, 'wrong result'
    assert solution.scoreOfParentheses("()()") == 2, 'wrong result'


if __name__ == '__main__':
    test_score_of_parentheses()
