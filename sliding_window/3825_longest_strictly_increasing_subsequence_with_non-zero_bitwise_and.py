from typing import List
from bisect import bisect_left


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def helper(b):
            stk = []
            for x in nums:
                if x & b:
                    if not stk or stk[-1] < x:
                        stk.append(x)
                    else:
                        stk[bisect_left(stk, x)] = x
            return len(stk)
        return max(helper(1 << i) for i in range(30))


def test_longest_subsequence():
    solution = Solution()
    assert solution.longestSubsequence([5, 4, 7]) == 2, 'wrong result'
    assert solution.longestSubsequence([2, 3, 6]) == 3, 'wrong result'
    assert solution.longestSubsequence([0, 1]) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_subsequence()
