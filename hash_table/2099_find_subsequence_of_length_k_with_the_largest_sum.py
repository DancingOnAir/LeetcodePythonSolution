from typing import List
from collections import Counter
import heapq


class Solution:
    # sort
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = sorted((v, i)for i, v in enumerate(nums))
        return [v for v, _ in sorted(nums[-k:], key=lambda x: x[1])]

    # heapq
    def maxSubsequence1(self, nums: List[int], k: int) -> List[int]:
        nums = [(v, i)for i, v in enumerate(nums)]
        res = heapq.nlargest(k, nums)
        return [v for v, _ in sorted(res, key=lambda x: x[1])]


def test_max_subsequence():
    solution = Solution()
    assert solution.maxSubsequence([2, 1, 3, 3], 2) == [3, 3], 'wrong result'
    assert solution.maxSubsequence([-1, -2, 3, 4], 3) == [-1, 3, 4], 'wrong result'
    assert solution.maxSubsequence([3, 4, 3, 3], 2) == [4, 3], 'wrong result'


if __name__ == '__main__':
    test_max_subsequence()
