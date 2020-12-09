from typing import List


class Solution:
    def __init__(self):
        self.dp = [[[0.0] * 101 for _ in range(25)] for _ in range(25)]

    # memoization but TLE
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if r in self.dp and c in self.dp[r] and K in self.dp[r][c]:
            return self.dp[r][c][K]

        if r < 0 or r >= N or c < 0 or c >= N:
            return 0

        if not K:
            return 1

        total = self.knightProbability(N, K - 1, r - 1, c - 2) + self.knightProbability(N, K - 1, r - 2, c - 1)\
                + self.knightProbability(N, K - 1, r - 1, c + 2) + self.knightProbability(N, K - 1, r - 2, c + 1)\
                + self.knightProbability(N, K - 1, r + 1, c - 2) + self.knightProbability(N, K - 1, r + 2, c - 1)\
                + self.knightProbability(N, K - 1, r + 1, c + 2) + self.knightProbability(N, K - 1, r + 2, c + 1)
        res = total / 8
        self.dp[r][c][K] = res
        return res

    def knightProbability2(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

        offset = [2, 1, -2, -1, -2, 1, 2, -1, 2]
        for k in range(K + 1):
            for i in range(N):
                for j in range(N):
                    if not k:
                        dp[i][j][0] = 1
                        continue

                    for s in range(len(offset) - 1):
                        if 0 <= i + offset[s] < N and 0 <= j + offset[s + 1] < N:
                            dp[i][j][k] += dp[i + offset[s]][j + offset[s + 1]][k - 1] / 8
        return dp[r][c][K]

    # TLE
    def knightProbability1(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[[r, c]]] + [[] for _ in range(K)]

        for i in range(1, K+1):
            if not len(dp[i-1]):
                return 0

            offset = [2, 1, -2, -1, -2, 1, 2, -1, 2]
            for pos in dp[i-1]:
                for j in range(len(offset) - 1):
                    if 0 <= pos[0] + offset[j] < N and 0 <= pos[1] + offset[j+1] < N:
                        dp[i].append([pos[0] + offset[j], pos[1] + offset[j+1]])
        return len(dp[K]) / (8 ** K)


def test_knight_probability():
    solution = Solution()

    assert solution.knightProbability(3, 2, 0, 0) == 0.0625, 'wrong result'
    assert solution.knightProbability(1, 1, 0, 0) == 0.0, 'wrong result'


if __name__ == '__main__':
    test_knight_probability()
