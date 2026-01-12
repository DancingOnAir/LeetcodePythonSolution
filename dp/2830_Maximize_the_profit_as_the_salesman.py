from typing import List
from functools import lru_cache


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        groups = [[] for _ in range(n)]
        for s, e, g in offers:
            groups[e].append([s, g])

        dp = [0] * (n + 1)
        for i, v in enumerate(groups):
            dp[i + 1] = dp[i]
            for s, g in v:
                dp[i + 1] = max(dp[i + 1], dp[s] + g)
        return dp[n]

    # MLE
    def maximizeTheProfit1(self, n: int, offers: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, last):
            if i >= m:
                return 0

            s, e, g = offers[i]
            if s <= last:
                return dfs(i + 1, last)
            return max(dfs(i + 1, e) + g, dfs(i + 1, last))

        offers.sort(key=lambda x: (x[0], x[1], -x[2]))
        m = len(offers)
        return dfs(0, -1)


def test_maximize_the_profit():
    solution = Solution()
    # assert solution.maximizeTheProfit(5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]]) == 3, 'wrong result'
    assert solution.maximizeTheProfit(5, [[0, 0, 1], [0, 2, 10], [1, 3, 2]]) == 10, 'wrong result'


if __name__ == '__main__':
    test_maximize_the_profit()
