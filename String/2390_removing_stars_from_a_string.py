class Solution:
    # improved method
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c == '*':
                res.pop()
            else:
                res.append(c)

        return ''.join(res)

    # orginal method
    def removeStars1(self, s: str) -> str:
        s = list(s)
        stk = []
        for i, ch in enumerate(s):
            if ch == '*':
                s[i] = ''
                s[stk.pop()] = ''
            else:
                stk.append(i)
        return ''.join(s)


def test_remove_stars():
    solution = Solution()
    assert solution.removeStars("leet**cod*e") == "lecoe", 'wrong result'
    assert solution.removeStars("erase*****") == "", 'wrong result'


if __name__ == '__main__':
    test_remove_stars()
