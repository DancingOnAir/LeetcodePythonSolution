from typing import List
from heapq import heappop, heappush

# class Fenwick:
#     def __init__(self, n):
#         self.tree = [0] * n
#
#     def add(self, i, v):
#         while i < len(self.tree):
#             self.tree[i] += v
#             i += i & -i
#
#     def query(self, i):
#         res = 0
#         while i > 0:
#             res += self.tree[i]
#             i -= i & -i
#         return res

class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)


class Solution:
    # heap
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        left = [[] for _ in heights]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                left[b].append((heights[a], i))

        h = []
        for i, x in enumerate(heights):
            while h and h[0][0] < x:
                res[heappop(h)[1]] = i

            for l in left[i]:
                heappush(h, l)
        return res


def test_left_most_building_queries():
    solution = Solution()
    assert solution.leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]) == [2, 5, -1,
                                                                                                              5,
                                                                                                              2], 'wrong result'
    assert solution.leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]) == [7,
                                                                                                                    6,
                                                                                                                    -1,
                                                                                                                    4,
                                                                                                                    6], 'wrong result'


if __name__ == '__main__':
    test_left_most_building_queries()
