from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)

        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return -inf
            return max(dfs(i - 1, j - 1) + nums1[i] * nums2[j], dfs(i - 1, j), dfs(i, j - 1), nums1[i] * nums2[j])
        return dfs(l1 - 1, l2 - 1)


def test_max_dot_product():
    solution = Solution()
    assert solution.maxDotProduct([2, 1, -2, 5], [3, 0, -6]) == 18, 'wrong result'
    assert solution.maxDotProduct([3, -2], [2, -6, 7]) == 21, 'wrong result'
    assert solution.maxDotProduct([-1, -1], [1, 1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_max_dot_product()
