from functools import lru_cache
from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        mx = int(n ** 0.5)

        @lru_cache(None)
        def dfs(x, c):
            if x < 1:
                return 0 if c == 0 else inf

            if c < x * x:
                return dfs(x - 1, c)
            return min(dfs(x - 1, c), dfs(x, c - x * x) + 1)
        return dfs(mx, n)


def test_num_squares():
    solution = Solution()
    assert solution.numSquares(12) == 3, 'wrong result'
    assert solution.numSquares(13) == 2, 'wrong result'


if __name__ == '__main__':
    test_num_squares()
