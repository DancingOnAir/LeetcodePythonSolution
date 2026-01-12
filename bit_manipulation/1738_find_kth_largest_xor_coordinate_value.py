from typing import List
from heapq import heappush, heappop, heappushpop


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = map(len, (matrix, matrix[0]))
        res = [[0] * (C + 1) for _ in range(R + 1)]
        hp = list()
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                res[r + 1][c + 1] = cell ^ res[r][c + 1] ^ res[r + 1][c] ^ res[r][c]
                if len(hp) < k:
                    heappush(hp, res[r + 1][c + 1])
                else:
                    heappushpop(hp, res[r + 1][c + 1])
        return hp[0]

    # concise
    def kthLargestValue2(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pq = list()

        for i in range(m):
            for j in range(n):
                if i:
                    matrix[i][j] ^= matrix[i - 1][j]
                if j:
                    matrix[i][j] ^= matrix[i][j - 1]
                if i and j:
                    matrix[i][j] ^= matrix[i - 1][j - 1]
                if len(pq) < k:
                    heappush(pq, matrix[i][j])
                else:
                    heappushpop(pq, matrix[i][j])
        return pq[0]

    # original
    def kthLargestValue1(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = [[-1] * n for _ in range(m)]
        hp = list()

        for i in range(m):
            for j in range(n):
                if 0 <= i - 1 < m and 0 <= j - 1 < n:
                    res[i][j] = res[i - 1][j - 1] ^ res[i - 1][j] ^ res[i][j - 1] ^ matrix[i][j]
                elif 0 <= i - 1 < m:
                    res[i][j] = res[i - 1][j] ^ matrix[i][j]
                elif 0 <= j - 1 < n:
                    res[i][j] = res[i][j - 1] ^ matrix[i][j]
                else:
                    res[i][j] = matrix[i][j]
                heappush(hp, -res[i][j])

        for i in range(k - 1):
            heappop(hp)
        return -heappop(hp)


def test_kth_largest_value():
    solution = Solution()
    assert solution.kthLargestValue([[5, 2], [1, 6]], 1) == 7, 'wrong result'
    assert solution.kthLargestValue([[5, 2], [1, 6]], 2) == 5, 'wrong result'
    assert solution.kthLargestValue([[5, 2], [1, 6]], 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_kth_largest_value()
