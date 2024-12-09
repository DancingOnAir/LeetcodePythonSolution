from typing import List
from collections import Counter


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = float('-inf')
        tot = sum(nums)
        for y in nums:
            t = tot - y * 2
            if t in cnt and (t != y or cnt[t] > 1):
                res = max(res, t)
        return res


def test_get_largest_outlier():
    solution = Solution()
    assert solution.getLargestOutlier([6, -31, 50, -35, 41, 37, -42, 13]) == -35, 'wrong result'
    assert solution.getLargestOutlier([2, 3, 5, 10]) == 10, 'wrong result'
    assert solution.getLargestOutlier([-2, -1, -3, -6, 4]) == 4, 'wrong result'
    assert solution.getLargestOutlier([1, 1, 1, 1, 1, 5, 5]) == 5, 'wrong result'


if __name__ == '__main__':
    test_get_largest_outlier()
