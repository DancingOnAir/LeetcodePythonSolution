from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = [c for r in grid for c in r ]
        if len(set(v % x for v in vals)) > 1:
            return -1
        median = sorted(vals)[len(vals) // 2]
        return sum(abs(median - v) // x for v in vals)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([[2, 4], [6, 8]], x=2) == 4, 'wrong result'
    assert solution.minOperations([[1, 5], [2, 3]], x=1) == 5, 'wrong result'
    assert solution.minOperations([[1, 2], [3, 4]], x=2) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
