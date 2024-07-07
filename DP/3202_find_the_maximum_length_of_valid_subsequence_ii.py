from typing import List
from collections import defaultdict, Counter


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        res = 0
        for v in range(k):
            dp = [0] * k
            for x in nums:
                dp[x % k] = dp[(v - x) % k] + 1
            res = max(res, max(dp))
        return res

    # dp[a][b] means the length of subsequence ending with ...,a,b
    def maximumLength1(self, nums: List[int], k: int) -> int:
        dp = defaultdict(Counter)
        for x in nums:
            for y in range(k):
                dp[y][x % k] = max(dp[y][x % k], dp[x % k][y] + 1)
        return max(max(dp[x].values()) for x in range(k))


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength([1,2,3,4,5], 2) == 5, 'wrong result'
    assert solution.maximumLength([1,4,2,3,1,4], 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
