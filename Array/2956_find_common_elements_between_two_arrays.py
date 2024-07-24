from typing import List
from collections import Counter


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def helper(arr1, arr2):
            return sum(v for k, v in Counter(arr1).items() if k in set(arr2))

        return [helper(nums1, nums2), helper(nums2, nums1)]


def test_find_intersection_values():
    solution = Solution()
    assert solution.findIntersectionValues([2, 3, 2], [1, 2]) == [2, 1], 'wrong result'
    assert solution.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]) == [3, 4], 'wrong result'
    assert solution.findIntersectionValues([3, 4, 2, 3], [1, 5]) == [0, 0], 'wrong result'


if __name__ == '__main__':
    test_find_intersection_values()
