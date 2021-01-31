from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(nums[i] - dp[i + 1][i + d], nums[i + d] - dp[i][i + d - 1])

        return dp[0][-1] >= 0


def test_predict_the_winner():
    solution = Solution()
    assert not solution.PredictTheWinner([1, 5, 2]), 'wrong result'
    assert solution.PredictTheWinner([1, 5, 233, 7]), 'wrong result'


if __name__ == '__main__':
    test_predict_the_winner()
