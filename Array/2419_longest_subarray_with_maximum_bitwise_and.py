from typing import List
from itertools import groupby


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = cur = mx = 0
        for x in nums:
            if mx < x:
                mx = x
                res = cur = 0

            if mx == x:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res

    # groupby
    def longestSubarray(self, nums: List[int]) -> int:
        return max((k, len(list(g))) for k, g in groupby(nums))[1]


def test_longest_subarray():
    solution = Solution()
    assert solution.longestSubarray([1, 2, 3, 3, 2, 2, 3, 3, 3]) == 3, 'wrong result'
    assert solution.longestSubarray([1, 2, 3, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_subarray()
