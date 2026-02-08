from typing import List
from math import ceil, sqrt
from bisect import bisect_left


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        n = len(nums)

        def check(k):
            return n + sum((x - 1) // k for x in nums) <= k * k

        left = ceil(sqrt(n))
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def minimumK1(self, nums: List[int]) -> int:
        def check(k):
            return sum(ceil(x / k) for x in nums) <= k * k

        nums.sort()
        left, right = ceil(sqrt(len(nums))), max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


def test_minimum_k():
    solution = Solution()
    assert solution.minimumK([3, 7, 5]) == 3, 'wrong result'
    assert solution.minimumK([1]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_k()
