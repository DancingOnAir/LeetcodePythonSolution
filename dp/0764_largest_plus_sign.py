from typing import List
from bisect import bisect_right


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        rows = [[-1, N] for _ in range(N)]
        cols = [[-1, N] for _ in range(N)]

        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)

        for i in range(N):
            rows[i].sort()
            cols[i].sort()

        res = 0
        for r in range(N):
            for i in range(len(rows[r]) - 1):
                left = rows[r][i]
                right = rows[r][i + 1]
                for c in range(left + res + 1, right - res):
                    idx = bisect_right(cols[c], r) - 1
                    up = cols[c][idx]
                    down = cols[c][idx + 1]
                    res = max(res, min(c - left, right - c, r - up, down - r))

        return res

    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        dp = [[N] * N for _ in range(N)]

        for i, j in mines:
            dp[i][j] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if dp[i][j] else 0
                dp[i][j] = min(dp[i][j], l)

                r = r + 1 if dp[i][k] else 0
                dp[i][k] = min(dp[i][k], r)

                u = u + 1 if dp[j][i] else 0
                dp[j][i] = min(dp[j][i], u)

                d = d + 1 if dp[k][i] else 0
                dp[k][i] = min(dp[k][i], d)

        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res

    def validate_one(self, N, mines, x, y):
        if x < 0 or x >= N or y < 0 or y >= N or [x, y] in mines:
            return False
        return True

    # brute force solution but TLE
    def orderOfLargestPlusSign1(self, N: int, mines: List[List[int]]) -> int:
        res = 0
        for i in range(N):
            for j in range(N):
                order = 0
                if [i, j] not in mines:
                    order += 1
                    radius = 1
                    while self.validate_one(N, mines, i - radius, j) and self.validate_one(N, mines, i + radius, j) and\
                            self.validate_one(N, mines, i, j - radius) and self.validate_one(N, mines, i, j + radius):
                        order += 1
                        radius += 1
                res = max(res, order)
        return res


def test_order_of_largest_plus_sign():
    solution = Solution()

    N1 = 5
    mines1 = [[4, 2]]
    assert solution.orderOfLargestPlusSign(N1, mines1) == 2, 'wrong result'

    N2 = 2
    mines2 = []
    assert solution.orderOfLargestPlusSign(N2, mines2) == 1, 'wrong result'

    N3 = 1
    mines3 = [[0, 0]]
    assert solution.orderOfLargestPlusSign(N3, mines3) == 0, 'wrong result'


if __name__ == '__main__':
    test_order_of_largest_plus_sign()
