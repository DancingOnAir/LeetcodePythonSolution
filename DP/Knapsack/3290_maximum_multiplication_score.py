from typing import List
from functools import lru_cache


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == 4:
                return 0
            if j == len(b):
                return float('-inf')
            return max(dfs(i, j + 1), dfs(i + 1, j + 1) + a[i] * b[j])
        return dfs(0, 0)


def test_max_score():
    solution = Solution()
    assert solution.maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]) == 26, 'wrong result'
    assert solution.maxScore([-1, 4, 5, -2], [-5, -1, -3, -2, -4]) == -1, 'wrong result'


if __name__ == '__main__':
    test_max_score()
