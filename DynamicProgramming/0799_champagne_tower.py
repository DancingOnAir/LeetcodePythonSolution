class Solution:
    #
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if not poured:
            return 0

        dp = [[0.0] * col for col in range(1, query_row + 3)]
        dp[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                num = (dp[r][c] - 1.0) / 2.0
                if num > 0:
                    dp[r + 1][c] += num
                    dp[r + 1][c + 1] += num

        return min(1.0, dp[query_row][query_glass])


def test_champagne_tower():
    solution = Solution()

    assert solution.champagneTower(1, 1, 1) == 0.0000, 'wrong result'
    assert solution.champagneTower(2, 1, 1) == 0.5000, 'wrong result'
    assert solution.champagneTower(100000009, 33, 17) == 1.0000, 'wrong result'
    assert solution.champagneTower(25, 6, 1) == 0.18750, 'wrong result'


if __name__ == '__main__':
    test_champagne_tower()
