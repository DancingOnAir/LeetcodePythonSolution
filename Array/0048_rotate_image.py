from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        matrix.reverse()

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


def test_rotate():
    solution = Solution()

    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    solution.rotate(matrix1)
    print(matrix1)

    matrix2 = [[5, 1, 9, 11],
               [2, 4, 8, 10],
               [13, 3, 6, 7],
               [15, 14, 12, 16]]
    solution.rotate(matrix2)
    print(matrix2)


if __name__ == '__main__':
    test_rotate()
