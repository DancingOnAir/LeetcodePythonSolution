from functools import lru_cache


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0:
                return float('inf')
            if j < 0:
                return 0
            return min(dp(i, j - 1) + int(floor[j]), dp(i - 1, j - carpetLen))
        return dp(numCarpets, len(floor) - 1)

    # dp[i][j] 代表用i条地毯覆盖前j块板砖
    def minimumWhiteTiles1(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0] * n for _ in range(numCarpets + 1)]
        dp[0][0] = floor[0] == '1'
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + (floor[j] == '1')

        for i in range(1, numCarpets + 1):
            for j in range(carpetLen, n):
                dp[i][j] = min(dp[i][j - 1] + (floor[j] == '1'), dp[i - 1][j - carpetLen])
        return dp[-1][-1]


def test_minimum_white_tiles():
    solution = Solution()
    assert solution.minimumWhiteTiles("10110101", 2, 2) == 2, 'wrong result'
    assert solution.minimumWhiteTiles("11111", 2, 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_white_tiles()
