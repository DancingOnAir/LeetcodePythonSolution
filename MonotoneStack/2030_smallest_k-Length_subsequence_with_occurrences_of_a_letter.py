from collections import Counter
from itertools import accumulate


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        cnt_letter = len([c for c in s if c == letter])
        stk = list()

        for i, c in enumerate(s):
            while stk and stk[-1] > c and len(stk) + len(s) - i > k and (stk[-1] != letter or cnt_letter > repetition):
                repetition += (stk.pop() == letter)
            if len(stk) < k:
                if c == letter:
                    stk.append(c)
                    repetition -= 1
                elif k - len(stk) > repetition:
                    stk.append(c)
            if c == letter:
                cnt_letter -= 1
        return ''.join(stk)

    def smallestSubsequence1(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        m = list(accumulate([c == letter for c in s][::-1]))[::-1]
        stk = ['#']
        for i, c in enumerate(s):
            while stk[-1] > c and len(stk) + n - i > k + 1 and (stk[-1] != letter or repetition < m[i]):
                repetition += (stk.pop() == letter)
            if len(stk) < min(k, k - repetition + (c == letter)) + 1:
                stk += [c]
                repetition -= (c == letter)
        return ''.join(stk[1:])


def test_smallest_subsequence():
    solution = Solution()

    # assert solution.smallestSubsequence("leet", 3, "e", 1) == "eet", 'wrong result'
    assert solution.smallestSubsequence("leetcode", 4, "e", 2) == "ecde", 'wrong result'
    assert solution.smallestSubsequence("bb", 2, "b", 2) == "bb", 'wrong result'


if __name__ == '__main__':
    test_smallest_subsequence()
