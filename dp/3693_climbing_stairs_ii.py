class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            dp[i] = costs[i] + 1 + dp[i + 1]
            if i + 2 <= n:
                dp[i] = min(dp[i], costs[i + 1] + 4 + dp[i + 2])
            if i + 3 <= n:
                dp[i] = min(dp[i], costs[i + 2] + 9 + dp[i + 3])
        return dp[0]


def test_climb_stairs():
    solution = Solution()
    assert solution.climbStairs(4, costs=[1, 2, 3, 4]) == 13, 'wrong result'
    assert solution.climbStairs(4, costs=[5, 1, 6, 2]) == 11, 'wrong result'
    assert solution.climbStairs(3, costs=[9, 8, 3]) == 12, 'wrong result'


if __name__ == "__main__":
    test_climb_stairs()
