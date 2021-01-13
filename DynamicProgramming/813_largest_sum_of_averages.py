from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        pre_sum = [0]
        for a in A:
            pre_sum.append(pre_sum[-1] + a)

        def average(i, j):
            return (pre_sum[j] - pre_sum[i]) / (j - i)

        n = len(A)
        dp = [average(i, n) for i in range(n)]

        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], dp[j] + average(i, j))
        return dp[0]

    def largestSumOfAverages1(self, A: List[int], K: int) -> float:
        n = len(A)
        if K == 1:
            return sum(A) / n
        if K == n:
            return sum(A)

        pre_sum = [0]
        for a in A:
            pre_sum.append(pre_sum[-1] + a)

        dp = [[0.0] * (K + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][1] = pre_sum[i] / i

        for i in range(1, n + 1):
            for k in range(2, K + 1):
                for j in range(k - 1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + (pre_sum[i] - pre_sum[j]) / (i - j))
        return dp[-1][-1]


def test_largest_sum_of_averages():
    solution = Solution()

    A1 = [9, 1, 2, 3, 9]
    K1 = 3
    assert solution.largestSumOfAverages(A1, K1) == 20, 'wrong result'


if __name__ == '__main__':
    test_largest_sum_of_averages()
