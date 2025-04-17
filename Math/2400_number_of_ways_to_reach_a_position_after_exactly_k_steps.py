from functools import lru_cache
from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if endPos - startPos > k or (k - endPos + startPos) % 2:
            return 0
        return comb(k, (endPos - startPos + k) // 2) % (10 ** 9 + 7)

    def numberOfWays1(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10 ** 9 + 7

        # 表示当前在x，还剩left步时，走到终点的方案数
        @lru_cache(None)
        def dfs(x, left):
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1
            return (dfs(x - 1, left - 1) + dfs(x + 1, left - 1)) % mod

        return dfs(startPos, k)


def test_number_of_ways():
    solution = Solution()
    assert solution.numberOfWays(1, 2, 3) == 3, 'wrong result'
    assert solution.numberOfWays(2, 5, 10) == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_ways()
