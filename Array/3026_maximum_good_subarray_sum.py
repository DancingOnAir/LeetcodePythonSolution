from typing import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre_sum, val_to_min_pre_sum = 0, defaultdict(lambda: float('inf'))
        res = float('-inf')
        for i, x in enumerate(nums):
            if val_to_min_pre_sum[x] > pre_sum:
                val_to_min_pre_sum[x] = pre_sum
            pre_sum += x
            res = max(res, pre_sum - val_to_min_pre_sum[x - k], pre_sum - val_to_min_pre_sum[x + k])

        return res if res > float('-inf') else 0


def test_maximum_subarray_sum():
    solution = Solution()
    assert solution.maximumSubarraySum([1, 5], 2) == 0, 'wrong result'
    assert solution.maximumSubarraySum([1, 2, 3, 4, 5, 6], 1) == 11, 'wrong result'
    assert solution.maximumSubarraySum([-1, 3, 2, 4, 5], 3) == 11, 'wrong result'
    assert solution.maximumSubarraySum([-1, -2, -3, -4], 2) == -6, 'wrong result'


if __name__ == '__main__':
    test_maximum_subarray_sum()
