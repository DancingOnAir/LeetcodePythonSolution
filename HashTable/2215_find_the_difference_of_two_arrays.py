from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


def test_find_difference():
    solution = Solution()
    assert solution.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]], 'wrong result'
    assert solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []], 'wrong result'


if __name__ == '__main__':
    test_find_difference()
