from typing import List
from itertools import combinations


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if numSelect == n:
            return m

        res = 0
        for comb in combinations(range(n), numSelect):
            cur = 0
            for r in range(m):
                valid = True
                for c in range(n):
                    if c not in comb and matrix[r][c] == 1:
                        valid = False
                        break
                cur += valid
            res = max(res, cur)
        return res


def test_maximum_rows():
    solution = Solution()
    assert solution.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2) == 3, 'wrong result'
    assert solution.maximumRows([[1], [0]], 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_rows()
