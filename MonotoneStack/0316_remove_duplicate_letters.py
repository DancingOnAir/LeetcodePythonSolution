class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        memo = {c: i for i, c in enumerate(s)}
        stk = list()

        for i, c in enumerate(s):
            if c in stk:
                continue
            while stk and stk[-1] > c and memo[stk[-1]] > i:
                stk.pop()
            stk.append(c)
        return ''.join(stk)


def test_remove_duplicate_letters():
    solution = Solution()
    assert solution.removeDuplicateLetters("bcabc") == "abc", 'wrong result'
    assert solution.removeDuplicateLetters("cbacdcbc") == "acdb", 'wrong result'


if __name__ == '__main__':
    test_remove_duplicate_letters()

