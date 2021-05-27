class Solution:
    # pythonic stack
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stk = list()

        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    s[i] = ''
        while stk:
            s[stk.pop()] = ''
        return ''.join(s)

    def minRemoveToMakeValid1(self, s: str) -> str:
        idx = list()
        res = list()
        i = 0

        for c in s:
            if c == '(':
                idx.append(i)
                res.append(c)
                i += 1
            elif c == ')':
                if idx:
                    idx.pop()
                    res.append(c)
                    i += 1
            else:
                res.append(c)
                i += 1
        while idx:
            res.pop(idx[-1])
            idx.pop()

        return ''.join(res)


def test_min_remove_to_make_valid():
    solution = Solution()
    assert solution.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de", 'wrong result'
    assert solution.minRemoveToMakeValid("a)b(c)d") == "ab(c)d", 'wrong result'
    assert solution.minRemoveToMakeValid("))((") == "", 'wrong result'
    assert solution.minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)", 'wrong result'


if __name__ == '__main__':
    test_min_remove_to_make_valid()
