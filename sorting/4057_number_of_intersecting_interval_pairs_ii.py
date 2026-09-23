from bisect import bisect_right


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return 0
        intervals.sort(key=lambda x: x[0])
        starts = [x[0] for x in intervals]
        non_intersecting = 0
        for _, end in intervals:
            i = bisect_right(starts, end)
            non_intersecting += n - i
        return n * (n - 1) // 2 - non_intersecting


def test_count_intersecting_intervals():
    solution = Solution()
    assert solution.countIntersectingIntervals([[1,2],[2,3],[3,4]]) == 2, 'wrong result'
    assert solution.countIntersectingIntervals([[1,5],[2,4],[3,6]]) == 3, 'wrong result'
    assert solution.countIntersectingIntervals([[1,2],[3,4],[5,6]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_intersecting_intervals()
