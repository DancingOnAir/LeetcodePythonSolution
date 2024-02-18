from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(t):
            return int(t[:2]) * 60 + int(t[3:])

        timePoints.sort()
        res = helper(timePoints[0]) + 1440 - helper(timePoints[-1])
        for i in range(len(timePoints) - 1):
            res = min(res, helper(timePoints[i+1]) - helper(timePoints[i]))
        return res


def test_find_min_difference():
    solution = Solution()
    assert solution.findMinDifference(["23:59", "00:00"]) == 1, 'wrong result'
    assert solution.findMinDifference(["00:00", "23:59", "00:00"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_find_min_difference()
