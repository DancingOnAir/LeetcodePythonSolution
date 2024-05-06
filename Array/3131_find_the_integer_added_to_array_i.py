from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return sorted(nums2)[0] - sorted(nums1)[0]


def test_added_integer():
    solution = Solution()
    assert solution.addedInteger([2, 6, 4], [9, 7, 5]) == 3, 'wrong result'
    assert solution.addedInteger([10], [5]) == -5, 'wrong result'
    assert solution.addedInteger([1, 1, 1, 1], [1, 1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_added_integer()
