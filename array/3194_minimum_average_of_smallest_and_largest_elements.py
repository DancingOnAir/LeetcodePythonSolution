from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res = nums[-1]
        for i in range(len(nums) // 2):
            res = min(res, (nums[i] + nums[len(nums) - i - 1]) / 2)
        return res

    def minimumAverage1(self, nums: List[int]) -> float:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 50
        while l < r:
            res = min(res, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return res


def test_minimum_average():
    solution = Solution()
    eps = 1e-6
    assert abs(solution.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]) - 5.5) < eps, 'wrong result'
    assert abs(solution.minimumAverage([1, 9, 8, 3, 10, 5]) - 5.5) < eps, 'wrong result'
    assert abs(solution.minimumAverage([1, 2, 3, 7, 8, 9]) - 5.0) < eps, 'wrong result'


if __name__ == '__main__':
    test_minimum_average()
