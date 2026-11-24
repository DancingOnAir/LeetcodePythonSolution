class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            dp[i] = x + dp[i + 1] if x % 3 else x - dp[i + 1]
            if i < n - 1:
                s = x + nums[i + 1]
                s = s + dp[i + 2] if s % 3 else s - dp[i + 2]
                dp[i] = max(dp[i], s)
        return dp[0]


def test_max_difference():
    solution = Solution()
    assert solution.maxDifference([3, 6, 4]) == 5, 'wrong result'
    assert solution.maxDifference([6, 1, 2, 1, 2]) == 12, 'wrong result'
    assert solution.maxDifference([3, 3, 4, 5]) == -3, 'wrong result'


if __name__ == '__main__':
    test_max_difference()
