from typing import List
from collections import deque
import heapq


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        res = float('-inf')

        for x, y in points:
            while q and x - q[0][1] > k:
                heapq.heappop(q)
            if q:
                res = max(res, x + y - q[0][0])
            heapq.heappush(q, (x - y, x))
        return res

    # sliding window
    # max(y1 + y2 + |x2 - x1|) = max(y2 + x2) + max(y1 - x1) = max(x2 + y2) - min(x1 - y1)
    def findMaxValueOfEquation1(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        q = deque([points[0]])
        for right in range(1, len(points)):

            while q and points[right][0] - q[0][0] > k:
                q.popleft()

            if q:
                res = max(res, points[right][1] + points[right][0] + q[0][1] - q[0][0])

            while q and points[right][1] - points[right][0] > q[-1][1] - q[-1][0]:
                q.pop()

            q.append(points[right])
        return res


def test_find_max_value_of_equation():
    solution = Solution()

    # points1 = [[1, 3], [2, 0], [5, 10], [6, -10]]
    # k1 = 1
    # print(solution.findMaxValueOfEquation(points1, k1))
    #
    # points2 = [[0, 0], [3, 0], [9, 2]]
    # k2 = 3
    # print(solution.findMaxValueOfEquation(points2, k2))

    points3 = [[-17, 5], [-10, -8], [-5, -13], [-2, 7], [8, -14]]
    k3 = 4
    print(solution.findMaxValueOfEquation(points3, k3))


if __name__ == '__main__':
    test_find_max_value_of_equation()
