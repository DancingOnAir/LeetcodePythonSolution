from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = res = 0
        while res < len(nums):
            total += nums[res]
            if total <= 0:
                return res
            res += 1
        return res


def test_max_score():
    solution = Solution()
    assert solution.maxScore([-687767,-860350,950296,52109,510127,545329,-291223,-966728,852403,828596,456730,-483632,-529386,356766,147293,572374,243605,931468,641668,494446]) == 20, 'wrong result'
    assert solution.maxScore([2, -1, 0, 1, -3, 3, -3]) == 6, 'wrong result'
    assert solution.maxScore([-2, -3, 0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_score()
