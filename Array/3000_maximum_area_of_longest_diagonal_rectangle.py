from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        h, w = max(dimensions, key=lambda x: (x[0] ** 2 + x[1] ** 2, x[0] * x[1]))
        return h * w


def test_area_of_max_diagonal():
    solution = Solution()
    assert solution.areaOfMaxDiagonal([[9, 3], [8, 6]]) == 48, 'wrong result'
    assert solution.areaOfMaxDiagonal([[3, 4], [4, 3]]) == 12, 'wrong result'


if __name__ == '__main__':
    test_area_of_max_diagonal()
