class Solution:
    # ^ is logical xor:
    # The decimal values of lowercase and uppercase English letters differ with each other by 32.
    # Take an example: a -> 97(1100001), A -> 65 (1000001). So we have a ^ 32 = A, A ^ 32 = a.
    #    1 1 0 0 0 0 1 (97)
    # ^  0 1 0 0 0 0 0 (32)
    #    1 0 0 0 0 0 1 (65)
    def makeGood(self, s: str) -> str:
        stk = list()
        for c in s:
            if stk and stk[-1] == chr(ord(c) ^ 32):
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

    def makeGood1(self, s: str) -> str:
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
