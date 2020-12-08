from typing import List


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
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


if __name__ == '__main__':
    test_knight_probability()
