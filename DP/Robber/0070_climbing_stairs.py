from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0
            if i < 2:
                return 1
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)


def test_climb_stairs():
    solution = Solution()
    assert solution.climbStairs(2) == 2, 'wrong result'
    assert solution.climbStairs(3) == 3, 'wrong result'


if __name__ == '__main__':
    test_climb_stairs()
