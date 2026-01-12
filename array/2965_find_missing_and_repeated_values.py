from typing import List
from collections import Counter


class Solution:
    # hash
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = Counter(x for r in grid for x in r)
        d = {cnt[i]: i for i in range(1, len(grid) ** 2 + 1)}
        return [d[2], d[0]]

    # math + hash
    def findMissingAndRepeatedValues1(self, grid: List[List[int]]) -> List[int]:
        first = 0
        cnt = Counter()
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                total += x
                cnt[x] += 1
                if cnt[x] == 2:
                    first = x
        second = (1 + n * n) * n * n // 2 - total + first
        return [first, second]


def test_find_missing_and_repeated_values():
    solution = Solution()
    assert solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4], 'wrong result'
    assert solution.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [9, 5], 'wrong result'


if __name__ == '__main__':
    test_find_missing_and_repeated_values()
