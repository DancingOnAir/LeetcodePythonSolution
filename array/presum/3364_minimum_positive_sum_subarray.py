from itertools import accumulate
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ps = list(accumulate(nums, initial=0))
        res = float('inf')
        for k in range(l, r+1):
            for i in range(k, len(nums)+1):
                cur = ps[i] - ps[i - k]
                if 0 < cur < res:
                    res = cur
        return res if res < float('inf') else -1

    def minimumSumSubarray1(self, nums: List[int], l: int, r: int) -> int:
        res = float('inf')
        n = len(nums)
        ps = list(accumulate(nums, initial=0))
        for left in range(n):
            for right in range(left+1, n+1):
                cur = ps[right] - ps[left]
                sz = right - left
                if l <= sz <= r and 0 < cur < res:
                    res = cur
        return res if res < float('inf') else -1


def test_minimum_sum_subarray():
    solution = Solution()
    assert solution.minimumSumSubarray([3, -2, 1, 4], l=2, r=3) == 1, 'wrong result'
    assert solution.minimumSumSubarray([-2, 2, -3, 1], l=2, r=3) == -1, 'wrong result'
    assert solution.minimumSumSubarray([1, 2, 3, 4], l=2, r=4) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_sum_subarray()
