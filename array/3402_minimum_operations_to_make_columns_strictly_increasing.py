from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i - 1][j]:
                    res += grid[i - 1][j] + 1 - grid[i][j]
                    grid[i][j] += grid[i - 1][j] + 1 - grid[i][j]
        return res


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([[3, 2], [1, 3], [3, 4], [0, 1]]) == 15, 'wrong result'
    assert solution.minimumOperations([[3, 2, 1], [2, 1, 0], [1, 2, 3]]) == 12, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
