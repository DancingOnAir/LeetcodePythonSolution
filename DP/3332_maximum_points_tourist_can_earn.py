from typing import List
from functools import lru_cache


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(k - 1, -1, -1):
            for j, x in enumerate(stayScore[i]):
                dp[i][j] = max(dp[i + 1][j] + x, max(d + s for d, s in zip(dp[i + 1], travelScore[j])))
        return max(dp[0])

    # dfs
    def maxScore1(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, cur):
            if i == k:
                return 0
            # stay
            res = dfs(i + 1, cur) + stayScore[i][cur]
            # travel
            for dest in range(n):
                res = max(res, dfs(i + 1, dest) + travelScore[cur][dest])
            return res

        return max(dfs(0, j) for j in range(n))


def test_max_score():
    solution = Solution()
    assert solution.maxScore(2, 1, [[2, 3]], [[0, 2], [1, 0]]) == 3, 'wrong result'
    assert solution.maxScore(3, 2, [[3, 4, 2], [2, 1, 2]], [[0, 2, 1], [2, 0, 4], [3, 2, 0]]) == 8, 'wrong result'


if __name__ == '__main__':
    test_max_score()
