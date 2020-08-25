from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n
        for i in range(n):
            if obstacleGrid[0][i]:
                break
            else:
                dp[i] = 1

        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    if dp[j] and not obstacleGrid[i][j]:
                        dp[j] = 1
                    else:
                        dp[j] = 0
                else:
                    if obstacleGrid[i][j]:
                        dp[j] = 0
                    else:
                        dp[j] += dp[j - 1]
        return dp[n - 1]


def test_unique_paths_with_obstacles():
    solution = Solution()

    obstacle_grid1 = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]]
    print(solution.uniquePathsWithObstacles(obstacle_grid1))

    obstacle_grid2 = [[1, 0]]
    print(solution.uniquePathsWithObstacles(obstacle_grid2))

    obstacle_grid3 = [[0], [1]]
    print(solution.uniquePathsWithObstacles(obstacle_grid3))


if __name__ == '__main__':
    test_unique_paths_with_obstacles()
