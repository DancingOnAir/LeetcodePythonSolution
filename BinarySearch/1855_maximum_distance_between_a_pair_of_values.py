from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        res = 0
        for i, v in enumerate(nums1):
            left, right = 0, l2 - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] >= v:
                    left = mid + 1
                else:
                    right = mid - 1
            res = max(res, left - 1 - i if left >= i else 0)
        return res


def test_max_distance():
    solution = Solution()
    assert solution.maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]) == 2, 'wrong result'
    assert solution.maxDistance([2, 2, 2], [10, 10, 1]) == 1, 'wrong result'
    assert solution.maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_distance()
