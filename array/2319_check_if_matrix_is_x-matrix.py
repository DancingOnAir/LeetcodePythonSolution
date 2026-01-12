from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True


def test_check_x_matrix():
    solution = Solution()
    assert solution.checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]), 'wrong result'
    assert not solution.checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]), 'wrong result'


if __name__ == '__main__':
    test_check_x_matrix()
