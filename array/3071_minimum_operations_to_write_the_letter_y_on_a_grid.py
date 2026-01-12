from typing import List
from collections import Counter


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        center = n // 2
        not_y, y = Counter(), Counter()
        not_y_sum, y_sum = 0, 0

        for r in range(n):
            for c in range(n):
                if (r < center and (r == c or r == n - 1 - c)) or (r >= center and c == center):
                    y[grid[r][c]] += 1
                    y_sum += 1
                else:
                    not_y[grid[r][c]] += 1
                    not_y_sum += 1

        res = n * n
        for i in range(3):
            for j in range(3):
                if j != i:
                    res = min(res, y_sum - y[i] + not_y_sum - not_y[j])
        return res


def test_minimum_operations_to_write_y():
    solution = Solution()
    assert solution.minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]) == 3, 'wrong result'
    assert solution.minimumOperationsToWriteY(
        [[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]) == 12, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations_to_write_y()
