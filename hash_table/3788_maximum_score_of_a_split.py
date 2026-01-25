from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        tot = sum(nums)
        mi = float('inf')
        res = float('-inf')
        for i in range(len(nums) - 1, 0, -1):
            cur = nums[i]
            mi = min(cur, mi)
            tot -= cur
            res = max(res, tot - mi)
        return res


def test_maximum_score():
    solution = Solution()
    assert solution.maximumScore([10, -1, 3, -4, -5]) == 17, 'wrong result'
    assert solution.maximumScore([-7, -5, 3]) == -2, 'wrong result'
    assert solution.maximumScore([1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_score()
