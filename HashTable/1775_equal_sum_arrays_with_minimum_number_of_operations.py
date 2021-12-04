from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        changes1 = [0] * 6
        changes2 = [0] * 6

        for x in nums1:
            changes1[6 - x] += 1
            changes1[x - 1] += 1

        for x in nums2:
            changes2[6 - x] += 1
            changes2[x - 1] += 1

        # freq1, freq2 = [0] * 7, [0] * 7
        # sum1 = sum2 = 0
        #
        # for x in nums1:
        #     freq1[x] += 1
        #     sum1 += x
        #
        # for x in nums2:
        #     freq2[x] += 1
        #     sum2 += x
        #
        # res = 0
        # if sum1 == sum2:
        #     return res
        # if sum1 < sum2:
        #     if
        #
        # return res
        pass


def test_min_operations():
    solution = Solution()

    assert solution.minOperations([1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]) == 3, 'wrong result'
    assert solution.minOperations([1, 1, 1, 1, 1, 1, 1], [6]) == -1, 'wrong result'
    assert solution.minOperations([6, 6], [1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_operations()

