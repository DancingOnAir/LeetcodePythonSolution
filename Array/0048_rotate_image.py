from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [r[::-1] for r in zip(*matrix)]

    # zip
    def rotate3(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        transposed = zip(*matrix)
        for i, row in enumerate(transposed):
            matrix[i] = reversed(row)

    # transpose first then reverse
    def rotate2(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for i, row in enumerate(matrix):
            matrix[i].reverse()

    # reverse first, then transpose
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        matrix.reverse()
        print(matrix)
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
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
