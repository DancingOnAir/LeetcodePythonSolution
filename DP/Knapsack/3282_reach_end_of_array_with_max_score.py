from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = mx = 0
        for x in nums[:-1]:
            mx = max(mx, x)
            res += mx
        return res


def test_find_maximum_score():
    solution = Solution()
    assert solution.findMaximumScore([1, 3, 1, 5]) == 7, 'wrong result'
    assert solution.findMaximumScore([4, 3, 1, 3, 2]) == 16, 'wrong result'


if __name__ == '__main__':
    test_find_maximum_score()
