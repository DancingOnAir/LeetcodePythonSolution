from typing import List
from itertools import accumulate


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = list(accumulate(nums, initial=0))
        min_s = [float('inf')] * k
        res = float('-inf')
        for j, x in enumerate(pre_sum):
            i = j % k
            res = max(res, x - min_s[i])
            min_s[i] = min(min_s[i], x)
        return res


def test_max_subarray_sum():
    solution = Solution()
    assert solution.maxSubarraySum([1, 2], 1) == 3, 'wrong result'
    assert solution.maxSubarraySum([-1, -2, -3, -4, -5], 4) == -10, 'wrong result'
    assert solution.maxSubarraySum([-5, 1, 2, -3, 4], 2) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_subarray_sum()

