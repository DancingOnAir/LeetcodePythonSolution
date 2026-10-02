class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == ')' and stk:
                if stk[-1] != '(':
                    return False
                else:
                    stk.pop()
            elif c == ']' and stk:
                if stk[-1] != '[':
                    return False
                else:
                    stk.pop()
            elif c == '}' and stk:
                if stk[-1] != '{':
                    return False
                else:
                    stk.pop()
            else:
                stk.append(c)
        return len(stk) == 0


def test_is_valid():
    solution = Solution()
    assert solution.isValid("()"), 'wrong result'
    assert solution.isValid("()[]{}"), 'wrong result'
    assert not solution.isValid("(]"), 'wrong result'
    assert solution.isValid("([])"), 'wrong result'
    assert not solution.isValid("([)]"), 'wrong result'


if __name__ == '__main__':
    test_is_valid()
