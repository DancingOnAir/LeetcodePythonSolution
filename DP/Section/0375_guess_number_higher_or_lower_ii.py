from math import inf
from functools import lru_cache


class Solution:
    # dfs + cache
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0
            elif i + 1 == j:
                return i
            return min(max(dfs(i, k - 1), dfs(k + 1, j)) + k for k in range(i + 1, j))
        return dfs(1, n)


def test_get_money_amount():
    solution = Solution()
    assert solution.getMoneyAmount(10) == 16, 'wrong result'
    assert solution.getMoneyAmount(1) == 0, 'wrong result'
    assert solution.getMoneyAmount(2) == 1, 'wrong result'


if __name__ == '__main__':
    test_get_money_amount()

