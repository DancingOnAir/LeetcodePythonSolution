from typing import List
from bisect import bisect_left


class Solution:
    # brute force
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = list()
        for r in matrix:
            arr += r
        return sorted(arr)[k - 1]


def test_kth_smallest():
    solution = Solution()
    assert solution.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 3) == 5, 'wrong result'
    assert solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13, 'wrong result'
    assert solution.kthSmallest([[-5]], 1) == -5, 'wrong result'


if __name__ == '__main__':
    test_kth_smallest()
