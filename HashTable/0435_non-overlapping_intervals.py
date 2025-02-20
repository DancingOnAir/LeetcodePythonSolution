from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        non_overlap = 0
        pre_r = float('-inf')
        for l, r in intervals:
            if l >= pre_r:
                non_overlap += 1
                pre_r = r
        return len(intervals) - non_overlap


def test_erase_overlap_intervals():
    solution = Solution()
    assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1, 'wrong result'
    assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2, 'wrong result'
    assert solution.eraseOverlapIntervals([[1,2],[2,3]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_erase_overlap_intervals()
