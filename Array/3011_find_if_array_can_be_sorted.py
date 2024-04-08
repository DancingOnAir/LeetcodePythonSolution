from typing import List
from itertools import groupby, chain


class Solution:
    # one line
    def canSortArray(self, nums: List[int]) -> bool:
        return list(chain.from_iterable(sorted(g) for _, g in groupby(nums, key=lambda x: bin(x)[2:].count('1')))) == sorted(nums)

    # O(n)
    def canSortArray1(self, nums: List[int]) -> bool:
        def helper(x):
            return bin(x)[2:].count('1')

        i, last = 0, 0

        while i < len(nums):
            bits = helper(nums[i])
            mx = mi = nums[i]
            j = i + 1
            while j < len(nums) and helper(nums[j]) == bits:
                mi = min(mi, nums[j])
                mx = max(mx, nums[j])
                j += 1

            if mi < last:
                return False

            i, last = j, mx

        return True


def test_can_sort_array():
    solution = Solution()
    # assert solution.canSortArray([8, 4, 2, 30, 15]), 'wrong result'
    # assert solution.canSortArray([1, 2, 3, 4, 5]), 'wrong result'
    assert not solution.canSortArray([3, 16, 8, 4, 2]), 'wrong result'


if __name__ == '__main__':
    test_can_sort_array()
