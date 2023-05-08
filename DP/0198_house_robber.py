from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1Xj411K7oF/?spm_id_from=333.788&vd_source=e6f3bca3cb4f75b9e8b036e0e78f1541
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]

            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            memo[i] = res
            return res

        return dfs(len(nums) - 1)

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0

        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1

    def rob1(self, nums: List[int]) -> int:
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
