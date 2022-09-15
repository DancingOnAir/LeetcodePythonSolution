from typing import List
from collections import defaultdict, Counter


class Solution:
    # pythonic，先col后row使用Counter更简单
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = Counter(zip(*grid))
        return sum(c[tuple(r)] for r in grid)

    def equalPairs1(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        for r in grid:
            k = ','.join(map(str, r))
            m[k] += 1

        res = 0
        for c in zip(*grid):
            k = ','.join(map(str, c))
            if k in m:
                res += m[k]
        return res


def test_equal_pairs():
    solution = Solution()
    assert solution.equalPairs([[11, 1], [1, 11]]) == 2, 'wrong result'
    assert solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]) == 1, 'wrong result'
    assert solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_equal_pairs()
