from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0
        rows, cols = set(), set()
        for t, i, v in queries[::-1]:
            if t == 0:
                if i not in rows:
                    res += (n - len(cols)) * v
                    rows.add(i)
            else:
                if i not in cols:
                    res += (n - len(rows)) * v
                    cols.add(i)
        return res


def test_matrix_sum_queries():
    solution = Solution()
    assert solution.matrixSumQueries(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]) == 23, 'wrong result'
    assert solution.matrixSumQueries(3, [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]) == 17, 'wrong result'


if __name__ == '__main__':
    test_matrix_sum_queries()
