from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        dp1, dp2 = 0, 0
        for a, b in zip(nums1, nums2):
            if max(a, b) > max(nums1[-1], nums2[-1]):
                return -1
            if min(a, b) > min(nums1[-1], nums2[-1]):
                return -1
            if a > nums1[-1] or b > nums2[-1]:
                dp1 += 1
            if a > nums2[-1] or b > nums1[-1]:
                dp2 += 1
        return min(dp1, dp2)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 2], [2, 1]) == 1, 'wrong result'
    assert solution.minOperations([1, 1, 1], [1, 5, 15]) == 0, 'wrong result'
    assert solution.minOperations([1, 5, 15], [1, 1, 1]) == 0, 'wrong result'
    assert solution.minOperations([1, 2, 7], [4, 5, 3]) == 1, 'wrong result'
    assert solution.minOperations([2, 3, 4, 5, 9], [8, 8, 4, 4, 4]) == 2, 'wrong result'
    assert solution.minOperations([1, 5, 4], [2, 5, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
