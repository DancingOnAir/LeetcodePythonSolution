class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        cnt = 0
        for c in s:
            if c == '(' and cnt > 0:
                res += c
            elif c == ')' and cnt > 1:
                res += c
            cnt += 1 if c == '(' else -1
        return res

    def removeOuterParentheses1(self, s: str) -> str:
        stk = list()
        depth = 0
        res = ''
        i = 0
        while i < len(s):
            while not stk or depth > 0:
                if s[i] == '(':
                    depth += 1
                else:
                    depth -= 1

                stk.append(s[i])
                i += 1

            res += ''.join(stk)[1:-1]
            stk = list()

        return res


def test_remove_outer_parentheses():
    solution = Solution()

    assert solution.removeOuterParentheses("(()())(())") == "()()()", 'wrong result'
    assert solution.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())", 'wrong result'
    assert solution.removeOuterParentheses("()()") == "", 'wrong result'


if __name__ == '__main__':
    test_remove_outer_parentheses()
