class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        # dp[i][j]: i表示子串右端点的位置，j=0表示不删除，j=1表示删除
        dp = [[float('-inf')] * 2] + [[0, 0] for _ in arr]
        for i, x in enumerate(arr):
            dp[i + 1][0] = max(dp[i][0], 0) + x
            dp[i + 1][1] = max(dp[i][1] + x, dp[i][0])
        return max(max(x) for x in dp)


def test_maximum_sum():
    solution = Solution()
    assert solution.maximumSum([1, -2, 0, 3]) == 4, 'wrong result'
    assert solution.maximumSum([1, -2, -2, 3]) == 3, 'wrong result'
    assert solution.maximumSum([-1, -1, -1, -1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_maximum_sum()
