from typing import List
from collections import defaultdict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m[mat[i][j]] = [i, j]

        cnt_r, cnt_c = defaultdict(int), defaultdict(int)
        for i, x in enumerate(arr):
            r, c = m[x]
            cnt_r[r] += 1
            cnt_c[c] += 1
            if cnt_r[r] == len(mat[0]) or cnt_c[c] == len(mat):
                return i
        return -1


def test_first_complete_index():
    solution = Solution()
    assert solution.firstCompleteIndex([1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]]) == 1, 'wrong result'
    assert solution.firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]) == 2, 'wrong result'
    assert solution.firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9],
                                       [[3, 2, 5], [1, 4, 6], [8, 7, 9]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_first_complete_index()
