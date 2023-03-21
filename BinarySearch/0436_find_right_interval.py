from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted((val[0], val[1], i) for i, val in enumerate(intervals))
        res = [-1] * len(intervals)
        for i, val in enumerate(intervals):

            j = bisect_left(arr, (val[1], val[1], 0))
            if j >= len(intervals):
                continue

            res[i] = arr[j][2]
        return res


def test_find_right_interval():
    solution = Solution()
    assert solution.findRightInterval([[1, 2]]) == [-1], 'wrong result'
    assert solution.findRightInterval([[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1], 'wrong result'
    assert solution.findRightInterval([[1, 4], [2, 3], [3, 4]]) == [-1, 2, -1], 'wrong result'


if __name__ == '__main__':
    test_find_right_interval()
