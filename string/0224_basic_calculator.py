class Solution:
    def calculate(self, s: str) -> int:
        def calc():
            if len(nums) < 2:
                ops.pop()
                return

            b = nums.pop()
            a = nums.pop()
            sign = ops.pop()
            nums.append(a + b * (1 if sign == '+' else -1))

        s = s.replace(' ', '')
        ops = list()
        nums = list()
        nums.append(0)

        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c == '(':
                ops.append(c)
            elif c == ')':
                while ops:
                    op = ops[-1]
                    if op != '(':
                        calc()
                    else:
                        ops.pop()
                        break
            else:
                if c.isdigit():
                    num = 0
                    j = i
                    while j < n and s[j].isdigit():
                        num = num * 10 + int(s[j])
                        j += 1
                    nums.append(num)
                    i = j - 1
                else:
                    if s[i - 1] in '(+-':
                        nums.append(0)

                    while ops and ops[-1] != '(':
                        calc()
                    ops.append(c)
            i += 1

        while ops:
            calc()
        return nums[-1]

    def calculate1(self, s: str) -> int:
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
