from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        path = list()
        m = n * 2

        def dfs(i, open):
            if i == m:
                res.append(''.join(path))
                return

            if open < n:
                path.append('(')
                dfs(i + 1, open + 1)
                path.pop()

            if i - open < open:
                path.append(')')
                dfs(i + 1, open)
                path.pop()
        dfs(0, 0)
        return res


def test_generate_parenthesis():
    solution = Solution()
    assert solution.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"], 'wrong result'
    assert solution.generateParenthesis(1) == ["()"], 'wrong result'


if __name__ == '__main__':
    test_generate_parenthesis()
