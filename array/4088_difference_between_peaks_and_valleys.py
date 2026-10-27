class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                res += nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                res -= nums[i]
        return res


def test_peak_valley_difference():
    solution = Solution()
    assert solution.peakValleyDifference([1, 5, 2, 4, 1, 3, 0]) == 9, 'wrong result'
    assert solution.peakValleyDifference([-5, -6, -1, -2, 5, 3, 2]) == 12, 'wrong result'
    assert solution.peakValleyDifference([6, 5, 2, 5, 5, 3, 6]) == -5, 'wrong result'


if __name__ == '__main__':
    test_peak_valley_difference()
