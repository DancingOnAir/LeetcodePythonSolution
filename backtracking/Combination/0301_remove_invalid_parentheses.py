from typing import List


class Solution:
    # backtracking + pruning
    # time complex O(n x 2^n)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(i, cur, left_remove, right_remove, balance):
            if left_remove < 0 or right_remove < 0 or balance < 0:
                return

            if left_remove == 0 and right_remove == 0:
                if len(cur) == l:
                    res.add(cur)

            if i == n:
                return

            if s[i] == '(':
                dfs(i + 1, cur + s[i], left_remove, right_remove, balance + 1)
                dfs(i + 1, cur, left_remove - 1, right_remove, balance)
            elif s[i] == ')':
                dfs(i + 1, cur + s[i], left_remove, right_remove, balance - 1)
                dfs(i + 1, cur, left_remove, right_remove - 1, balance)
            else:
                dfs(i + 1, cur + s[i], left_remove, right_remove, balance)

        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove == 0:
                    right_remove += 1
                else:
                    left_remove -= 1
        l = len(s) - left_remove - right_remove
        res = set()
        n = len(s)
        dfs(0, '', left_remove, right_remove, 0)
        return list(res)


def test_remove_invalid_parentheses():
    solution = Solution()
    assert solution.removeInvalidParentheses("()())()") == ["(())()", "()()()"], 'wrong result'
    assert solution.removeInvalidParentheses("(a)())()") == ["(a())()", "(a)()()"], 'wrong result'
    assert solution.removeInvalidParentheses(")(") == [""], 'wrong result'


if __name__ == '__main__':
    test_remove_invalid_parentheses()
