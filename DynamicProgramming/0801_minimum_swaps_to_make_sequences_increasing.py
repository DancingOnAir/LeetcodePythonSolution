from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0

        dp = [0] * n
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[i] = dp[i - 1]
            elif A[i - 1] >= A[i] > B[i - 1] or B[i - 1] >= B[i] > A[i - 1]:
                dp[i] = dp[i - 1] + 1
                A[i], B[i] = B[i], A[i]
        return dp[n - 1]


def test_min_swap():
    solution = Solution()

    A1 = [1, 3, 5, 4]
    B1 = [1, 2, 3, 7]
    assert solution.minSwap(A1, B1) == 1, 'wrong result'

    A2 = [0, 3, 5, 8, 9]
    B2 = [2, 1, 4, 6, 9]
    assert solution.minSwap(A2, B2) == 1, 'wrong result'

    A3 = [3, 3, 8, 9, 10]
    B3 = [1, 7, 4, 6, 8]
    assert solution.minSwap(A3, B3) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_swap()
