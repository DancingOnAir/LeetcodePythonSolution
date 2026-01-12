from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            max_row = 0
            for row in range(len(mat)):
                max_row = row if mat[row][mid] > mat[max_row][mid] else max_row

            left_is_bigger = mid - 1 >= left and mat[max_row][mid - 1] > mat[max_row][mid]
            right_is_bigger = mid + 1 <= right and mat[max_row][mid + 1] > mat[max_row][mid]
            if (not left_is_bigger) and (not right_is_bigger):
                return [max_row, mid]
            elif left_is_bigger:
                right = mid - 1
            else:
                left = mid + 1
        return []


def test_find_peak_grid():
    solution = Solution()
    assert solution.findPeakGrid([[1, 4], [3, 2]]) == [1, 0], 'wrong result'
    assert solution.findPeakGrid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]) == [1, 1], 'wrong result'


if __name__ == '__main__':
    test_find_peak_grid()
