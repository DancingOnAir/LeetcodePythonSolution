from typing import List
from collections import Counter


class Solution:
    #
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        stk = list()
        dp = [0] * n
        for i in range(n):
            while stk and stk[-1] >= nums[i]:
                stk.pop()

            stk.append(nums[i])
            dp[i] = len(stk)
        print(dp)
        res = 1
        for k, v in Counter(dp).items():
            res *= v
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
