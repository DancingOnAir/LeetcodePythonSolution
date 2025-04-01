from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        n = len(nums1)
        res = tot = 0
        for i in range(n):
            diff = nums1[i] - nums2[i]
            if diff % k != 0:
                return -1
            if diff > 0:
                res += diff // k
            tot += diff
        return -1 if tot else res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([4, 3, 1, 4], nums2=[1, 3, 7, 1], k=3) == 2, 'wrong result'
    assert solution.minOperations([3, 8, 5, 2], nums2=[2, 4, 1, 6], k=1) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
