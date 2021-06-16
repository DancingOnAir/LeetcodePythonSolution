class Solution:
    def isValid(self, s: str) -> bool:
        stk = list()
        for c in s:
            if c == 'c':
                if not stk or stk.pop() != 'b':
                    return False
                if not stk or stk.pop() != 'a':
                    return False
            else:
                stk.append(c)

        return False if stk else True


def test_is_valid():
    solution = Solution()

    assert solution.isValid('aabcbc'), 'wrong result'
    assert solution.isValid('abcabcababcc'), 'wrong result'
    assert not solution.isValid('abccba'), 'wrong result'
    assert not solution.isValid('cababc'), 'wrong result'


if __name__ == '__main__':
    test_is_valid()
