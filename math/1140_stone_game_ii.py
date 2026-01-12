from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dfs(i, m):
            if i + 2 * m >= n:
                return piles[i]
            return piles[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)


def test_stone_game_ii():
    solution = Solution()
    assert solution.stoneGameII([2, 7, 9, 4, 4]) == 10, 'wrong result'
    assert solution.stoneGameII([1, 2, 3, 4, 5, 100]) == 104, 'wrong result'


if __name__ == '__main__:':
    test_stone_game_ii()
