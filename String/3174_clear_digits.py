from string import digits


class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isnumeric():
                if stk:
                    stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

    def clearDigits1(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isalpha():
                stk.append(c)
            else:
                if stk and stk[-1].isalpha():
                    stk.pop()
                else:
                    stk.append(c)

        return ''.join(stk)


def test_clear_digits():
    solution = Solution()
    assert solution.clearDigits("abc") == "abc", 'wrong result'
    assert solution.clearDigits("cb34") == "", 'wrong result'


if __name__ == '__main__':
    test_clear_digits()
