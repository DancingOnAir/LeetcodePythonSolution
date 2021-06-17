class Solution:
    # brute force
    def isValid(self, s: str) -> bool:
        s2 = ""
        while s2 != s:
            s, s2 = s.replace('abc', ''), s
        return s == ''

    # stack
    def isValid1(self, s: str) -> bool:
        stk = list()
        for c in s:
            if c == 'c':
                if not stk or stk.pop() != 'b':
                    return False
                if not stk or stk.pop() != 'a':
                    return False
            else:
                stk.append(c)

        return not stk


def test_is_valid():
    solution = Solution()

    assert solution.isValid('aabcbc'), 'wrong result'
    assert solution.isValid('abcabcababcc'), 'wrong result'
    assert not solution.isValid('abccba'), 'wrong result'
    assert not solution.isValid('cababc'), 'wrong result'


if __name__ == '__main__':
    test_is_valid()
