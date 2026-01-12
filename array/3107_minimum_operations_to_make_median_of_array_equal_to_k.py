from typing import List
from bisect import bisect_left


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        return sum(max(nums[i] - k, 0) for i in range(n // 2 + 1)) + sum(max(k - nums[i], 0) for i in range(n // 2, n))

    def minOperationsToMakeMedianK1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mid = n // 2
        nums.sort()

        pos = bisect_left(nums, k)
        if pos == mid:
            return nums[mid] - k

        res = 0
        if pos < mid:
            for i in range(pos, mid + 1):
                res += nums[i] - k
        else:
            for i in range(mid, pos):
                res += k - nums[i]

        return res


def test_min_operations_to_make_median_k():
    solution = Solution()
    assert solution.minOperationsToMakeMedianK([2, 5, 6, 8, 5], 4) == 2, 'wrong result'
    assert solution.minOperationsToMakeMedianK([2, 5, 6, 8, 5], 7) == 3, 'wrong result'
    assert solution.minOperationsToMakeMedianK([1, 2, 3, 4, 5, 6], 4) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations_to_make_median_k()
