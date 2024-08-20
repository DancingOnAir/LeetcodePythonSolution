from typing import List
from itertools import accumulate


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        d = [0] * (10 ** 6 + 1)
        for l, r in intervals:
            d[l] += 1
            if r < 10 ** 6:
                d[r + 1] -= 1
        return max(accumulate(d))


def test_min_groups():
    solution = Solution()
    assert solution.minGroups([[1, 1]]) == 1, 'wrong result'
    assert solution.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3, 'wrong result'
    assert solution.minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_groups()
