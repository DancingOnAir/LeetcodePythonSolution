from typing import List
from functools import lru_cache
from collections import Counter


class Solution:
    # dp
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0] * 2 for _ in range(n)]
        mx = 0
        for i in range(n):
            sz = dp[i][0]
            cnt = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] == sz:
                        cnt += dp[j][1]
                    elif dp[j][0] > sz:
                        cnt = dp[j][1]
                        sz = dp[j][0]
            dp[i] = [sz + 1, cnt if cnt != 0 else 1]
            mx = max(mx, dp[i][0])
        return sum(dp[i][1] for i in range(n) if dp[i][0] == mx)

    # double dp
    def findNumberOfLIS1(self, nums: List[int]) -> int:
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
