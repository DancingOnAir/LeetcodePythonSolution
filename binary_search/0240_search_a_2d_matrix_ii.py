from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        # start from the top-right cell
        row, col = 0, len(matrix[0]) - 1
        while row < n and col >= 0:
            mid = matrix[row][col]
            if mid == target:
                return True
            if mid > target:
                col -= 1
            else:
                row += 1
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r = bisect_right(matrix, [target])
        if r < len(matrix) and matrix[r][0] == target:
            return True

        for i in range(r):
            c = bisect_left(matrix[i], target)
            if c < len(matrix[i]) and matrix[i][c] == target:
                return True
        return False


def test_search_matrix():
    solution = Solution()

    assert solution.searchMatrix([[5], [6]], 5), 'wrong result'
    assert solution.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        5), 'wrong result'
    assert not solution.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        20), 'wrong result'


if __name__ == '__main__':
    test_search_matrix()
