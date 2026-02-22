from typing import List
from collections import Counter


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        cnt = Counter(p[1] for p in points)
        res = tot = 0
        for k in cnt.values():
            c = k * (k - 1) // 2
            res += c * tot
            tot += c
        return res % MOD


def test_count_trapezoids():
    solution = Solution()
    assert solution.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]) == 3, 'wrong result'
    assert solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_trapezoids()
