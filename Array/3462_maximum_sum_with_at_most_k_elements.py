from typing import List
from heapq import heappop, heappush


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        hp = []
        for i, r in enumerate(grid):
            r.sort(reverse=True)
            for j in range(limits[i]):
                heappush(hp, (-r[j], i))

        res = 0
        for _ in range(k):
            a, b = heappop(hp)
            if limits[b] > 0:
                res -= a
                limits[b] -= 1

        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([[1, 2], [3, 4]], limits=[1, 2], k=2) == 7, 'wrong result'
    assert solution.maxSum([[5, 3, 7], [8, 2, 6]], limits=[2, 2], k=3) == 21, 'wrong result'


if __name__ == '__main__':
    test_max_sum()

