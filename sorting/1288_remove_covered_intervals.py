class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, max_right = intervals[0]
        res = 1
        for l, r in intervals[1:]:
            if left <= l and r <= max_right:
                continue
            res += 1
            if max_right < r:
                max_right = r
                left = l
        return res


def test_remove_covered_intervals():
    solution = Solution()
    assert solution.removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2, 'wrong result'
    assert solution.removeCoveredIntervals([[1,4],[2,3]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_remove_covered_intervals()

