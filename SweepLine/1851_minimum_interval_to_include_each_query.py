from typing import List
from collections import defaultdict
from bisect import bisect_right
from heapq import heappop, heappush


class Solution:
    # https://leetcode.com/problems/minimum-interval-to-include-each-query/solutions/1187616/python-heap-2-pointers-explained/
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        A = sorted(intervals) + [[float('inf'), 0]]
        Q = sorted([val, i] for i, val in enumerate(queries))
        l1, l2 = len(A), len(Q)
        h, res, p1, p2 = list(), [-1] * l2, 0, 0

        while p1 < l1 and p2 < l2:
            x, y = A[p1]
            q, idx = Q[p2]

            while h and h[0][1] < q:
                heappop(h)

            if x <= q:
                heappush(h, (y - x + 1, y))
                p1 += 1
            else:
                if h:
                    res[idx] = h[0][0]
                p2 += 1

        return res

    def minInterval1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)[::-1]
        h = list()
        res = dict()
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                i, j = intervals.pop()
                if j >= q:
                    heappush(h, [j - i + 1, j])

            while h and h[0][1] < q:
                heappop(h)

            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]


def test_min_interval():
    solution = Solution()
    assert solution.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4], 'wrong result'
    assert solution.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6], 'wrong result'


if __name__ == '__main__':
    test_min_interval()
