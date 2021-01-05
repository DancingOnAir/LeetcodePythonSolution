class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if not poured:
            return 0
        if query_row == 0 and query_glass == 0:
            return 1

        dp = [[0.0] * i for i in range(1, query_row + 2)]
        dp[0][0] = 1.0
        poured -= 1
        for i in range(1, query_row + 1):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] / 2
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] / 2
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) / 2

                if i == query_row and j == query_glass:
                    return poured * dp[i][j] if poured < i + 1 else 1
            poured -= i + 1
        return dp[query_row][query_glass]

        # prev_sum = (query_row + 1) * query_row // 2
        # cur_sum = (query_row + 2) * (query_row + 1) // 2
        #
        # if poured <= prev_sum:
        #     return 0
        # elif poured >= cur_sum:
        #     return 1
        # cur_glass_num = query_row + 1
        # res = (poured - prev_sum) / (cur_glass_num * 2 - 2)
        # if query_glass == 0 or query_glass == cur_glass_num - 1:
        #     return res
        # else:
        #     return res * 2


def test_champagne_tower():
    solution = Solution()

    assert solution.champagneTower(1, 1, 1) == 0.0000, 'wrong result'
    assert solution.champagneTower(2, 1, 1) == 0.5000, 'wrong result'
    assert solution.champagneTower(100000009, 33, 17) == 1.0000, 'wrong result'
    assert solution.champagneTower(25, 6, 1) == 0.18750, 'wrong result'


if __name__ == '__main__':
    test_champagne_tower()
