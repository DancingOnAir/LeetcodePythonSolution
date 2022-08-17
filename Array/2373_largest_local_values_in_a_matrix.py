from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = list()
        for row in grid:
            res.append([max(row[i:i + 3]) for i in range(len(row) - 2)])
        pass


def test_largest_local():
    solution = Solution()
    assert solution.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]) == [[9, 9], [8, 6]], 'wrong result'
    assert solution.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]], 'wrong result'


if __name__ == '__main__':
    test_largest_local()
