from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2:
            return 0
        elif sum1 > sum2:
            return self.minOperations(nums2, nums1)

        target = sum2 - sum1

        gains1 = [6 - x for x in nums1]
        gains2 = [x - 1 for x in nums2]
        gains = gains1 + gains2
        gains.sort(reverse=True)

        res = 0
        for g in gains:
            target -= g
            res += 1
            if target <= 0:
                return res
        return -1


def test_min_operations():
    solution = Solution()

    assert solution.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]) == 3, 'wrong result'
    assert solution.minOperations([1, 1, 1, 1, 1, 1, 1], [6]) == -1, 'wrong result'
    assert solution.minOperations([6, 6], [1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_operations()

