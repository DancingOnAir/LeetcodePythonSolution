from typing import List
from collections import Counter


class Solution:
    # bytearray
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for r in range(n):
            row = bytearray(n + 1)
            col = bytearray(n + 1)
            for c in range(n):
                ro, co = matrix[r][c], matrix[c][r]
                row[ro] += 1
                col[co] += 1

                if row[ro] > 1 or col[co] > 1:
                    return False
        return True

    # one line by measuring length of row & col
    def checkValid2(self, matrix: List[List[int]]) -> bool:
        return all(len(set(m)) == len(matrix) for m in matrix + list(zip(*matrix)))

    # Counter
    def checkValid1(self, matrix: List[List[int]]) -> bool:
        c = Counter(range(1, len(matrix) + 1))

        for row in matrix:
            if len(c - Counter(row)) > 0:
                return False
        for col in zip(*matrix):
            if len(c - Counter(col)) > 0:
                return False
        return True


def test_check_valid():
    solution = Solution()

    assert solution.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]), 'wrong result'
    assert not solution.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]), 'wrong result'


if __name__ == '__main__':
    test_check_valid()
