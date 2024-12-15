from typing import List
from bisect import bisect_left
from itertools import pairwise


class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    def pre(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = sorted(zip(xCoord, yCoord))
        # 离散化
        ys = sorted(set(yCoord))
        res = -1
        tree = Fenwick(len(ys))
        tree.add(bisect_left(ys, points[0][1]) + 1)
        pre = {}
        for (x1, y1), (x2, y2) in pairwise(points):
            y = bisect_left(ys, y2) + 1
            tree.add(y)
            if x1 != x2:
                continue
            cur = tree.query(bisect_left(ys, y1) + 1, y)
            if y2 in pre and pre[y2][1] == y1 and pre[y2][2] + 2 == cur:
                res = max(res, (x2 - pre[y2][0]) * (y2 - y1))
            pre[y2] = (x1, y1, cur)
        return res


def test_max_rectangle_area():
    solution = Solution()
    assert solution.maxRectangleArea([1,1,3,3], [1,3,1,3]) == 4, 'wrong result'
    assert solution.maxRectangleArea([1,1,3,3,2], [1,3,1,3,2]) == -1, 'wrong result'
    assert solution.maxRectangleArea([1,1,3,3,1,3], [1,3,1,3,2,2]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_rectangle_area()
