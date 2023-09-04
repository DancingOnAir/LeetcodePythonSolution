from typing import List


class Solution:
    # mode1 choose or node choose
    def generateParenthesis1(self, n: int) -> List[str]:
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

    # mode 2
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(i, left, right):
            if len(path) == n:
                s = [')'] * n * 2
                for j in path:
                    s[j] = '('
                res.append(''.join(s))
                return

            # 可以填充0到left - right个右括号
            for j in range(left - right + 1):
                # 填充1个左括号
                path.append(i + j)
                dfs(i + j + 1, left + 1, right + j)
                path.pop()
        dfs(0, 0, 0)
        return res


def test_generate_parenthesis():
    solution = Solution()
    assert solution.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"], 'wrong result'
    assert solution.generateParenthesis(1) == ["()"], 'wrong result'


if __name__ == '__main__':
    test_generate_parenthesis()
