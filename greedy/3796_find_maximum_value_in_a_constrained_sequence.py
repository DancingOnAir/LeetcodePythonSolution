from typing import List
from math import inf


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        max_val = [inf] * n
        for i, x in restrictions:
            max_val[i] = x

        res = [0] * n
        for i, d in enumerate(diff):
            res[i + 1] = min(res[i] + d, max_val[i + 1])
        # res[0] = 0 no need to update
        for i in range(n - 2, 0, -1):
            res[i] = min(res[i], res[i + 1] + diff[i])

        return max(res)


def test_find_max_val():
    solution = Solution()
    assert solution.findMaxVal(10, [[3, 1], [8, 1]], [2, 2, 3, 1, 4, 5, 1, 1, 2]) == 6, 'test1'
    assert solution.findMaxVal(8, [[3, 2]], [3, 5, 2, 4, 2, 3, 1]) == 12, 'test2'


if __name__ == '__main__':
    test_find_max_val()
