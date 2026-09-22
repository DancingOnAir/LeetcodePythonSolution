class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    res += 1
        return res


def test_count_intersecting_intervals():
    solution = Solution()
    assert solution.countIntersectingIntervals([[1,2],[2,3],[3,4]]) == 2, 'wrong result'
    assert solution.countIntersectingIntervals([[1,5],[2,4],[3,6]]) == 3, 'wrong result'
    assert solution.countIntersectingIntervals([[1,2],[3,4],[5,6]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_intersecting_intervals()
