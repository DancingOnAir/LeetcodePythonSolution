from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        mark = [[False] * n for _ in range(m)]
        for i in range(m):
            for j, val in enumerate(matrix[i]):
                if not val:
                    mark[i][j] = True

        for i in range(m):
            for j, val in enumerate(mark[i]):
                if val:
                    matrix[i][:] = [0] * n
                    for k in range(m):
                        matrix[k][j] = 0


def test_set_zeroes():
    solution = Solution()

    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix1)
    print(matrix1)

    matrix2 = [[0, 1, 2, 0],[3, 4, 5, 2],[1, 3, 1, 5]]
    solution.setZeroes(matrix2)
    print(matrix2)


if __name__ == '__main__':
    test_set_zeroes()
