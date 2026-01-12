from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            res[r1][c1] += 1
            if r2 + 1 < n:
                res[r2 + 1][c1] -= 1
            if c2 + 1 < n:
                res[r1][c2 + 1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                res[r2 + 1][c2 + 1] += 1
        # sweep line by row
        for r in range(1, n):
            for c in range(n):
                res[r][c] += res[r - 1][c]
        # sweep line by col
        for r in range(n):
            for c in range(1, n):
                res[r][c] += res[r][c - 1]
        return res

    # https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-w-visualization-clean-concise/
    # Time complexity: O(n2+nq) ≈ O(nq) if q≫n; 这里q是queries的长度
    def rangeAddQueries1(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                res[r][c1] += 1
                if c2 + 1 < n:
                    res[r][c2 + 1] -= 1
        for i in range(n):
            for j in range(1, n):
                res[i][j] += res[i][j - 1]
        return res


def test_range_add_queries():
    solution = Solution()
    assert solution.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]) == [[1, 1, 0], [1, 2, 1],
                                                                         [0, 1, 1]], 'wrong result'
    assert solution.rangeAddQueries(2, [[0, 0, 1, 1]]) == [[1, 1], [1, 1]], 'wrong result'


if __name__ == '__main__':
    test_range_add_queries()
