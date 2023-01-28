from typing import List
from heapq import heappush, heappop


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
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
