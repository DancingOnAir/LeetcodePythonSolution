class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i][j][k]: i表示子串左端点的位置，j=0表示不删除，j=1表示删除, k 为false表示不取反，true为取反
        dp = [[[float('-inf')] * 2 for _ in range(2)] for _ in range(n + 1)]
        res = float('-inf')
        for i in range(n - 1, -1, -1):
            x = nums[i]
            dp[i][0][0] = max(dp[i + 1][0][1], 0) + x
            dp[i][0][1] = max(dp[i + 1][0][0], 0) - x
            dp[i][1][0] = max(dp[i + 1][1][1] + x, dp[i + 1][0][0])
            dp[i][1][1] = max(dp[i + 1][1][0] - x, dp[i + 1][0][1])
            res = max(res, dp[i][0][0], dp[i][1][0])
        return res


def test_max_alternating_sum():
    solution = Solution()
    assert solution.maxAlternatingSum([5,-5,1]) == 11, 'wrong result'
    assert solution.maxAlternatingSum([10,-5,-100]) == 110, 'wrong result'
    assert solution.maxAlternatingSum([4,7]) == 7, 'wrong result'


if __name__ == '__main__':
    test_max_alternating_sum()
