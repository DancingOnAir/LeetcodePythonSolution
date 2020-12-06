from typing import List
from collections import Counter


class Solution:
    #
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp1, dp2 = [1] * n, [1] * n
        max_len, res = 1, 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j] + 1
                        dp2[i] = dp2[j]
                    elif dp1[j] + 1 == dp1[i]:
                        dp2[i] += dp2[j]

            if dp1[i] > max_len:
                max_len = dp1[i]
                res = dp2[i]
            elif dp1[i] == max_len:
                res += dp2[i]
        return res


def test_find_number_of_LIS():
    solution = Solution()

    nums1 = [1, 3, 5, 4, 7]
    assert solution.findNumberOfLIS(nums1) == 2, 'wrong result'

    nums2 = [2, 2, 2, 2, 2]
    assert solution.findNumberOfLIS(nums2) == 5, 'wrong result'

    nums3 = [1, 2, 4, 3, 5, 4, 7, 2]
    assert solution.findNumberOfLIS(nums3) == 3, 'wrong result'


if __name__ == '__main__':
    test_find_number_of_LIS()
