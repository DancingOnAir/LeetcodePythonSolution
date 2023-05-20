from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if coins[i] > c:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i, c - coins[i])
        return dfs(n - 1, amount)


def test_change():
    solution = Solution()
    assert solution.change(5, [1, 2, 5]) == 4, 'wrong result'
    assert solution.change(3, [2]) == 0, 'wrong result'
    assert solution.change(10, [10]) == 1, 'wrong result'


if __name__ == '__main__':
    test_change()


