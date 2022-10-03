from typing import List
from itertools import groupby


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return max((k, len(list(g))) for k, g in groupby(nums))[1]


def test_longest_subarray():
    solution = Solution()
    assert solution.longestSubarray([1, 2, 3, 3, 2, 2, 3, 3, 3]) == 3, 'wrong result'
    assert solution.longestSubarray([1, 2, 3, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_subarray()
