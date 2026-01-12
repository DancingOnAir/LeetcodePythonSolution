from typing import List


class Solution:
    # monotone stack
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stk = list()
        res = [-1] * n
        for i in range(n - 1, -1, -1):
            p, s = cars[i]
            # Imagine a,b,c on the road
            # if the a catches b later than b catched c,
            # then a won't catch b but b+c.
            while stk and (cars[stk[-1]][1] >= s or (cars[stk[-1]][0] - p) / (s - cars[stk[-1]][1]) >= res[stk[-1]] > 0):
                stk.pop()

            if stk:
                res[i] = (cars[stk[-1]][0] - p) / (s - cars[stk[-1]][1])
            stk.append(i)

        return res

    # brute force, TLE
    def getCollisionTimes1(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        res = [-1] * n
        for i in range(n - 1, -1, -1):
            t = min([(cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1]) for j in range(i, n) if cars[j][1] < cars[i][1]], default=-1)
            res[i] = t
        return res


def test_get_collision_times():
    solution = Solution()
    assert solution.getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]) == [1.00000, -1.00000, 3.00000,
                                                                            -1.00000], 'wrong result'
    assert solution.getCollisionTimes([[3, 4], [5, 4], [6, 3], [9, 1]]) == [2.00000, 1.00000, 1.50000,
                                                                            -1.00000], 'wrong result'


if __name__ == '__main__':
    test_get_collision_times()

