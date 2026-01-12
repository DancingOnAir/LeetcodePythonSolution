from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(row[i] for j, row in enumerate(mat) for i in {j, len(mat) - 1 - j})

    def diagonalSum1(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[n - 1 - i][i]
        return res - mat[n // 2][n // 2] if n & 1 else res


def test_diagonal_sum():
    solution = Solution()

    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert solution.diagonalSum(mat1) == 25, "error input"

    mat2 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    assert solution.diagonalSum(mat2) == 8, "error input"


if __name__ == '__main__':
    test_diagonal_sum()
