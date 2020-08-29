from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return 0

        n = len(matrix[0])
        if not n:
            return 0

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            temp = matrix[mid // n][mid % n]
            if temp == target:
                return True
            elif temp < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return 0

        n = len(matrix[0])
        if not n:
            return 0

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1] and target in matrix[i]:
                return True
        return False


def test_search_matrix():
    solution = Solution()

    matrix1 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 50]]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))

    matrix2 = [[1, 3, 5, 7],
               [10, 11, 16, 20],
               [23, 30, 34, 50]]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))


if __name__ == '__main__':
    test_search_matrix()
