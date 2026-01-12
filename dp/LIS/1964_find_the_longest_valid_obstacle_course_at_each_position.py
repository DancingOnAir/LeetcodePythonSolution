from typing import List
from functools import lru_cache
from bisect import bisect_right


class Solution:
    # binary search
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        g = list()
        res = list()
        for x in obstacles:
            j = bisect_right(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            res.append(j + 1)
        return res

    # TLE dp
    def longestObstacleCourseAtEachPosition2(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)

        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return dp

    # TLE dfs
    def longestObstacleCourseAtEachPosition1(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)

        @lru_cache(None)
        def dfs(i):
            sz = 0

            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    sz = max(sz, dfs(j))
            return sz + 1

        return [dfs(i) for i in range(n)]


def test_longest_obstacle_course_at_each_position():
    solution = Solution()
    assert solution.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3], 'wrong result'
    assert solution.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1], 'wrong result'
    assert solution.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2], 'wrong result'


if __name__ == '__main__':
    test_longest_obstacle_course_at_each_position()
