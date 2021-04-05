class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s

        stk = ['']
        for c in s:
            if stk[-1].swapcase() == c:
                stk.pop()
            else:
                stk.append(c)

        return ''.join(stk)


def test_make_good():
    solution = Solution()
    assert solution.makeGood('leEeetcode') == 'leetcode', 'wrong result'
    assert solution.makeGood('abBAcC') == '', 'wrong result'
    assert solution.makeGood('s') == 's', 'wrong result'


if __name__ == '__main__':
    test_make_good()
