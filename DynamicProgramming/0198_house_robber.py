from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]


def test_rob():
    solution = Solution()

    nums1 = [1, 2, 3, 1]
    assert solution.rob(nums1) == 4, 'wrong result'
    nums2 = [2, 7, 9, 3, 1]
    assert solution.rob(nums2) == 12, 'wrong result'


if __name__ == '__main__':
    test_rob()
