from typing import List
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # dp[i][a] means the longest good subsequence with i different neighbours,
        dp = [defaultdict(int) for _ in range(k + 1)]
        # res[i] is the longest good subsequence with i different neighbours.
        res = [0] * (k + 1)
        for x in nums:
            for i in range(k, -1, -1):
                dp[i][x] = max(dp[i][x] + 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], dp[i][x])
        return res[k]

    # TLE
    def maximumLength1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if not n:
            return 0

        dp = [[1] * (k + 1) for _ in range(n)]
        for i in range(n):
            for j in range(k + 1):
                for p in range(i):
                    if nums[i] == nums[p]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)

        return max(max(r) for r in dp)


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength([1, 2, 1, 1, 3], 2) == 4, 'wrong result'
    assert solution.maximumLength([1, 2, 3, 4, 5, 1], 0) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()