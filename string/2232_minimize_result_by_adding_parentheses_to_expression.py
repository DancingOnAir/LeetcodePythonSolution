class Solution:
    def minimizeResult(self, expression: str) -> str:
        def cal(s):
            return eval(s.replace('(', '*(').replace(')', ')*').strip('*'))

        left, right = expression.split('+')
        lft = [left[:i] + '(' + left[i:] for i in range(len(left))]
        rgt = [right[:i] + ')' + right[i:] for i in range(1, len(right) + 1)]
        return min([l + '+' + r for l in lft for r in rgt], key=cal)

    def minimizeResult1(self, expression: str) -> str:
        res = expression
        val = eval(expression)
        x, y = expression.split('+')
        for i in range(len(x)):
            if i == 0:
                xx = '(' + x
            else:
                xx = x[:i] + '*(' + x[i:]
            for j in range(1, len(y) + 1):
                if j == len(y):
                    yy = y + ')'
                else:
                    yy = y[:j] + ')*' + y[j:]

                cur = xx + '+' + yy
                if eval(cur) < val:
                    val = eval(cur)
                    res = cur.replace('*', '')

        return res


def test_minimize_result():
    solution = Solution()
    assert solution.minimizeResult("247+38") == "2(47+38)", 'wrong result'
    assert solution.minimizeResult("12+34") == "1(2+3)4", 'wrong result'
    assert solution.minimizeResult("999+999") == "(999+999)", 'wrong result'


if __name__ == '__main__':
    test_minimize_result()
