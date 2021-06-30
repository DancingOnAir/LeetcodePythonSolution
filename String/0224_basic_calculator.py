class Solution:
    def calculate(self, s: str) -> int:
        res = cur = 0
        sign = 1
        stk = list()

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == ')':
                res += sign * cur
                res *= stk.pop()
                res += stk.pop()
                cur = 0
            elif c == '(':
                stk.append(res)
                stk.append(sign)
                sign = 1
                res = 0
            elif c in '+-':
                res += sign * cur
                cur = 0
                sign = [-1, 1][c == '+']

        return res + sign * cur


def test_calculate():
    solution = Solution()

    assert solution.calculate("1 + 1") == 2, 'wrong result'
    assert solution.calculate(" 2-1 + 2 ") == 3, 'wrong result'
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23, 'wrong result'
    assert solution.calculate("+48 + -48") == 0, 'wrong result'


if __name__ == '__main__':
    test_calculate()
