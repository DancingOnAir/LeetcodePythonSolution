from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i: i+3])
        return 0


def test_largest_perimeter():
    solution = Solution()
    assert solution.largestPerimeter([2, 1, 2]) == 5, 'wrong result'
    assert solution.largestPerimeter([1, 2, 1, 10]) == 0, 'wrong result'


if __name__ == '__main__':
    test_largest_perimeter()
