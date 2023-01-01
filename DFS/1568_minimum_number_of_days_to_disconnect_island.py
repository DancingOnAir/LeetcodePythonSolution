from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        pass


def test_min_days():
    solution = Solution()
    assert solution.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 2, 'wrong result'
    assert solution.minDays([[1, 1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_days()
